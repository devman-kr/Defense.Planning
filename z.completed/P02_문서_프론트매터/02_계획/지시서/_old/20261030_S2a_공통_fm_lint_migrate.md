---
id: 20261030-p02-s2a-fm-lint-migrate
title: 작업지시서 — P02 · S2a · `_공통` fm_lint · fm_migrate
summary: 서브에이전트 B1(opus)에게 `_공통/_도구/fm_lint.py`(문서규약 11절 L01~L23 검사 · `--hook`)와 `fm_migrate.py`(draft · apply)와 unittest 시험을 맡긴다. 커밋과 실제 문서 쓰기는 하지 않는다.
doc_type: handoff
status: final
lifecycle: static
created: 2026-10-30
updated: 2026-10-30
work_unit: P02
implements: [20261030-p02-plan-frontmatter]
---

# 작업지시서 — P02 · S2a · `_공통` fm_lint · fm_migrate

계획서 2절 분할표 S2a 행(B1)의 지시서다. 리드(주 세션 af266641)가 `Agent` 도구로 아래 본문을 넘긴다. S2b(B2 — 로그 훅 · Planning 도구)와 동시에 돈다.

---

## 프롬프트 본문 (여기부터 붙여 넣는다)

이 지시서는 Opus 5.5 기준으로 썼다(가이드 확인일 2026-10-30). 세션 모델이 다르면 보고 첫 줄에 알린다.

### 맡는 일

과제 P02(문서 프론트매터) · 분할표 S2a. 세 게임 작업 공간과 `_공통` 의 모든 마크다운이 YAML 프론트매터로 시작하게 하는 규약이 `/Users/devman/_Projects/_Personal/Games/_공통/문서규약.md`(이하 규약)에 있다. 이 규약을 기계로 지키게 하는 도구 둘을 만든다. **검사기** `fm_lint.py` 는 규약 11절 규칙 L01~L23 을 검사하고, 커밋 전 검사와 Claude Code `PostToolUse` 훅(`--hook`)에 쓰인다. **이행기** `fm_migrate.py` 는 다음 단계(S3)에서 기존 문서 약 130건에 프론트매터를 붙이는 데 한 번 쓰인다. 끝나면 리드가 이 둘로 세 게임 전체를 검사하고 이행한다. 결과물은 다른 두 게임도 그대로 쓰므로 단순하고 읽기 쉽게 만든다 — 사용자는 1인 포트폴리오를 가볍게 운영하길 원한다.

### 성공 기준

1. `python3 -I -m unittest discover -s /Users/devman/_Projects/_Personal/Games/_공통/_도구/tests` 가 전부 통과한다(B2 의 시험 파일도 같은 폴더에 생긴다 — 그 파일이 아직 미완이면 네 시험 파일만 돌린 결과를 따로 적는다).
2. 규약 11절 규칙마다 위반 한 건 · 정상 한 건의 시험이 있다. 경계값(summary 200자 · title 120자 · slug 2~40자)은 시험 코드에 숫자로 직접 적는다 — 검사기 상수를 시험에서 다시 쓰면 그 상수는 시험되지 않는다(Clew M03 교훈).
3. 검사기의 어휘 상수(doc_type 13 · status · lifecycle · work_type · 영역 코드 10)가 규약 2 · 3 · 8절 표와 같은지 보는 시험이 하나 있다 — 실제 규약 파일을 읽어 대조한다.
4. 기준선: Games 루트에서 `python3 -I _공통/_도구/fm_lint.py Defense AirShooter RideShooter _공통 CLAUDE.md` 의 출력과 종료 코드를 `/private/tmp/claude-501/-Users-devman--Projects--Personal-Games-Defense/af266641-28cb-4e0c-8761-a8ed2ac6f364/scratchpad/p02/b1/baseline.txt` 에 남기고, 규칙별 건수를 보고에 적는다. 지금은 대부분 L01 경고가 나와야 한다.
5. `python3 -I _공통/_도구/fm_migrate.py draft Defense --out <위 scratchpad>/p02/b1/draft_Defense.json` 이 돌고, 경로 관례 · git 이력으로 채운 항목 표본 5개를 보고에 붙인다.
6. `apply` 는 임시 폴더의 사본(시험 자료)에서만 돌렸고, 본문 바이트가 그대로이며 블록만 앞에 붙는다는 시험이 있다.

### 위험 등급 · 되돌리는 법

