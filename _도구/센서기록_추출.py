# 센서기록_추출.py — 코드 리뷰 센서(서브에이전트)의 지시 원문 · 최종 보고 · 토큰을 세션 기록에서 뽑아 파일로 남긴다.
#
# 왜: 센서 · 검증 · 반론 에이전트의 보고 원문은 세션 기록(`~/.claude/projects/<작업 공간 경로를 바꾼 이름>/<세션 id>/subagents/agent-*.jsonl`)에만
#     남고, 그 기록은 영구 보존이 아니다. 작업 보고 「코드 리뷰」 절은 압축본이라 나중의 검산 · 유형 집계 · 반론 이력 추적에 모자란다
#     (코드리뷰_가이드.md 8절 — 2026-10-21 검토서). 센서가 끝난 직후 작성 세션이 이 스크립트로 원문을 과제 폴더에 복사한다.
#
# 쓰는 법(한글 출력 때문에 -X utf8 필수, 스크립트 자체는 표준 라이브러리만 쓴다):
#   python3 -X utf8 -I _도구/센서기록_추출.py <세션 id 또는 subagents 폴더> <출력 폴더> [--only <에이전트 id 접두,...>]
#   예) python3 -X utf8 -I _도구/센서기록_추출.py 0f0e49ba-0279-4b34-a2d3-08d4d6981e33 "P00_환경_체계_로깅/03_작업기록/코드리뷰_20261030_S1"
#   세션 id 만 주면 `~/.claude/projects/*/<세션 id>/subagents` 를 찾는다(세션 id 는 프로젝트를 가로질러 하나뿐이다).
#   여러 개 · 0개면 멈춘다 — 그때는 subagents 폴더 경로를 통째로 넘긴다(가이드 8.1).
#   Mac 기본 python3 는 3.9 다 — 아래 __future__ 줄이 `str | None` 표기를 3.9 에서도 돌게 한다.
#
# 산출(출력 폴더):
#   agent-<id>_final.md   — 에이전트의 최종 보고(마지막 `SubagentHandback` 메시지. 없으면 마지막 assistant 텍스트). 한 글자도 고치지 않는다.
#   agent-<id>_prompt.md  — 작성 세션이 보낸 첫 지시 원문.
#   summary.json · 표준 출력의 마크다운 표 — 역할 설명(meta.json description) · 모델 · 시작 · 끝(KST) · 도구 호출 수 · 토큰.
# 역할(A · B · C · D · 2라운드)은 description 과 prompt 첫 줄로 구분해 작성 세션이 파일 이름을 바꾼다(선례: 1_센서A_opus.md …).
# 비밀값 · 토큰 문자열이 섞였는지는 작성 세션이 눈으로 확인한다 — 스크립트는 가리지 않는다.
#
# 새 토큰 = cache_creation_input_tokens + input_tokens + output_tokens(가이드 8절 · 지표.md 의 정의와 같다). cache_read 는 참고로만 적는다.
# 세션 기록이 아닌 폴더 · 다른 사람 세션을 가리키면 안 된다. 다른 과제의 기록을 읽어 쓰지 않는다.

from __future__ import annotations

import glob
import json
import os
import sys
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))


def resolve_src(arg: str) -> str:
    if os.path.isdir(arg):
        return arg
    pattern = os.path.join(os.path.expanduser("~"), ".claude", "projects", "*", arg, "subagents")
    found = [p for p in glob.glob(pattern) if os.path.isdir(p)]
    if len(found) == 1:
        return found[0]
    sys.exit(f"subagents 폴더를 하나로 찾지 못했다: {arg} (찾은 수 {len(found)}, 시도: {pattern})")


def to_kst(ts: str | None) -> str:
    if not ts:
        return ""
    dt = datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(KST)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def extract(path: str) -> dict:
    aid = os.path.basename(path)[:-len(".jsonl")]
    meta_path = path[:-len(".jsonl")] + ".meta.json"
    meta = json.load(open(meta_path, encoding="utf-8")) if os.path.exists(meta_path) else {}
    first_user = None
    handback = None
    last_text = None
    cc = inp = outp = cr = 0
    first_ts = last_ts = None
    model = None
    ntool = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            if r.get("type") not in ("user", "assistant"):
                continue
            ts = r.get("timestamp")
            if ts:
                first_ts = first_ts or ts
                last_ts = ts
            m = r.get("message") or {}
            ct = m.get("content")
            if m.get("role") == "user" and first_user is None:
                if isinstance(ct, str):
                    first_user = ct
                elif isinstance(ct, list):
                    t = [c.get("text", "") for c in ct if isinstance(c, dict) and c.get("type") == "text"]
                    if t:
                        first_user = "\n".join(t)
            elif m.get("role") == "assistant":
                u = m.get("usage") or {}
                cc += u.get("cache_creation_input_tokens") or 0
                inp += u.get("input_tokens") or 0
                outp += u.get("output_tokens") or 0
                cr += u.get("cache_read_input_tokens") or 0
                model = m.get("model") or model
                if isinstance(ct, list):
                    for c in ct:
                        if not isinstance(c, dict):
                            continue
                        if c.get("type") == "tool_use":
                            ntool += 1
                            if c.get("name") == "SubagentHandback":
                                handback = (c.get("input") or {}).get("message")
                        elif c.get("type") == "text" and c.get("text", "").strip():
                            last_text = c["text"]
    return dict(
        id=aid, description=meta.get("description"), model_requested=meta.get("model"), model=model,
        start_kst=to_kst(first_ts), end_kst=to_kst(last_ts), tool_calls=ntool,
        cache_creation=cc, input=inp, output=outp, cache_read=cr, new_tokens=cc + inp + outp,
        final_source="SubagentHandback" if handback else ("last_text" if last_text else "none"),
        prompt=first_user or "", final=handback or last_text or "",
    )


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__ or "인자: <세션 id 또는 subagents 폴더> <출력 폴더> [--only a,b]")
    src = resolve_src(sys.argv[1])
    out = sys.argv[2]
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1].split(",")
    os.makedirs(out, exist_ok=True)
    rows = []
    for path in sorted(glob.glob(os.path.join(src, "agent-*.jsonl"))):
        aid = os.path.basename(path)[:-len(".jsonl")]
        if only and not any(aid.startswith("agent-" + o) or aid.startswith(o) for o in only):
            continue
        r = extract(path)
        with open(os.path.join(out, aid + "_prompt.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(r.pop("prompt"))
        with open(os.path.join(out, aid + "_final.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(r.pop("final"))
        rows.append(r)
    with open(os.path.join(out, "summary.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    print("| 에이전트 | 설명 | 모델 | 시작(KST) | 끝(KST) | 도구 호출 | 새 토큰 | cache_read | 보고 출처 |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| `{r['id']}` | {r['description']} | {r['model']} | {r['start_kst']} | {r['end_kst']} | {r['tool_calls']} | "
              f"{r['new_tokens']:,} | {r['cache_read']:,} | {r['final_source']} |")
    total = sum(r["new_tokens"] for r in rows)
    print(f"\n에이전트 {len(rows)} · 새 토큰 합 {total:,}")


if __name__ == "__main__":
    main()
