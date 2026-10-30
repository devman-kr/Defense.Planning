---
id: 20261030-p02-s2b-log-hooks-tools
title: 작업지시서 — P02 · S2b · 로그 훅 · Planning 도구 프론트매터
summary: 서브에이전트 B2(opus)에게 로그 훅 `log_prompt.py` · `digest_session.py`(스크래치 사본에서)와 Planning `_도구/센서기록_추출.py` · `코드리뷰_집계.py` 가 만드는 마크다운에 문서규약 프론트매터를 쓰게 하는 일과 시험을 맡긴다.
doc_type: handoff
status: final
lifecycle: static
created: 2026-10-30
updated: 2026-10-30
work_unit: P02
implements: [20261030-p02-plan-frontmatter]
---

# 작업지시서 — P02 · S2b · 로그 훅 · Planning 도구 프론트매터

계획서 2절 분할표 S2b 행(B2)의 지시서다. 리드(주 세션 af266641)가 `Agent` 도구로 아래 본문을 넘긴다. S2a(B1 — `fm_lint.py` · `fm_migrate.py`)와 동시에 돈다.

---

## 프롬프트 본문 (여기부터 붙여 넣는다)

이 지시서는 Opus 5.5 기준으로 썼다(가이드 확인일 2026-10-30). 세션 모델이 다르면 보고 첫 줄에 알린다.

### 맡는 일

과제 P02(문서 프론트매터) · 분할표 S2b. 세 게임 작업 공간과 `_공통` 의 모든 마크다운은 YAML 프론트매터로 시작해야 한다 — 규약 `/Users/devman/_Projects/_Personal/Games/_공통/문서규약.md`(이하 규약). 사람 · 세션이 쓰는 문서는 템플릿과 검사기가 맡지만, **스크립트가 만드는 마크다운**은 스크립트가 처음부터 맞게 써야 한다(쓰는 순간 검사하는 훅은 `Write` · `Edit` 도구만 본다). 그런 스크립트가 넷이다 — 로그 훅 둘(세 게임의 프롬프트 로그 · 세션 다이제스트를 쓴다)과 Defense Planning 도구 둘(코드리뷰 센서 기록 · 집계). 이 넷이 규약의 프론트매터를 쓰게 고친다. 본문은 지금과 바이트까지 같게 둔다.

### 성공 기준

