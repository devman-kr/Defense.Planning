---
id: 20261030-p02-s2-a8ad00a8-final
title: 코드리뷰 S2 — 에이전트 a8ad00a8 최종 보고 원문
summary: 「센서 R — S2 도구 코드 리뷰」 에이전트(claude-opus-5-5 · 도구 호출 60)가 돌려준 최종 보고 원문 — 출처 SubagentHandback.
doc_type: review
status: final
lifecycle: static
created: 2026-10-30
updated: 2026-10-30
work_unit: P02
---
| # | 종류 | 심각도 | 기원 | 유형 | 파일:줄 | 실패 시나리오(입력 → 잘못된 결과) | 확신 |
|---|---|---|---|---|---|---|---|
| 1 | question | important | new | 명세에서 벗어남(의도한 변경), 기대값도 같이 고침 | `_공통/_도구/fm_migrate.py:194-196` · `_공통/_도구/tests/test_fm_migrate.py:108-115` | 지시서 S2a 명세는 프롬프트 로그 summary 를 「… 프롬프트 원문 <N>건(…)」(N = `## ` 머리 수)으로 정했다. 리드가 이를 S2b 훅 문구(건수 없음)로 바꾸면서 시험 기대값도 새 문구로 고쳤다 → 시험이 지시서 명세가 아니라 바뀐 동작을 지킨다. 지난 날짜 파일은 더 이어 쓰이지 않아 N 이 고정이다(B1 베이스라인 draft 에 「4건」 · 「95건」이 있었다). 그런데 그 정보가 빠졌고, N 이 낡는 파일은 이행 당일 파일 하나뿐이다. 변경 근거는 `_공통` 커밋 5b193d2 메시지에만 있다. P02 결정기록 · NOTES(작업 트리 포함) · 지시서에는 없다 | confirmed |
| 2 | issue | nit | new | 정규식 끝 조건이 사용자 글과 겹침 | `_공통/_도구/fm_migrate.py:74` · `:164-170` | 첫 사용자 블록이 `- [ ] 할 일` · `- [링크](…)` 처럼 `- [` 로 시작하는 경우다. 도구 호출 줄(`- [HH:MM:SS]`)에서 끊으려고 둔 lookahead `^- \[` 가 블록 첫 줄에서 바로 맞는다 → 내용이 빈 블록이 되고 다음 프롬프트를 「첫 프롬프트」로 적는다(실험: 첫 프롬프트 `- [ ] 할 일 하나` → `'둘째 프롬프트'`). 훅은 같은 입력에 `- [ ] 할 일 하나` 를 쓴다. 지금 로그 17건에는 해당 없음 | confirmed |
| 3 | issue | nit | new | 블록 판정 — 첫 줄이 수평선 | `_공통/_도구/fm_lint.py:115-122` · `_공통/_도구/fm_migrate.py:230-232` | 프론트매터 없이 첫 줄이 수평선 `---` 이고 본문 뒤쪽에 `---` 가 한 번 더 있는 문서 → 블록으로 읽힌다. draft 는 「이미 프론트매터」로 세고 건너뛰어 이행에서 빠지고, 린트는 L01 대신 L02 · L18 오류를 낸다(실험 확인). 에이전트 보고 원문처럼 남이 쓴 글을 그대로 담은 기존 문서에서 나올 수 있다. 지금 실제 문서에는 해당 없음 | confirmed |
| 4 | issue | nit | new | 종료 코드 충돌 | `_공통/_도구/fm_lint.py:803-828` · `:405` | 읽을 수 없는 `.md`(PermissionError) 같은 예상 밖 예외 → 트레이스백과 함께 종료 1 이 나온다. 이 도구에서 1 은 「경고만」이다(실험: exit=1). S4 커밋 전 검사가 1 을 통과로 받으면, 검사가 끝나지 않았는데도 통과한다. 끊어진 심볼릭 링크 `x.md` 는 FileNotFoundError 로 잡혀 「경로가 없다」는 틀린 사유로 전체가 멈춘다(코드로 확인) | confirmed |
| 5 | issue | nit | new | 두 판정 함수 불일치(BOM) | `_공통/_도구/fm_lint.py:235-249`(독스트링 236) · 호출처 `_공통/_도구/fm_migrate.py:339` | BOM 이 있는 block_from 원본 → `parse_block` 은 BOM 을 떼고 블록을 찾지만 `split_block` 은 None 을 돌려준다(실험 확인). 그래서 apply 가 「block_from … 에 프론트매터가 없고 이번 이행에도 없다」는 틀린 사유로 멈춘다(쓰지는 않는다). 독스트링의 「판정은 parse_block 과 같다」와 다르다. `test_split_block_matches_parser`(test_fm_lint.py:419-422)는 BOM 을 다루지 않는다 | confirmed |
| 6 | issue | nit | new | 값 정리 누락 — 제어 문자 | `_공통/_도구/fm_migrate.py:108-110` · `:246-258` · `_공통/_도구/fm_lint.py:215-232` | H1 이나 세션 첫 프롬프트 첫 줄에 ESC(`\x1b[31m` — 붙여 넣은 터미널 출력) 같은 C0 제어 문자가 있는 경우다. `clean()` 은 공백류만 접고, `quote_if_needed` · `bare_problem` 은 제어 문자를 보지 않는다 → 맨 값으로 그대로 쓰이고 린트도 통과한다(실험: `title: a\x1b[31mred`, problems 빈 목록). YAML 명세는 C0 제어 문자를 허용하지 않는다. 로그 훅의 `fm_text` 는 같은 문자를 공백으로 바꾸므로 두 쓰기 경로가 다르다. 지금 문서 · 로그의 C0 제어 문자는 0건 | confirmed |
| 7 | issue | nit | new | 입력 검증 누락 | `_공통/_도구/fm_migrate.py:321` · `:330-338` | 손으로 고친 제안 JSON 의 `block_from` 이 문자열이 아닌 경우(목록 · 숫자) → `source in plan`(335) · `root / source`(338)에서 TypeError 트레이스백, 종료 1(실험 확인). 쓰기 전이라 문서는 안전하다. 다만 「항목 문제」 출력 · 종료 2 경로를 타지 않는다 | confirmed |
| 8 | issue | nit | new | 쓰이지 않는 코드 · 시험 자료가 남음 | `_공통/_도구/fm_migrate.py:73` · `_공통/_도구/tests/fixtures/games/Defense/z.docs/Defense.Logs/prompts/20261030.md:7` | 건수를 뺀 뒤 `PROMPT_HEAD_RE` 를 쓰는 곳이 없다(검색 0건). 픽스처의 「## 붙여 넣은 머리줄 — 프롬프트 수에 세지 않는다」를 보는 시험도 없다 → 다음 사람은 건수 기능이 아직 살아 있다고 읽는다 | confirmed |
| 9 | issue | nit | new | 같은 값을 만드는 두 구현이 다름 | `_공통/_도구/fm_migrate.py:164-183`(독스트링 174) · `_공통/_도구/digest_session.py:62` · `:70-71` · `:178-179` · `_공통/_도구/tests/test_fm_migrate.py:121` | 첫 프롬프트가 슬래시 명령이나 `<system-reminder>` 로 시작하는 경우다(실제 예: `Defense.Logs/sessions/20261030_de81874c.md` 의 `<command-name>/plugin</command-name>`). 이행기는 태그를 걷어 `/plugin` 을 쓰고, 훅은 `<command-name>/plugin</command-name>` · `<system-reminder>x</system-reminder>` 를 summary 에 그대로 쓴다(실험 확인). 「훅이 새 다이제스트에 쓰는 것과 같은 꼴」이라는 독스트링 · 시험 주석과 다르다 | confirmed |
| 10 | issue | nit | new | 길이 보정이 필드마다 다름 | `_공통/_도구/fm_migrate.py:154-161` | H1 이 120자를 넘는 문서 → summary 는 200자로 자르지만 title 은 자르지 않는다. 그래서 apply 가 L12 경고가 붙은 문서를 그대로 쓴다. 지금 Defense draft 82건에는 120자 넘는 제목이 없다 | confirmed |
| 11 | suggestion | nit | new | 성능 — 범위 전체를 메모리에 올림 | `_공통/_도구/fm_lint.py:421-437`(호출 `:535` · `:641`) · `:788` | `--hook` 은 id 가 있는 문서 하나를 볼 때도 유일 범위의 모든 `.md` 를 바이트 · 문자열 · 줄 목록으로 들고 있다. 계속 커지는 `*.Logs/sessions` 도 포함된다. 실측: 지금 Defense(md 3.4MB)는 0.13초 · 최대 RSS 약 40MB, 로그 48MB 가짜 트리는 0.15초 · 약 210MB. S4 부터 모든 md 쓰기마다 돌고, `_공통` 문서면 세 게임을 다 읽는다 → 로그가 쌓이면 쓰기마다 수백 MB 를 순간적으로 쓴다(16GB 기기, Unity 와 동시 실행). id 는 파일 앞부분 몇 KB 로 모으고, 같은 id 일 때만 전체 바이트를 비교하면 된다 | plausible |
| 12 | suggestion | nit | new | 정규식 처리 시간이 입력 길이의 제곱으로 늘어남 | `_공통/_도구/digest_session.py:62`(쓰는 곳 `:70` · `:178`) | 첫 프롬프트까지의 사용자 블록에 공백류가 수만 자 연속으로 있는 경우 → `\s*<browser_instruction>` 이 시작 위치마다 되짚는다. 실측: 2만 자 0.47초 · 4만 자 1.9초. 외삽하면 약 16만 자에서 Stop 훅 timeout 30초(Defense `settings.json`)를 넘겨 그 Stop 의 다이제스트를 못 쓴다. 정상 입력에서는 나오기 어렵다 | confirmed |
| 13 | suggestion | nit | new | 규약 대조 시험의 빈틈 | `_공통/_도구/fm_lint.py:65-66` · `:84-85` · `_공통/_도구/log_prompt.py:16-17`(같은 상수: `_공통/_도구/digest_session.py:26-27` · `Defense.Planning/_도구/센서기록_추출.py:39-40` · `Defense.Planning/_도구/코드리뷰_집계.py:34-35`) · `_공통/_도구/tests/test_fm_lint.py:507-553` | 9절 4번 목록(`YAML_INDICATORS` · `YAML_WORDS`, 쓰는 쪽 `FM_QUOTE_START` · `FM_QUOTE_WORDS` 4벌)과 1절 예외 폴더(`EXCLUDED_DIRS`)를 규약 파일과 대조하는 시험이 없다. Rulebook 시험은 2 · 3 · 8 · 11절만 보고, test_log_frontmatter 는 같은 목록을 손으로 다시 적었다 → 9절 · 1절을 고치면 검사기 · 훅 · Planning 도구가 소리 없이 어긋난다. 규약의 개정 안내(`_공통/문서규약.md:17`)도 3 · 8 · 11절과 fm_lint 상수만 말한다 | confirmed |
| 14 | question | nit | new | 규약 두 절의 우선순위 | `_공통/_도구/fm_lint.py:576-580` | `_공통/_템플릿/` 아래 골격에 `work_unit: "{Pnn}"` 이 있는 경우 → `_공통` 검사(6절)가 템플릿 예외(11절 끝 — `{…}` 필드는 L07 을 건너뜀)보다 먼저 돌아 L07 오류가 난다(실험 확인). 둘 중 어느 쪽이 우선인지 규약에 없다. 지금 `_공통/_템플릿/` 에는 `Games_CLAUDE.md` 하나뿐 | confirmed |
| 15 | thought | nit | new | 쓰기 경합 틈 | `_공통/_도구/fm_migrate.py:288-291` | 원본 다시 읽기(288)와 `os.replace`(291) 사이에 `log_prompt.py` 가 오늘 프롬프트 로그에 이어 쓰는 경우 → 그 프롬프트는 영구히 빠진다(이어 쓰기 파일이라서). 다이제스트의 Stop 재작성은 다음 Stop 까지만 빠진다. 틈은 짧다. 하지만 이행을 2026-10-30 에 하면 `prompts/20261030.md` 는 블록이 없는 채로 훅이 계속 이어 쓰는 파일이다 | plausible |
| 16 | thought | nit | new | 끝나도 draft 로 남는 상태값 | `_공통/_도구/digest_session.py:81` · `:256-257` | 세션이 SessionEnd 없이 끝난 경우(강제 종료 · 충돌) → 다이제스트가 `status: draft` 로 남고, 다른 세션의 SessionEnd `git add -A` 가 그대로 커밋한다. 이행기는 블록이 있는 파일을 건너뛰므로 고칠 경로가 없다 → 끝난 세션의 `draft` 로그가 쌓인다(7절의 「작성 중」과 뜻이 어긋난다) | plausible |
| 17 | thought | nit | new | 규약 9절 밖의 YAML 해석 차이 | `_공통/_도구/fm_lint.py:215-232` | 맨 값 `a\t#b`(탭 뒤 `#` 은 YAML 주석) · `a:\tb` · `12:30`(YAML 1.1 에서는 60진 정수) · `1e3`(YAML 1.2 에서는 실수)가 L18 없이 통과한다(앞의 둘은 실험으로 확인: `bare_problem` → None) → 9절 머리의 「이 안에서 쓰면 일반 YAML 파서도 같은 값으로 읽는다」가 맞지 않는 값이 있다. 이행기는 탭이 있으면 따옴표로 감싸 피하지만, 손으로 쓴 값은 막지 않는다 | plausible |