중 — 새 도구라 지금 돌아가는 것을 깨지 않는다. 다만 S4 부터 세 게임 모든 세션의 훅이 `fm_lint.py --hook` 를 부른다. 리드가 커밋하므로 되돌리기는 `git revert`.

### 승인 지점

없음. 아래 「금지」에 걸리는 일이 필요해 보이면 하지 말고 보고한다.

### 작업 위치

- Games 루트: `/Users/devman/_Projects/_Personal/Games`. 저장소 `_공통`(git, `main`). 시작 상태 `a28bbd1`.
- **수정 허용 영역**: `_공통/_도구/fm_lint.py` · `_공통/_도구/fm_migrate.py` · `_공통/_도구/tests/test_fm_lint.py` · `_공통/_도구/tests/test_fm_migrate.py` · `_공통/_도구/tests/fixtures/` 아래(시험용 가짜 Games 트리) · 위 scratchpad `p02/b1/` 아래.
- **읽기 전용**: 그 밖 전부. 특히 규약 · 템플릿 · 모든 문서 · `_공통/_도구/` 의 로그 훅 두 개(B2 가 스크래치에서 고친다) · `_공통/_도구/tests/test_log_frontmatter.py`(B2).
- 시작 전에 읽을 것: 규약 전체(특히 1 · 2 · 3 · 3.1 · 4 · 6 · 9 · 10 · 11절) → 기존 도구의 문체 `_공통/_도구/log_prompt.py` · `digest_session.py`(머리 독스트링 · 한글 주석 · `from __future__ import annotations`) → 참고만 할 원형 `Defense/z.tmp/clew-main/src/clew/frontmatter.py` · `lint.py` · `migrate.py`(Python 3.11 · ruamel.yaml 의존 — 코드를 옮겨 오지 말고 규칙만 참고).
- 실행 환경: 시스템 `python3`(3.9.6). 표준 라이브러리만 쓴다(PyYAML · ruamel 없음). 실행은 언제나 `python3 -I`. `-I` 는 스크립트 폴더를 `sys.path` 에 넣지 않는다 — `fm_migrate.py` 가 `fm_lint` 를 불러오려면 `sys.path.insert(0, str(Path(__file__).resolve().parent))`.

### 명세 — `fm_lint.py`

- `python3 -I fm_lint.py [--root DIR] [--strict] [--json] [--hook] <경로…>`. `--root` 기본값은 스크립트 위치의 `parents[2]`(Games 루트) — 시험은 `tests/fixtures/` 의 가짜 트리를 `--root` 로 준다. 경로는 루트 기준 상대나 절대, 파일이나 폴더(폴더면 아래 `.md` 전부). 규약 1절 예외는 건너뛴다(폴더 이름 정확히 일치 — `Defense.Logs` 는 예외가 아니다).
- **파서**는 규약 9절 부분 집합만 읽는다. 1행 `---` 와 닫는 `---` 사이 한 줄에 `키: 값`. 값은 맨 값 · 따옴표 값(`\"` · `\\` 풀기) · 목록 `[a, b]`(원소는 맨 값이나 따옴표 값). 9절 4번에 걸리는 맨 값 · 문법 위반 · 중복 키는 L18. 값은 전부 문자열로 다룬다(날짜 · 숫자로 바꾸지 않는다).
- **유일 범위**(L04 · L11): 파일이 속한 게임 작업 공간(루트 바로 아래 `Defense` · `AirShooter` · `RideShooter`) + `_공통` + 루트 `CLAUDE.md`. `_공통` · 루트 `CLAUDE.md` 의 문서는 세 게임 모두와 겹치면 안 된다. 범위 안 문서의 id 는 검사 대상 경로와 상관없이 범위 전체를 읽어 모은다(파일이 적어 1초 안이다).
- **규칙**은 규약 11절 표 그대로 — 심각도 · `--strict`(L01 을 오류로) · `_템플릿/` 아래 `{…}` 값 예외까지. 표에 없는 규칙을 더하지 않는다. 다음은 표의 뜻을 구체화한 것이다.
  - L06 의 「오늘」은 실행한 날의 로컬 날짜.
  - L07 과제 폴더: `<게임>/z.docs/<게임>.Planning/Pnn_*` 또는 `.../z.completed/Pnn_*`. 문서 경로의 조상에 `P\d\d_` 로 시작하는 폴더가 있으면 그 ID 와 같아야 한다. `work_report` 는 `work_unit` 필수.
  - L20 상대 링크: 본문(프론트매터 · 코드 펜스 ```` ``` ```` · `~~~` 밖)의 `](대상)` 에서 `http:` · `https:` · `mailto:` · `#…` · `/` 로 시작하는 것은 건너뛴다. `#앵커` 를 떼고 URL 디코딩해서 파일 위치 기준으로 푼다. doc_type `log` 와 `_템플릿/` 문서는 보지 않는다.
  - L21 날짜 접미: 파일 이름이 `_\d{8}` 를 담거나 `\d{8}_` 로 시작하는데 `lifecycle: living`.
  - L22: 파일 안에 `\\u` 뒤 한글 음절 범위(`AC00`~`D7A3`, 대소문자 무관) 네 자리.
  - L04 사본: 같은 id 가 두 파일 이상이면 바이트 비교 — 모두 같으면 통과(보고하지 않는다), 하나라도 다르면 오류. 값이 `{…}` 인 id 는 비교하지 않는다.
