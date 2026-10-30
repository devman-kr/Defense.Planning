# 코드리뷰_집계.py — 과제 폴더들의 처리표(`03_작업기록/코드리뷰_*/처리.md`)를 모아 지표 행 초안 · 영역 × 처리 표 · 「같은 영역 + 같은 파일 3세션」 목록을 낸다.
#
# 왜: 코드리뷰_가이드.md 7절 루프(「틀림」 2회 유형 → 기준 수정, 「고침」 2회 유형 → 결정론 층) · 10절 지표 행 · 6절 「3회 반복」(가로지르기)은
#     처리표를 모아 세어야 한다(X-14, 2026-10-21). 과제 종결 때 계획 세션이 돌리고, 결과를 보고 판정한다 — 이 스크립트는 세기만 한다.
#
# 쓰는 법(Planning 루트에서):
#   python3 -X utf8 -I _도구/코드리뷰_집계.py                 # 전체(z.completed 포함) — 표준 출력
#   python3 -X utf8 -I _도구/코드리뷰_집계.py --task P01      # 과제 하나(지표 행 초안용)
#   python3 -X utf8 -I _도구/코드리뷰_집계.py --write         # 전체 결과를 코드리뷰_집계.md 로 덮어쓴다(과제 종결 때)
#   --write 는 파일 맨 앞에 프론트매터(_공통/문서규약.md — register · final · living)를 붙인다. 이미 있는 파일의 id · created 는
#   이어 쓰고 updated 는 실행일. 표준 출력에는 붙이지 않는다.
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
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ID_RE = re.compile(r"^`?([A-Z]\d{2}[A-Za-z0-9]*)\.([^.`|]+)\.([A-Z]+)\.(\d+)`?$")
# 영역 코드는 가이드 부록 A(Unity 판, X-03) — 바꾸면 같이 바꾼다
AREAS = ["SAVE", "ECON", "LIFE", "TIME", "PERF", "INPUT", "CONTRACT", "TEST", "UI", "BUILD"]
PROCS = ["고침", "틀림", "의도", "범위 밖", "처리 안 함", "미해결"]

# ── 프론트매터 쓰기(_공통/문서규약.md 2 · 9절). python3 -I 라 다른 모듈을 불러오지 않고 스크립트마다 같은 함수를 둔다
FM_QUOTE_START = tuple("-?:,[]{}#&*!|>'\"%@`")  # 9절 4번 — 이 글자로 시작하는 값은 따옴표
FM_QUOTE_WORDS = {"true", "false", "yes", "no", "on", "off", "null", "~"}
FM_ID_RE = re.compile(r"^\d{8}-[a-z0-9-]{2,40}$")
FM_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


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


def existing_head(path: str):
    """이미 있는 파일 프론트매터의 (id, created) — 없거나 id 가 형식에 맞지 않으면 (None, None)."""
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.read().split("\n")
    except (OSError, UnicodeDecodeError):
        return None, None
    if lines[0] != "---":
        return None, None
    found = {}
    for line in lines[1:]:
        if line == "---":
            break
        key, sep, value = line.partition(": ")
        if sep:
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] == '"':
                value = re.sub(r'\\(["\\])', r"\1", value[1:-1])
            found[key] = value
    else:
        return None, None  # 닫는 --- 가 없다
    fid, created = found.get("id", ""), found.get("created", "")
    if not FM_ID_RE.match(fid):
        return None, None
    if not FM_DATE_RE.match(created):
        created = f"{fid[:4]}-{fid[4:6]}-{fid[6:8]}"  # id 의 날짜가 created 다(규약 4절)
    return fid, created


def aggregate_frontmatter(path: str, summary: str) -> str:
    """코드리뷰_집계.md 의 프론트매터 — register · final · living, updated 는 실행일."""
    today = datetime.now().strftime("%Y-%m-%d")
    fid, created = existing_head(path)
    return fm_block([
        ("id", fid or f"{today.replace('-', '')}-review-aggregate"),
        ("title", "코드리뷰 집계"),
        ("summary", fm_clip(summary, 200)),
        ("doc_type", "register"),
        ("status", "final"),
        ("lifecycle", "living"),
        ("created", created or today),
        ("updated", today),
    ])


