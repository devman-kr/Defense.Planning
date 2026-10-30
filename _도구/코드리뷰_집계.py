# 코드리뷰_집계.py — 과제 폴더들의 처리표(`03_작업기록/코드리뷰_*/처리.md`)를 모아 지표 행 초안 · 영역 × 처리 표 · 「같은 영역 + 같은 파일 3세션」 목록을 낸다.
#
# 왜: 코드리뷰_가이드.md 7절 루프(「틀림」 2회 유형 → 기준 수정, 「고침」 2회 유형 → 결정론 층) · 10절 지표 행 · 6절 「3회 반복」(가로지르기)은
#     처리표를 모아 세어야 한다(X-14, 2026-10-21). 과제 종결 때 계획 세션이 돌리고, 결과를 보고 판정한다 — 이 스크립트는 세기만 한다.
#
# 쓰는 법(Planning 루트에서):
#   python3 -X utf8 -I _도구/코드리뷰_집계.py                 # 전체(z.completed 포함) — 표준 출력
#   python3 -X utf8 -I _도구/코드리뷰_집계.py --task P01      # 과제 하나(지표 행 초안용)
#   python3 -X utf8 -I _도구/코드리뷰_집계.py --write         # 전체 결과를 코드리뷰_집계.md 로 덮어쓴다(과제 종결 때)
#
# 읽는 것: 처리.md 의 표 행 가운데 첫 칸이 식별자(`<과제>.<세션>.<저장소>.<번호>`)인 행. 열 순서는 가이드 8절 고정 —
#   식별자 · 원본 · 라운드 · 종류 · 심각도 · 기원 · 영역 · 유형 · 파일:줄 · 실패 시나리오 · 확신 · 처리 · 근거 · 커밋 · 반론 (14열).
#   같은 폴더의 summary.json(센서기록_추출.py 산출)이 있으면 에이전트 수 · 새 토큰을 더한다.
# 처리 값: 고침 · 틀림 · 의도 · 범위 밖 · 처리 안 함 · 미해결(앞 글자 일치). 「미해결」은 사용자 판정 대기 행.
# 3회 목록: 영역 + 파일 이름(파일:줄 칸의 첫 경로, 줄 번호 제외)이 같은 행이 서로 다른 세션 3개 이상에서 나오면 올린다.

import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ID_RE = re.compile(r"^`?([A-Z]\d{2}[A-Za-z0-9]*)\.([^.`|]+)\.([A-Z]+)\.(\d+)`?$")
# 영역 코드는 가이드 부록 A(Unity 판, X-03) — 바꾸면 같이 바꾼다
AREAS = ["SAVE", "ECON", "LIFE", "TIME", "PERF", "INPUT", "CONTRACT", "TEST", "UI", "BUILD"]
PROCS = ["고침", "틀림", "의도", "범위 밖", "처리 안 함", "미해결"]


def norm_proc(v: str) -> str:
    v = v.strip()
    for p in PROCS:
        if v.startswith(p):
            return p
    return "기타(" + v[:10] + ")"


LINE_RE = re.compile(r":\d+(?:-\d+)?$")
FILE_RE = re.compile(r"[\w./\\-]*\.[A-Za-z0-9]+")


def first_file(cell: str) -> str:
    # 칸의 첫 「경로.확장자」 토큰 — 확장자 목록에 묶지 않는다(Unity 파일 종류가 많고, 목록은 접두 일치로 `.shadergraph` 를 `.shader` 로 자른다)
    for tok in re.split(r"[\s,`()]+", cell):
        tok = LINE_RE.sub("", tok)
        if FILE_RE.fullmatch(tok):
            return os.path.basename(tok.replace("\\", "/"))
    return LINE_RE.sub("", cell.strip().split()[0].strip("`")) if cell.strip() else ""