- **출력**: 기본은 사람이 읽는 줄(`경로:줄: L03 오류 — 한글 메시지`, 끝에 규칙별 건수 요약), `--json` 은 JSON 목록. 종료 코드 0 · 1(경고만) · 2(오류).
- **`--hook`**: 표준 입력의 JSON 에서 `tool_input.file_path` 하나만 본다. 입력을 못 읽음 · `.md` 아님 · 루트 밖 · 예외 경로면 아무것도 쓰지 않고 0. 검사는 `--strict` 판정 + L23(`updated` 가 오늘보다 이르면 경고 — 「본문을 고쳤으면 오늘로, 프론트매터만 고쳤으면 그대로」). 오류가 있으면 오류 · 경고를 표준 오류에 쓰고 **종료 코드 2**(Claude Code 가 표준 오류를 세션에 돌려준다). 경고만 있으면 표준 출력에 `{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "<경고 줄>"}}` 을 쓰고 0. 아무 문제 없으면 출력 없이 0. 이 규격은 리드가 S4 에서 실제로 확인한다 — 다르면 리드가 고친다.

### 명세 — `fm_migrate.py`

- `python3 -I fm_migrate.py [--root DIR] draft <경로…> --out <제안.json>`: 프론트매터가 없는 `.md` 마다 항목 하나 — `{"path": 루트 기준 경로, "fields": {...}, "block_from": 경로 또는 null, "note": ""}`. 이미 프론트매터가 있는 파일은 건너뛰고 수를 출력한다.
  - `doc_type` · `lifecycle`: 규약 3.1 표(위에서부터 처음 맞는 줄). 맞는 줄이 없으면 빈 문자열.
  - `created`: `git -C <그 파일의 저장소> log --follow --format=%ad --date=short -- <파일>` 의 마지막 줄(가장 이른 날). `updated`: 같은 명령의 첫 줄. git 밖이거나 이력이 없으면 파일 생성 시각(`st_birthtime`) · 수정 시각의 날짜.
  - `title`: 본문 첫 `# ` 줄의 글자(없으면 파일 이름에서 확장자를 떼고 `_` 를 공백으로).
  - `work_unit`: 경로의 조상 폴더가 `P\d\d_` 로 시작하면 그 ID. 아니면 넣지 않는다.
  - `id` · `summary` · `status` 는 빈 문자열 — 다음 단계에서 요약 에이전트가 채운다. 단, doc_type `log` 는 이행기가 전부 채운다: 프롬프트 로그는 id `<날짜>-prompts` · status `final` · summary `<YYYY-MM-DD> <게임> 작업 공간 세션들이 보낸 프롬프트 원문 <N>건(UserPromptSubmit 훅이 쓴다).`(N = `## ` 머리 수), 세션 다이제스트는 id `<날짜>-session-<세션8>` · status `final` · summary 는 본문의 `- 모델:` · `- 프롬프트 … · 도구 호출 …` 줄과 첫 사용자 프롬프트 앞부분으로 200자 안. 요약 문자열의 `{` `}` 는 `(` `)` 로 바꾸고 줄바꿈은 공백으로.
  - `block_from`: 이 파일의 프론트매터를 다른 파일에서 그대로 가져오는 경우. ① 정본 · 사본(규약 10절 표 — 사본 쪽 항목에 정본 경로. `<게임>.Planning/_템플릿/루트_CLAUDE.md` → `<게임>/CLAUDE.md` 는 게임 셋 모두) ② AirShooter · RideShooter 의 `_템플릿/` 골격 6개(`검토서.md` · `결정기록.md` · `계획서.md` · `과제_NOTES.md` · `과제_README.md` · `작업지시서.md`)는 `Defense/z.docs/Defense.Planning/_템플릿/<같은 이름>`(이미 골격 프론트매터가 있다). `block_from` 항목은 `fields` 를 비워 둔다.