def norm_proc(v: str) -> str:
    v = v.strip()
    for p in PROCS:
        if v.startswith(p):
            return p
    return "기타(" + v[:10] + ")"


LINE_RE = re.compile(r":\d+(?:-\d+)?$")
# 파일로 볼 확장자 — 점이 든 일반 단어(`API.Spec` · `Time.timeScale` · `v1.2`)를 파일로 잡지 않게 목록으로 가른다.
# 목록 밖 확장자라도 경로(`/` · `\`)가 붙어 있으면 파일로 본다
EXTS = {
    "cs", "asmdef", "asmref", "asset", "unity", "prefab", "mat", "meta", "shader", "shadergraph", "shadersubgraph",
    "hlsl", "cginc", "compute", "uss", "uxml", "tss", "inputactions", "anim", "controller", "overridecontroller",
    "mask", "physicmaterial", "rendertexture", "playable", "spriteatlas", "png", "jpg", "jpeg", "tga", "psd", "exr",
    "fbx", "glb", "gltf", "obj", "blend", "wav", "ogg", "mp3", "ttf", "otf", "md", "json", "jsonl", "py", "sh",
    "yml", "yaml", "xml", "js", "ts", "html", "css", "txt", "csv", "ini", "cfg", "toml",
    "vue", "jsx", "tsx", "scss", "razor", "dart", "sql", "csproj", "sln", "props", "targets",
}
DOTFILES = {".gitignore", ".gitattributes", ".editorconfig", ".globalconfig", ".dockerignore"}
PATH_RE = re.compile(r"(?<![\w.])([\w./\\-]*\.([A-Za-z][A-Za-z0-9]*))(?![A-Za-z0-9])")
SEG_RE = re.compile(r"^([^`:·,;#]*?\.([A-Za-z][A-Za-z0-9]*))(?=$|[\s:·,;#])")


def first_file(cell: str) -> str:
    # 「파일:줄」 칸의 첫 파일 이름 — 같은 파일을 줄이 달라도 한 키로 묶는다(6절 「3회 반복」). 칸을 왼쪽부터 본다
    for piece in re.split(r"(`[^`]*`)", cell):
        if piece.startswith("`") and piece.endswith("`") and len(piece) > 1:
            # 백틱 안은 공백 · 괄호가 든 이름도 통째로(`Assets/Mats/New Material 1.mat:2` · `Foo_01 (1).png`)
            m = SEG_RE.match(piece[1:-1].strip())
            if m and m.group(2).lower() in EXTS:
                return os.path.basename(m.group(1).replace("\\", "/"))
        # 조사 · 기호 · 줄 표기(`SaveData.cs의` · `**Foo.cs:12**` · `Foo.cs#L41`)는 경계에서 떨어진다
        for m in PATH_RE.finditer(piece):
            path = m.group(1)
            name = os.path.basename(path.replace("\\", "/"))
            if m.group(2).lower() in EXTS or name in DOTFILES or "/" in path or "\\" in path:
                return name
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
        path = os.path.join(ROOT, "코드리뷰_집계.md")
        scope = f"과제 {task_filter} 의" if task_filter else f"과제 {len(by_task)}개의"
        head = aggregate_frontmatter(path, f"{scope} 처리표 {len(set(r['folder'] for r in rows))}개 · 지적 {len(rows)}건을 처리 · 영역별로 "
                                           f"센 결과다(같은 파일 3세션 후보 {len(hits)}건 · 미해결 · 반박 {len(unresolved)}건).")
        with open(path, "w", encoding="utf-8", newline="\n") as f:  # 프론트매터는 파일을 열기 전에 만든다
            f.write(head + text)
        print(f"→ {os.path.join(ROOT, '코드리뷰_집계.md')}")


if __name__ == "__main__":
    main()
