# NOTES — P00 작업 메모

세션이 작업하면서 **다음 세션이 알아야 할 것**을 적는 곳이다. 과제 지도는 [`README.md`](README.md), 결정은 [`결정기록.md`](결정기록.md), 여러 과제에 걸치는 메모는 [`../NOTES.md`](../NOTES.md), 세 게임 공통은 `_공통/README.md`.

**쓰는 법**: 위 세 절은 덮어쓰기(세션 끝에 갱신), 아래 절은 누적(새 항목 위에). 한 줄에 하나, 근거(파일:줄 · 명령 · 실측)를 붙인다. 추정은 **[추정]**, 에이전트 보고를 옮긴 것은 **△**. 비밀값 금지.

---

## 다음 세션 시작 전 확인 (덮어쓰기)

_갱신: 2026-10-29 — 세션 2(Opus 5.5): Planning README 복원 · GitHub MCP 설정 · P01 등재. 사용자 결정 · 실행 대기_

1. **지금 어느 단계**: 검토 완료 — 결정 대기. 막는 것은 `_공통/README.md` 3절 Q-01~Q-05 와 4절 실행 요청 1~5(사용자 몫). GitHub MCP 는 **연결 확인 완료**(2026-10-29 세션 3 — `get_me` → `devman-kr`, 공개 저장소 3). 실행 요청 3 완료.
2. **답이 오면 할 일 순서**: Q 답을 `_공통` G-nn 으로 옮긴다 → `02_계획/계획서_YYYYMMDD.md`(스트림 B · D · E · F 분할 — 코드 없음, 위험 저) → B(템플릿 Unity 화)는 답과 무관하니 먼저 해도 된다 → D 는 Unity 설치 확인 뒤(`ls /Applications | grep -i unity`, Hub 의 6000.x 버전 기록) → F 는 Q-01 · Q-02 · gh 로그인 뒤.
3. **D 에서 쓸 템플릿**: `../_템플릿/Unity_CLAUDE.md`(저장소 `CLAUDE.md` 정본 초안) · `../_템플릿/Unity_README.md`(공개 README 초안) — `Defense.Unity` 를 만들 때 복사하고 「(설치 뒤)」 · 「(채움)」을 실측으로.
4. **착수 전 확인**: 훅 첫 자동 실행 — `../../Defense.Logs/prompts/` 에 오늘 파일, `sessions/` 에 이 세션 파일. 안 돌았으면 `Defense.Logs/README.md` 「수동 실행」으로 재현하고 「함정」에 적는다. 이 세션(2026-10-29)의 다이제스트는 수동으로 만들었다(`sessions/20261029_f4cc0549.md`). 작업 공간 `.claude/settings.json` 은 git 밖 — 사본은 `Defense.Logs/README.md`.

## 현재 상태 (덮어쓰기)

_갱신: 2026-10-29_

| 항목 | 상태 |
|---|---|
| 검토 | 검토서 2026-10-29 ✔ |
| 결정 | D-01~D-03 · 공통 G-01~G-09 · 미결 Q-01~Q-04(`_공통`) |
| 계획 | 미작성(Q 답 뒤) |
| 저장소 변경 | `Defense.Planning` `main` 첫 커밋 · `Defense.Logs` `main` 첫 커밋(해시는 작업색인) · 원격 없음 |
| 환경 | Unity · Blender · .NET SDK · gh 미설치. brew cask: unity-hub 3.22.4 · blender 5.2.3 · dotnet-sdk 10.0.402 확인 ✔ |
| 훅 | 2026-10-29 세션 2 에서 `UserPromptSubmit` 자동 실행 ✔(`../../Defense.Logs/prompts/20261029.md` 생성, 미커밋 — SessionEnd 훅 몫) |
| GitHub MCP | 작업 공간 루트 `.mcp.json`(git 밖) — 공식 원격 서버 `https://api.githubcopilot.com/mcp/`, 헤더 `Authorization: Bearer ${GITHUB_PAT}` · `X-MCP-Toolsets: context,repos,issues,pull_requests,actions`. `.claude/settings.json` 에 `enabledMcpjsonServers: ["github"]` · `permissions.deny` `delete_repository` · `permissions.ask` 24개(저장소 생성 · 포크 · 파일 쓰기/삭제 · 브랜치 · PR 생성/수정/머지/리뷰 · 이슈 · 하위 이슈 · 댓글 · 워크플로 실행). **연결 ✔ 2026-10-29** — `get_me` 로그인 `devman-kr`, `search_repositories user:devman-kr` 공개 3(`devman-kr.github.io` · `medieval_inn_simulator` · `vscode-gdd-framework-preview`). `gh auth status` 범위 `repo` · `workflow` · `read:org` · `gist` |

