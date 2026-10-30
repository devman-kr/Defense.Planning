# 센서기록_추출.py — 코드 리뷰 센서(서브에이전트)의 지시 원문 · 최종 보고 · 토큰을 세션 기록에서 뽑아 파일로 남긴다.
#
# 왜: 센서 · 검증 · 반론 에이전트의 보고 원문은 세션 기록(`~/.claude/projects/<작업 공간 경로를 바꾼 이름>/<세션 id>/subagents/agent-*.jsonl`)에만
#     남고, 그 기록은 영구 보존이 아니다. 작업 보고 「코드 리뷰」 절은 압축본이라 나중의 검산 · 유형 집계 · 반론 이력 추적에 모자란다
#     (코드리뷰_가이드.md 8절 — 2026-10-21 검토서). 센서가 끝난 직후 작성 세션이 이 스크립트로 원문을 과제 폴더에 복사한다.
#
# 쓰는 법(한글 출력 때문에 -X utf8 필수, 스크립트 자체는 표준 라이브러리만 쓴다):
#   Planning 루트에서(출력 폴더는 실행한 곳 기준) python3 -X utf8 -I _도구/센서기록_추출.py <세션 id 또는 subagents 폴더> <출력 폴더> [--only <에이전트 id 접두,...>]
#   예) python3 -X utf8 -I _도구/센서기록_추출.py 0f0e49ba-0279-4b34-a2d3-08d4d6981e33 "P00_환경_체계_로깅/03_작업기록/코드리뷰_20261030_S1"
#   세션 id 만 주면 `~/.claude/projects/*/<세션 id>/subagents` 를 찾는다(세션 id 는 프로젝트를 가로질러 하나뿐이다).
#   여러 개 · 0개면 멈춘다 — 그때는 subagents 폴더 경로를 통째로 넘긴다(가이드 8.1).
#   Mac 기본 python3 는 3.9 다 — 아래 __future__ 줄이 `str | None` 표기를 3.9 에서도 돌게 한다.
#
# 산출(출력 폴더):
#   agent-<id>_final.md   — 에이전트의 최종 보고(마지막 `SubagentHandback` 메시지. 없으면 마지막 assistant 텍스트). 한 글자도 고치지 않는다.
#   agent-<id>_prompt.md  — 작성 세션이 보낸 첫 지시 원문.
#   두 .md 는 맨 앞에 프론트매터(_공통/문서규약.md — review · final · static)를 붙이고 바로 뒤에 원문을 그대로 둔다. id · created · work_unit 은
#   출력 폴더 경로 `…/Pnn_*/03_작업기록/코드리뷰_<YYYYMMDD>_<세션>/` 에서 얻는다(못 얻으면 실행일 · work_unit 생략). 파일 이름을 바꿔도 id 는 그대로.
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
import re
import sys
import unicodedata
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))

# ── 프론트매터 쓰기(_공통/문서규약.md 2 · 9절). python3 -I 라 다른 모듈을 불러오지 않고 스크립트마다 같은 함수를 둔다
FM_QUOTE_START = tuple("-?:,[]{}#&*!|>'\"%@`")  # 9절 4번 — 이 글자로 시작하는 값은 따옴표
FM_QUOTE_WORDS = {"true", "false", "yes", "no", "on", "off", "null", "~"}
RECORD_RE = re.compile(r"^코드리뷰_(\d{8})_(.+)$")


def fm_text(value) -> str:
    """값 한 줄 — 줄바꿈 · 제어 문자는 공백, { } 는 ( )(L17 자리표시와 겹치지 않게), 앞뒤 공백은 뗀다."""
    out = []
    for ch in str(value):
        code = ord(ch)
        if code < 0x20 or 0x7F <= code <= 0x9F or code in (0x2028, 0x2029) or 0xD800 <= code <= 0xDFFF:
            ch = " "
        out.append("(" if ch == "{" else ")" if ch == "}" else ch)
    return "".join(out).strip()


def fm_clip(text: str, limit: int) -> str:
    """limit 자 안으로 — 넘치면 끝 한 글자를 … 로."""
    return text if len(text) <= limit else text[:limit - 1].rstrip() + "…"