- `python3 -I fm_migrate.py [--root DIR] apply <제안.json> [--dry-run]`:
  - 먼저 **전부 검사하고 하나라도 어긋나면 아무것도 쓰지 않는다**(Clew `--fill`). 검사 = 필수 필드가 비지 않음 + 블록을 붙인 결과를 `fm_lint` 규칙으로 검사해 오류 0. `block_from` 항목은 원본 파일의 블록(같은 실행에서 원본도 이행되면 그 새 블록)을 그대로 쓰고, 정본 · 사본이면 두 파일 본문 바이트가 같아야 한다.
  - 블록은 규약 2절 키 순서로 만들고, 9절 4번에 걸리는 값은 스스로 따옴표 · 이스케이프한다. 줄 끝은 LF, 블록 뒤에 원래 본문이 바로 이어진다(빈 줄을 더하지 않는다 — 원래 첫 줄이 H1 이면 `---` 다음 줄이 H1).
  - 쓰기: 원본 바이트를 읽고 → 같은 폴더 임시 파일(`.<이름>.fm-migrate.tmp`)에 `블록 + 원본` → 이름 바꾸기 직전에 원본을 다시 읽어 처음 읽은 바이트와 같은지 확인(다르면 그 파일은 멈추고 보고 — 다른 세션이 쓰는 중) → `os.replace`. 쓰고 난 파일에서 블록 뒤가 원본과 바이트까지 같은지 다시 본다.
  - `--dry-run` 은 쓰지 않고 검사 결과와 붙일 블록 표본을 출력한다.

### 금지

- 커밋 · `git add` · 브랜치 · stash 등 git 상태를 바꾸는 명령(읽기 `log` · `show` · `status` · `diff` 는 된다). 커밋은 리드만 한다.
- 수정 허용 영역 밖 파일 변경. 실제 문서에 `apply` 를 돌리는 것(임시 폴더 사본에서만).
- 규약을 고치는 것. 규약이 모호하거나 서로 어긋나 그대로 구현할 수 없으면 그 자리를 멈추고 보고한다 — 이것이 원하는 멈춤이다.
- 계획에 없는 기능(설정 파일 · 색인 · 자동 수정 · 색깔 출력 등)을 더하는 것. 더 나은 방법이 보이면 보고에 한 문장으로 적고 명세대로 만든다.
- 패키지 설치 · 네트워크 · 설정 파일(`settings.json` 등) 변경.

원하지 않는 멈춤: 구간이 끝났다고 보고하러 멈추기, 작업을 막지 않는 세부를 묻기. 명세 안의 세부는 스스로 정하고 보고에 적는다.

### 보고 형식

한글로, 결론부터 완전한 문장으로 쓴다.

1. 한 줄 결론(완료 / 부분 / 막힘)
2. 만든 파일과 줄 수
3. 검증 — 시험 명령과 출력 마지막 줄 · 기준선 규칙별 건수 · draft 표본 5개
4. 확인하지 않은 것 · 추정한 것
5. 규약에서 모호했던 곳과 스스로 정한 해석
6. 리드가 알아야 할 것(훅 출력 규격에 기댄 부분 · 시간이 오래 걸리는 부분 등)

---

## 오케스트레이터 메모 (프롬프트에 넣지 않는다)

- 받는 모델 opus(Opus 5.5) · `Agent` 도구(general-purpose) · 백그라운드. B2 와 동시.
- 검산: 시험을 리드가 다시 돌림 · 기준선 파일을 열어 규칙별 건수 확인 · draft 표본 5개를 원문과 대조 · `git -C _공통 status` 로 수정 허용 영역 밖 변경 없음 확인.
- 범위 크기는 리드가 커밋 뒤 `git diff --shortstat a28bbd1..HEAD` 로 — 세션 센서(R) 범위에 들어간다.
