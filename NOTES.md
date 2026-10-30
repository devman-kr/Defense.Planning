---
id: 20261029-planning-notes
title: NOTES — 과제 공통 작업 메모
summary: 여러 과제에 걸치는 세션 인계 메모로, 세션 10 기준 다음 세션 확인 9개(P00 남은 일 · P01 설계 확정 · P02 프론트매터 끝남)와 환경 상태 표, 사용자 대기 Q-01~Q-05 · F0 해시, 누적 함정 · 발견 로그 · 미해결을 담는다.
doc_type: note
status: final
lifecycle: living
created: 2026-10-29
updated: 2026-10-31
---
# NOTES — 과제 공통 작업 메모

세션이 작업하면서 **다음 세션이 알아야 할 것**을 적는 곳이다. 과제 하나에만 해당하는 것은 그 과제의 `NOTES.md` 에, 여러 과제나 저장소 전체에 걸치는 것은 여기에 적는다. 세 게임 전체에 걸치는 것은 `../../../_공통/README.md`. 폴더 구조와 규칙은 [`README.md`](README.md).

**쓰는 법**
- 위 세 절(「다음 세션 시작 전 확인」 · 「현재 환경 상태」 · 「사용자 대기」)은 **덮어써서 항상 최신**으로 둔다. 세션을 끝낼 때 갱신한다.
- 아래 절(「함정 · 주의」 · 「발견 로그」 · 「미해결」)은 **누적**한다. 발견 로그는 새 항목을 위에 쓴다.
- 한 줄에 하나. 근거(파일:줄 · 명령 · 실측)를 붙인다. 추정이면 **[추정]**, 에이전트 보고를 옮긴 것은 **△**.
- 비밀값은 쓰지 않는다.

---

## 다음 세션 시작 전 확인 (덮어쓰기)

_갱신: 2026-10-31 — 세션 10(Opus 5.5): P00 종결(F0 작성자 재작성 · 첫 푸시 전 비밀값 검사 · S5 GitHub). 그 전: P02 문서 프론트매터 종결(2026-10-31) · 세션 10 잔여 정리(2026-10-30) · 세션 9: `_공통` G-12 · 세션 7: P00 S2 `Defense.Unity` 생성_

1. 열린 과제는 P01 — `P01_게임설계_코어/NOTES.md` 「다음 세션 시작 전 확인」부터. P00 · P02 는 종결(`z.completed/`).
2. **P00 종결(2026-10-31)** — 계획서 완료 기준 9 전부 ✔. 원격은 공개 GitHub `https://github.com/devman-kr/`(`games-common` · `Defense.Unity` · `Defense.Planning` · `Defense.Design` · `Defense.Logs` — `main` 보호: 강제 푸시 · 삭제 금지). **푸시는 사용자 허락 뒤** — 명령은 `z.completed/P00_환경_체계_로깅/NOTES.md` 「현재 상태」 GitHub 저장소 행(전역 git 에 GitHub 인증 도우미가 없다). 다른 두 게임 P00 은 같은 NOTES 2번 복사 목록부터. 결정론 게이트 명령은 `../../Defense.Unity/CLAUDE.md` 「결정론 게이트」(에디터 닫힘 `unity test` · `unity build` / 열림 `unity command`). **Unity 에디터는 세션이 연다**(`_공통` G-12 — 사용자에게 열어 달라 하지 않는다).
3. P01 은 설계 확정 — 기획 정본은 `../Defense.Design/기획서.md`. 게임 기획 · 특징은 Design 에만 적고 `CLAUDE.md` 에는 적지 않는다(`_공통` G-10, 세 게임 공통). P00 B · D 가 끝나 **계획서 2차를 쓸 수 있다** — 다음 일은 `P01_게임설계_코어/NOTES.md` 「다음 세션」.
4. 훅: 프롬프트 · 다이제스트 · `SessionEnd` 커밋 모두 ✔(Logs `99e4e35` 등 2026-10-30 — P00 R1 닫음).
5. GitHub MCP: 연결 ✔(2026-10-29, `devman-kr`). 도구 목록이 바뀌면 권한 대조(`z.completed/P00_환경_체계_로깅/NOTES.md` 「함정」).
6. 작업 공간 루트 `NOTES.md`(git 밖, 2026-10-30~) — 사용자와 정한 다음 할 일 메모. 지금은 목업 제작 템플릿 하나.
7. 같은 Planning 에서 세션 여럿이 동시에 돈다(2026-10-30 — 코딩 표준 세션 · S2 세션). 편집 전 `git status` 와 다른 세션 전사 수정 시각을 보고, 결정 번호는 예약된 것(코딩 표준 D-06 · D-07)을 건너뛴다.
8. NRE 조기 감지 체계 X-04(README 7절, 2026-10-30 세션 8) — 구현은 P01 `DEF-M01`, 계획서 2차에 넣는다(`P01_게임설계_코어/NOTES.md` 4번).
9. **P02 문서 프론트매터(G-18) 끝남**(2026-10-31 종결, 세션 af266641 — 기록 `z.completed/P02_문서_프론트매터/`). 새 마크다운은 `../../../_공통/문서규약.md`(1.2)의 프론트매터로 시작한다 — 쓰는 순간 PostToolUse 훅이 검사해 돌려주고, 커밋 전에는 `fm_lint.py --strict` 오류 0(루트 `CLAUDE.md` 세션 종료 5번). P00 이 넘겨받아 처리했다(2026-10-31 — GitHub 의 프론트매터 표 렌더 확인 ✔).