1. 로그 훅 두 스크립트의 고친 판이 스크래치 `/private/tmp/claude-501/-Users-devman--Projects--Personal-Games-Defense/af266641-28cb-4e0c-8761-a8ed2ac6f364/scratchpad/p02/b2/hooks/` 에 있다. 수동 모드로 임시 로그 폴더에 쓴 결과가 프론트매터로 시작하고, 프론트매터 뒤 본문이 지금 정본 스크립트의 결과와 바이트까지 같다(같은 입력으로 둘 다 돌려 대조).
2. Planning 도구 둘이 만드는 마크다운(`agent-<id>_final.md` · `agent-<id>_prompt.md` · `코드리뷰_집계.md`)이 프론트매터로 시작하고, 원문 본문은 한 글자도 바뀌지 않는다. 임시 출력 폴더로 실제 실행해 확인한다.
3. 만든 프론트매터가 규약 2절 필드 · 3절 어휘 · 9절 부분 집합(따옴표 · 이스케이프)에 맞는다. 프롬프트 원문처럼 사용자가 쓴 글을 값에 넣을 때 `: ` · ` #` · `"` · `\` · 줄바꿈 · `{` `}` 이 섞여도 맞다는 시험이 있다.
4. `python3 -I -m unittest discover -s /Users/devman/_Projects/_Personal/Games/_공통/_도구/tests -p 'test_log*.py'` 가 통과한다. 시험은 로그 훅 스크립트를 환경 변수 `FM_LOG_SCRIPTS_DIR`(기본 `_공통/_도구`)의 폴더에서 불러온다 — 지금은 스크래치 판을 가리켜 돌리고, 리드가 정본으로 바꿔 넣은 뒤 기본값으로 다시 돌린다.
5. 프론트매터를 만들다 예외가 나도 로그 본문은 지금처럼 써진다(로그가 끊기지 않는 것이 먼저).

### 위험 등급 · 되돌리는 법

중 — 로그 훅 정본(`_공통/_도구/log_prompt.py` · `digest_session.py`)은 세 게임 모든 세션의 훅이 바로 부른다. 그래서 정본은 고치지 않고 스크래치 사본에서 고치며, 리드가 시험 뒤 바꿔 넣는다. 되돌리기는 리드의 `git revert`.

### 승인 지점

없음. 아래 「금지」에 걸리는 일이 필요해 보이면 하지 말고 보고한다.

### 작업 위치

- Games 루트 `/Users/devman/_Projects/_Personal/Games`. 저장소 `_공통`(git, `main`, 시작 `a28bbd1`) · `Defense/z.docs/Defense.Planning`(git, `main`, 시작 `9c4e0b2`).
- **수정 허용 영역**: 스크래치 `p02/b2/` 아래(로그 훅 사본 `hooks/log_prompt.py` · `hooks/digest_session.py`, 시험용 임시 폴더) · `_공통/_도구/tests/test_log_frontmatter.py` · `_공통/_도구/tests/fixtures_log/` 아래 · `Defense/z.docs/Defense.Planning/_도구/센서기록_추출.py` · `Defense/z.docs/Defense.Planning/_도구/코드리뷰_집계.py`.
- **읽기 전용**: 그 밖 전부. 특히 `_공통/_도구/log_prompt.py` · `digest_session.py` 정본(사본을 스크래치에 복사해서 고친다) · 실제 로그 저장소 `*/z.docs/*.Logs/`(읽기만 — 수동 모드의 출력 폴더로 쓰지 않는다) · B1 의 파일(`fm_lint.py` · `fm_migrate.py` · `tests/test_fm_*.py` · `tests/fixtures/`).
- 시작 전에 읽을 것: 규약 2 · 3 · 4 · 6 · 9절 → 네 스크립트 전부(머리 주석이 쓰는 법이다) → `Defense/z.docs/Defense.Planning/코드리뷰_가이드.md` 8절(센서 기록 폴더 구조).
- 실행 환경: 시스템 `python3`(3.9.6), 표준 라이브러리만, 실행은 `python3 -I`(Planning 도구는 `python3 -X utf8 -I`). `-I` 는 스크립트 폴더를 `sys.path` 에 넣지 않으므로 **다른 모듈(`fm_lint` 등)을 import 하지 않는다** — 프론트매터를 쓰는 작은 함수를 각 스크립트에 둔다.

### 명세 — 무엇을 쓰나

| 파일 | `id` | `title` | `summary` | doc_type · status · lifecycle | 날짜 · work_unit |
|---|---|---|---|---|---|
| 프롬프트 로그 `prompts/YYYYMMDD.md` — 그날 파일을 **새로 만들 때만** 블록을 먼저 쓴다(이어 쓰기는 지금처럼) | `<YYYYMMDD>-prompts` | 지금의 H1 글자(`프롬프트 로그 — YYYY-MM-DD`) | `<YYYY-MM-DD> <게임> 작업 공간 세션들이 보낸 사용자 프롬프트 원문(UserPromptSubmit 훅이 쓴다).` — `<게임>` 은 로그 저장소 폴더 이름에서 `.Logs` 를 뗀 것 | `log` · `final` · `static` | created = updated = 그날. work_unit 없음 |
| 세션 다이제스트 `sessions/YYYYMMDD_<세션8>.md` — 매번 파일 전체를 다시 쓰므로 매번 블록부터 | `<YYYYMMDD>-session-<세션8>` | 지금의 H1 글자 | `세션 <세션8>(<모델>) — 프롬프트 N · 도구 호출 M · 변경 파일 K. 첫 프롬프트: <첫 사용자 프롬프트 첫 줄>` 를 200자 안으로 자른다 | `log` · 진행 중(Stop) `draft` · SessionEnd 뒤 `final` · `static` | created = 파일 이름의 날짜, updated = 쓰는 날. work_unit 없음 |
| 센서 원본 `agent-<id>_final.md` · `agent-<id>_prompt.md` | `<YYYYMMDD>-<pnn>-<세션 소문자>-<에이전트 id 앞 8자>-final` 또는 `-prompt` (slug 40자 안) — 날짜 · 과제 · 세션은 출력 폴더 경로 `…/Pnn_*/03_작업기록/코드리뷰_<YYYYMMDD>_<세션>/` 에서 | `코드리뷰 <세션> — 에이전트 <id8> 최종 보고 원문` / `… 지시 원문` | 역할 설명(meta description) · 모델 · 도구 호출 수를 담아 200자 안 | `review` · `final` · `static` | created = updated = 폴더 날짜, work_unit = 경로의 과제 ID. 경로에서 못 얻으면 실행일 · work_unit 생략 |
| `코드리뷰_집계.md`(Planning 루트, `--write`) | 이미 파일에 프론트매터가 있으면 그 `id` · `created` 를 이어 쓰고, 없으면 `<실행일>-review-aggregate` | `코드리뷰 집계` | 처리표를 모은 결과(과제 수 · 행 수)를 한 문장 | `register` · `final` · `living` | updated = 실행일. work_unit 없음 |

- 값 쓰기는 규약 9절 그대로 — 따옴표가 필요한 값(9절 4번)은 `"…"` 로 감싸고 `"` → `\"`, `\` → `\\`. 사용자 글에서 온 값은 줄바꿈 · 제어 문자를 공백으로, `{` `}` 를 `(` `)` 로 바꾼다(규약 L17 이 `{…}` 를 템플릿 자리표시로 본다). 한글은 그대로 쓴다.
- 블록 뒤에 본문이 바로 이어진다 — 지금 파일의 첫 줄(H1)이 `---` 다음 줄이 된다.
- 훅 스크립트의 지금 약속은 그대로다 — 표준 출력에 아무것도 쓰지 않는다, 실패해도 종료 0, 오류는 `hook_errors.log`. `digest_session.py` 의 SessionEnd 커밋 동작은 바꾸지 않는다.