def fm_value(text: str) -> str:
    """9절 3 · 4번 — 맨 값으로 쓸 수 없으면 큰따옴표로 감싸고 안의 역슬래시 · 큰따옴표를 이스케이프한다."""
    if (not text or text != text.strip() or " #" in text or ": " in text or text.endswith(":")
            or text.startswith(FM_QUOTE_START) or text.lower() in FM_QUOTE_WORDS):
        return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return text


def fm_block(fields) -> str:
    """[(키, 값)] → `---` 로 감싼 블록(끝 줄바꿈 포함). 값이 None 인 키는 쓰지 않는다."""
    lines = ["---"] + [f"{key}: {fm_value(fm_text(value))}" for key, value in fields if value is not None]
    block = "\n".join(lines + ["---", ""])
    block.encode("utf-8")  # 쓸 수 없는 글자가 있으면 본문을 쓰기 전에 여기서 예외
    return block


def fm_slug(text: str) -> str:
    """id slug 조각 — 영소문자 · 숫자 밖의 글자는 하이픈으로."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def record_info(out: str):
    """출력 폴더 `…/Pnn_*/03_작업기록/코드리뷰_<YYYYMMDD>_<세션>/` → (YYYYMMDD, 세션, 과제 ID). 못 얻은 것은 None."""
    parts = unicodedata.normalize("NFC", os.path.abspath(out)).split(os.sep)
    day = session = task = None
    m = RECORD_RE.match(parts[-1])
    if m:
        session = m.group(2)
        try:
            datetime(int(m.group(1)[:4]), int(m.group(1)[4:6]), int(m.group(1)[6:]))
            day = m.group(1)
        except ValueError:
            pass
    if len(parts) >= 3 and parts[-2] == "03_작업기록":
        t = re.match(r"^(P\d{2})_", parts[-3])
        task = t.group(1) if t else None
    return day, session, task


def record_frontmatter(info, r: dict, kind: str) -> str:
    """센서 원본 한 파일(kind = final · prompt)의 프론트매터 — info 는 record_info 결과, r 은 extract 결과."""
    day, session, task = info
    day = day or datetime.now().strftime("%Y%m%d")  # 경로에서 못 얻으면 실행일
    id8 = (r["id"][len("agent-"):] if r["id"].startswith("agent-") else r["id"])[:8]
    pre = task.lower() if task else ""
    tail = "-".join(p for p in (fm_slug(id8), kind) if p)
    sess = fm_slug(session or "")[:max(0, 40 - len(pre) - len(tail) - 2)].strip("-")  # slug 40자 안
    what = "최종 보고 원문" if kind == "final" else "지시 원문"
    title = f"코드리뷰 {session} — 에이전트 {id8} {what}" if session else f"코드리뷰 — 에이전트 {id8} {what}"
    who = f"{r.get('model') or r.get('model_requested') or '?'} · 도구 호출 {r.get('tool_calls', 0)}"
    if kind == "final":
        summary = f"에이전트({who})가 돌려준 최종 보고 원문 — 출처 {r.get('final_source')}."
    else:
        summary = f"에이전트({who})에 작성 세션이 보낸 첫 지시 원문."
    desc = fm_text(r.get("description") or "")
    if desc:
        summary = f"「{fm_clip(desc, max(1, 200 - len(summary) - 3))}」 {summary}"
    date = f"{day[:4]}-{day[4:6]}-{day[6:]}"
    return fm_block([
        ("id", f"{day}-" + "-".join(p for p in (pre, sess, tail) if p)),
        ("title", fm_clip(title, 120)),
        ("summary", fm_clip(summary, 200)),
        ("doc_type", "review"),
        ("status", "final"),
        ("lifecycle", "static"),
        ("created", date),
        ("updated", date),
        ("work_unit", task),
    ])


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
    info = record_info(out)
    rows = []
    for path in sorted(glob.glob(os.path.join(src, "agent-*.jsonl"))):
        aid = os.path.basename(path)[:-len(".jsonl")]
        if only and not any(aid.startswith("agent-" + o) or aid.startswith(o) for o in only):
            continue
        r = extract(path)
        prompt, final = r.pop("prompt"), r.pop("final")
        heads = {kind: record_frontmatter(info, r, kind) for kind in ("prompt", "final")}  # 파일을 열기 전에 만든다
        with open(os.path.join(out, aid + "_prompt.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(heads["prompt"] + prompt)
        with open(os.path.join(out, aid + "_final.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(heads["final"] + final)
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