## 현재 환경 상태 (덮어쓰기)

_갱신: 2026-10-31_

| 항목 | 상태 |
|---|---|
| 저장소 | `Defense.Planning` · `Defense.Design`(X-02 → G-10) · `Defense.Logs` · **`Defense.Unity`(2026-10-30 신설 — Unity 6000.3.27f1 · URP 17.3)** 모두 `main` — 2026-10-31 공개 GitHub `devman-kr` 에 첫 푸시 · `main` 보호(`_공통` 은 `games-common`) |
| 도구 | Unity Hub 3.22.5 · Unity **6000.3.27f1 LTS**(arm64) + Android(OpenJDK 17 · SDK · NDK r27c) · WebGL · Blender 5.2.3 LTS · .NET SDK 10.0.403 · `csharp-ls` 0.28.0(PATH ✔) · Unity CLI 1.0.0-beta.13(`~/.unity/bin`) · Claude Code `unity` 플러그인 0.1.6-beta · Chrome · Xcode 26.6 · Node 24.21 · Python 3.9.6 · uv · Homebrew · gh · git-filter-repo 2.47.0(2026-10-30 실측) |
| 훅 | `.claude/settings.json` 등록 완료(G-05). 프롬프트 · 다이제스트 · `SessionEnd` 커밋 ✔ · 문서 검사(`PostToolUse`, G-18 — 2026-10-31) ✔ |
| MCP | `.mcp.json` GitHub(공식 원격) 연결 ✔ 2026-10-29 — 계정 `devman-kr`. 쓰기 도구 `permissions.ask` 24 · 저장소 삭제 `deny` |

## 사용자 대기 (덮어쓰기)

- `_공통/README.md` 3절 Q-04 · Q-05(Q-01~Q-03 은 2026-10-30 G-13~G-15 로 해소).
- P01 계획서 1차 · 지시서 S1 승인.

---

## 함정 · 주의 (누적)

- 훅은 세션 시작 때 읽힌다. 훅을 고친 뒤에는 세션을 새로 연다. 세션은 이 작업 공간 루트(`~/_Projects/_Personal/Games/Defense`)에서 연다 — 상위 `Games/` 나 하위 저장소에서 열면 훅 · 루트 `CLAUDE.md` 가 맞지 않는다.
- `UserPromptSubmit` 훅의 stdout 은 대화 컨텍스트에 들어간다. 로그 스크립트는 아무것도 출력하지 않는다.
- Unity Asset Store 「무료」 에셋은 CC0 가 아니다(EULA 재배포 금지). 공개 저장소에 올릴 수 없다.

## 발견 로그 (누적, 최신 위)

- 2026-10-31 — GitHub 은 마크다운 맨 앞 YAML 프론트매터를 표로 그린다(Planning README 렌더 HTML 의 첫 `<table>`) — 공개 첫 화면 `*.Unity/README.md` 를 예외로 둔 `_공통/문서규약.md` 1절이 맞았다. ✔
- 2026-10-29 — Claude Code 전사의 thinking 블록은 세션당 0~4K자(Fable · Opus 4세션 실측). 사고 과정은 전사로 복원할 수 없다 → G-05 보완 규칙. ✔

## 미해결 (누적)

- ~~Unity 6 정확한 버전(6000.x LTS)은 설치 뒤 기록.~~ → 6000.3.27f1 LTS(2026-10-30, `_공통` G-01 비고).