### 확인하지 않은 것 · 추정한 것

- 지시대로 unittest 시험 묶음은 돌리지 않았다. 통과 여부는 확인하지 않았다.
- 실험은 3e1d702 의 `fm_lint.py` · `fm_migrate.py` · `digest_session.py` 를 스크래치패드로 복사해 시스템 Python 3.9.6(`python3 -I -B`)으로 돌렸고, 끝난 뒤 지웠다. 실제 트리에서는 읽기 전용 실행만 했다: 측정용 `fm_lint.py --hook`(실제 지시서 하나)와, B1 의 e2e 사본(`scratchpad/p02/b1/e2e/games`)에 대한 린트. 두 저장소의 작업 트리는 바꾸지 않았다. Planning 쪽에 수정이 있는 P02 문서 둘은 원래부터 있던 것이다.
- YAML 쪽 해석은 실제 YAML 파서로 확인하지 않았다. 표준 라이브러리에 파서가 없어 YAML 명세 지식에 기댄 추정이다(탭+`#` 주석, `12:30` 60진, 제어 문자 거부, GitHub 이 프론트매터를 표로 그리는 동작).
- Claude Code PostToolUse 규격(종료 2 면 stderr 를 세션에 돌려준다, `additionalContext`)은 지시서 서술을 그대로 믿었다.
- #11 의 메모리 증가 전망은 이틀치 로그(`Defense.Logs/sessions` 2.3MB)와 가짜 48MB 트리 측정에서 외삽한 것이다. #12 의 30초 경계도 2만 · 4만 자 측정에서 외삽했다.
- `test_fm_migrate.py` 에서 리드가 고친 곳이 기대값 한 곳뿐인지는 대조하지 못했다. B1 원본이 남아 있지 않아, 커밋 메시지와 베이스라인 draft 의 「N건」으로만 확인했다.
- B2 보고의 「실제 전사 43개 · 129파일 본문 대조」는 다시 하지 않았다. 골든 파일 시험 1건을 코드로 읽은 것이 전부다.
- `digest()` 반환값이 셋으로 바뀐 데 대한 호출처는 `digest_session.py` 의 `main()` 과 `test_log_frontmatter.py` 뿐이었다(Games 전체 `.py` 검색). diff 에서 지워진 분기나 좁아진 조건은 찾지 못했다.
- `log_prompt.py` 와 Planning 도구 둘(`센서기록_추출.py` · `코드리뷰_집계.py`)은 끝 시점 파일을 전부 읽었다. 이들에서는 결함을 찾지 못했고, 실행해 보지는 않았다. `log_prompt.py` 에는 그날 첫 프롬프트가 동시에 두 번 들어오면 블록이 두 번 써지는 경합이 있는데, diff 전부터 있던 H1 중복 경합과 같은 것이라 표에 넣지 않았다.
- NFC 정규화로 문자열이 더 길어지는 문자(합성 제외 문자)가 L12 경계에 걸리는 경우 같은 극단은 따져 보지 않았다.