### 금지

- `_공통/_도구/log_prompt.py` · `digest_session.py` 정본을 고치는 것(교체는 리드). 실제 로그 저장소를 수동 모드의 출력 폴더로 쓰는 것 — 반드시 스크래치 임시 폴더.
- 커밋 · `git add` 등 git 상태를 바꾸는 명령. 커밋은 리드만 한다.
- 수정 허용 영역 밖 파일 변경 · 규약 변경 · 설정 파일 변경 · 패키지 설치 · 네트워크.
- 계획에 없는 기능을 더하는 것(H-01 에 적힌 Planning 도구 견고성 손질 등 — 보이면 보고에만). 더 나은 방법이 보이면 보고에 한 문장으로 적고 명세대로 만든다.

원하는 멈춤: 규약대로 쓸 수 없는 값이 나올 때 · 본문 바이트를 지킬 수 없을 때 — 멈추고 보고한다. 원하지 않는 멈춤: 구간이 끝났다고 보고하러 멈추기, 작업을 막지 않는 세부를 묻기.

### 보고 형식

한글로, 결론부터 완전한 문장으로 쓴다.

1. 한 줄 결론(완료 / 부분 / 막힘)
2. 바꾼 파일(스크래치 사본 포함)과 바뀐 줄 수
3. 검증 — 시험 명령과 출력 마지막 줄 · 정본 대 고친 판 본문 대조 방법과 결과 · Planning 도구 실제 실행 결과 경로
4. 확인하지 않은 것 · 추정한 것
5. 규약에서 모호했던 곳과 스스로 정한 해석
6. 리드가 정본을 바꿔 넣을 때 할 일(복사할 파일 · 다시 돌릴 시험)

---

## 오케스트레이터 메모 (프롬프트에 넣지 않는다)

- 받는 모델 opus(Opus 5.5) · `Agent` 도구(general-purpose) · 백그라운드. B1 과 동시.
- 검산: 스크래치 판과 정본의 `diff` 를 리드가 읽는다 · 시험을 정본 경로로 다시 돌린다 · 고친 판 출력을 B1 의 `fm_lint.py` 로 검사한다 · `git -C Defense.Planning status` 로 `_도구/` 두 파일 밖 변경 없음 확인.
- 정본 교체는 다른 세션이 쉬는 틈에 `cp` 한 번 — 교체 직후 이 세션의 다음 턴 다이제스트가 새 판으로 써지는지 본다.