## 사용자 대기 (덮어쓰기)

- `_공통/README.md` Q-01~Q-05 · 실행 요청 1~5(3 에 `GITHUB_PAT` 추가).

---

## 함정 · 주의 (누적)

- GitHub MCP 도구 이름은 서버 판마다 바뀐다(2026-10-29 실측: `issue_write` · `sub_issue_write` · `actions_run_trigger` · `pull_request_review_write` · `delete_repository` 가 세션 2 의 예상 목록에 없었다). **서버를 다시 연결하거나 도구 목록이 바뀌면 쓰기 도구가 전부 `permissions.ask` · `deny` 에 있는지 다시 대조한다** — 빠진 도구는 확인 없이 원격에 쓴다.

- 이 세션(훅 설치 세션)은 상위 `Games/` 에서 열려 있어 Defense 의 훅이 돌지 않았다. 다음부터는 `Games/Defense/` 에서 연다.
- 2026-10-29 첫 골격은 루트 단일 `games.planning`(InvestBuddy 판 기반)이었고 사용자 지시로 게임별 분리 · EasyCheck 원본 기준으로 다시 만들었다(G-06). 옛 골격은 삭제했다 — 내용은 이 과제와 `_공통` 에 옮겼다.

## 발견 로그 (누적, 최신 위)

- 2026-10-29 — `Defense.Planning/README.md` 가 0바이트로 첫 커밋 `07e187b` 에 들어가 있었다(AirShooter · RideShooter 판은 11.6 KB). AirShooter 판에서 이름만 바꿔 복원하고 현황판 · 8절을 Defense 기준으로 고쳤다. ✔
- 2026-10-29 — GitHub MCP 는 OAuth 대신 PAT 헤더 방식으로 등록했다. 토큰은 파일에 쓰지 않고 `gh auth token`(키체인)을 환경 변수로 넘긴다 — gh 로그인 한 번으로 `gh` · MCP 가 같이 된다. [추정] VS Code 를 Dock 에서 열어도 로그인 셸 환경을 읽으므로 `~/.zshrc` 의 export 가 확장에 전달된다 — 연결 확인 때 검산.

- 2026-10-29 — Unity 공식 Claude Code 플러그인(2026-09-09 블로그 △): 스킬 29개 · `unity-cli` 로 열린 에디터 제어. 비용 · macOS 표기 없음 — D 에서 확인. 구 Unity MCP(AI Assistant 패키지)는 deprecated · AI 도구 체험 · 구독 필요 → 쓰지 않는다.
- 2026-10-29 — Blender Lab 공식 MCP v1.0.3(2026-09-11 △). 구 blender-mcp 는 개명 · CVE 보고(2차). 공식 것만.
- 2026-10-29 — EasyCheck 와 InvestBuddy 템플릿 대조: 7종 전부 다름(계획서 95줄 중 79줄), InvestBuddy 에만 세션 역할 셋 · 종결 검토 · 검산 · 보류작업 템플릿. ✔ → EasyCheck 원본으로 재구성(G-06).

## 미해결 (누적)

- Unity 6 정확한 버전은 설치 뒤.
- Supercent 스타일은 [추정](`_공통/조사/Supercent_스타일보드.md` 3절) — 캡처 뒤 확정(E).