def load_rows(path: str):
    rows = []
    for line in open(path, encoding="utf-8"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 12:
            continue
        m = ID_RE.match(cells[0])
        if not m:
            continue
        task, session, repo, num = m.groups()
        rows.append(dict(
            id=cells[0].strip("`"), task=task, session=session, repo=repo, num=int(num),
            round=cells[2], kind=cells[3], severity=cells[4], origin=cells[5], area=cells[6].strip("`"),
            type=cells[7], file=first_file(cells[8]), confidence=cells[10], proc=norm_proc(cells[11]),
            rebuttal=cells[13] if len(cells) > 13 else "", folder=os.path.relpath(os.path.dirname(path), ROOT),
        ))
    return rows


def main() -> None:
    args = sys.argv[1:]
    task_filter = args[args.index("--task") + 1] if "--task" in args else None
    write = "--write" in args
    paths = sorted(glob.glob(os.path.join(ROOT, "**", "03_작업기록", "코드리뷰_*", "처리.md"), recursive=True))
    rows, agents, tokens = [], Counter(), Counter()
    for p in paths:
        r = load_rows(p)
        if not r:
            continue
        if task_filter and r[0]["task"] != task_filter:
            continue
        rows += r
        sj = os.path.join(os.path.dirname(p), "summary.json")
        if os.path.exists(sj):
            s = json.load(open(sj, encoding="utf-8"))
            agents[r[0]["task"]] += len(s)
            tokens[r[0]["task"]] += sum(x.get("new_tokens", 0) for x in s)
    out = []
    out.append(f"# 코드 리뷰 집계 — 처리표 {len(set(r['folder'] for r in rows))}개 · 지적 {len(rows)}건" + (f" (과제 {task_filter})" if task_filter else ""))
    out.append("")
    out.append("`_도구/코드리뷰_집계.py` 산출(과제 종결 때 덮어쓰기). 판정은 계획 세션이 한다 — 가이드 7절 루프 · 10절 지표 · 6절 「3회 반복」.")
    out.append("")
    # 1. 지표 행 초안
    out.append("## 1. 지표 행 초안 (과제별 — `지표.md` 열 가운데 리뷰 열만)")
    out.append("")
    out.append("| 과제 | 리뷰 횟수(폴더) | 지적 | 고침 | 틀림 | 의도 | 범위 밖 | 처리 안 함 | 미해결 | 에이전트 | 새 토큰 |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|")
    by_task = defaultdict(list)
    for r in rows:
        by_task[r["task"]].append(r)
    for t, rs in sorted(by_task.items()):
        c = Counter(r["proc"] for r in rs)
        folders = len(set(r["folder"] for r in rs))
        out.append(f"| {t} | {folders} | {len(rs)} | {c['고침']} | {c['틀림']} | {c['의도']} | {c['범위 밖']} | {c['처리 안 함']} | {c['미해결']} | {agents[t] or '—'} | {tokens[t]:,} |" if tokens[t] else
                   f"| {t} | {folders} | {len(rs)} | {c['고침']} | {c['틀림']} | {c['의도']} | {c['범위 밖']} | {c['처리 안 함']} | {c['미해결']} | {agents[t] or '—'} | — |")
    out.append("")
    # 2. 영역 × 처리
    out.append("## 2. 영역 × 처리 (7절 루프 — 「틀림」 2 이상 · 「고침」 2 이상인 영역부터 자유 유형을 묶어 본다)")
    out.append("")
    out.append("| 영역 | 지적 | 고침 | 틀림 | 의도 | 범위 밖 | 처리 안 함 | 미해결 | 식별자 |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    by_area = defaultdict(list)
    for r in rows:
        by_area[r["area"]].append(r)
    for a in AREAS + sorted(set(by_area) - set(AREAS)):
        rs = by_area.get(a, [])
        if not rs:
            continue
        c = Counter(r["proc"] for r in rs)
        ids = " ".join(f"`{r['id']}`" for r in rs)
        out.append(f"| `{a}` | {len(rs)} | {c['고침']} | {c['틀림']} | {c['의도']} | {c['범위 밖']} | {c['처리 안 함']} | {c['미해결']} | {ids} |")
    out.append("")
    # 3. 같은 저장소 · 같은 영역 · 같은 파일 3세션
    #    저장소를 키에 넣는다 — 저장소가 다른 같은 이름의 파일을 이름만으로 묶으면 거짓 후보가 난다(EasyCheck 검산 2026-10-22).
    #    한 과제의 구현 세션과 마일스톤 리뷰 세션이 같은 파일을 짚는 것은 둘로 세되 재발은 아니다 — 「과제 수」 열로 사람이 가른다.
    out.append("## 3. 같은 저장소 · 영역 · 파일이 세 세션 이상 (6절 「3회 반복」 가로지르기 — 사용자에게 올릴 후보. 과제 수 1 이면 구현 + 마일스톤 리뷰가 겹친 것일 수 있다)")
    out.append("")
    grp = defaultdict(list)
    for r in rows:
        if r["file"]:
            grp[(r["repo"], r["area"], r["file"])].append(r)

    def sessions(v):
        return sorted({f"{x['task']}.{x['session']}" for x in v})

    hits = [(k, v) for k, v in grp.items() if len(sessions(v)) >= 3]
    if hits:
        out.append("| 저장소 | 영역 | 파일 | 세션 수 | 과제 수 | 세션 | 식별자 · 유형 |")
        out.append("|---|---|---|---|---|---|---|")
        for (repo, a, f), v in sorted(hits, key=lambda kv: -len(kv[1])):
            ses = sessions(v)
            tasks = len({x["task"] for x in v})
            out.append(f"| {repo} | `{a}` | `{f}` | {len(ses)} | {tasks} | {' · '.join(ses)} | " + " · ".join(f"`{x['id']}` {x['type']}" for x in v) + " |")
    else:
        out.append("없음.")
    out.append("")
    # 4. 두 세션 (예고)
    pre = [(k, v) for k, v in grp.items() if len(sessions(v)) == 2]
    out.append("## 4. 두 세션 (다음에 한 번 더 나오면 3절로 — 참고)")
    out.append("")
    if pre:
        for (repo, a, f), v in sorted(pre):
            out.append(f"- {repo} `{a}` `{f}` — 세션 {' · '.join(sessions(v))} — " + " · ".join(f"`{x['id']}`" for x in v))
    else:
        out.append("없음.")
    out.append("")
    # 5. 미해결 · 반박
    unresolved = [r for r in rows if r["proc"] == "미해결" or r["rebuttal"].startswith("반박")]
    out.append("## 5. 미해결 · 반론 반박 행")
    out.append("")
    out.extend(f"- `{r['id']}` {r['type']} — {r['proc']} / {r['rebuttal'][:80]}" for r in unresolved) if unresolved else out.append("없음.")
    out.append("")
    text = "\n".join(out) + "\n"
    print(text)
    if write:
        with open(os.path.join(ROOT, "코드리뷰_집계.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print(f"→ {os.path.join(ROOT, '코드리뷰_집계.md')}")


if __name__ == "__main__":
    main()
