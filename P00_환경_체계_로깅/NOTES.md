# NOTES — P00 작업 메모

세션이 작업하면서 **다음 세션이 알아야 할 것**을 적는 곳이다. 과제 지도는 [`README.md`](README.md), 결정은 [`결정기록.md`](결정기록.md), 여러 과제에 걸치는 메모는 [`../NOTES.md`](../NOTES.md), 세 게임 공통은 `_공통/README.md`.

**쓰는 법**: 위 세 절은 덮어쓰기(세션 끝에 갱신), 아래 절은 누적(새 항목 위에). 한 줄에 하나, 근거(파일:줄 · 명령 · 실측)를 붙인다. 추정은 **[추정]**, 에이전트 보고를 옮긴 것은 **△**. 비밀값 금지.

---

## 다음 세션 시작 전 확인 (덮어쓰기)

_갱신: 2026-10-30 — 세션 4(Opus 5.5): 계획서 1차 → S1 템플릿 Unity 화 완료(`1fab994` · X-03)_

1. **지금 어느 단계**: 계획 — [`02_계획/계획서_20261030.md`](02_계획/계획서_20261030.md). 끝난 것(A 골격 · C 훅 · gh · GitHub MCP · Design · Unity 템플릿 초안)은 0절에 한 번 적고 다시 계획하지 않는다(사용자 2026-10-30).
2. **S1 완료**: 템플릿 · 가이드 · 도구가 Unity 판(Planning README 7절 X-03). 게이트 명령은 템플릿에 쓰지 않고 `Defense.Unity/CLAUDE.md` 「결정론 게이트」 한 곳 — **S2 에서 실측해 거기와 `_템플릿/Unity_CLAUDE.md` 에 같이 쓴다**. S4 는 이것으로 흡수(계획서 추기). 세션 센서 기록 `03_작업기록/코드리뷰_20261030_S1/`.
3. **사용자 답을 기다리는 것**: 계획서 7절 #1~#8(특히 #1 작성자 이메일 — 원격이 없는 지금이 가장 싸다, #2 E 를 P01 로 이관). 답이 오면 #1 은 `_공통` Q-06 으로, #2 는 D-04 로.
4. **설치 뒤**: S2 D1 은 실행 요청 1(Unity) · 4(.NET — 이제 권장) 뒤, S3 D2 는 실행 요청 2(Blender) 뒤이고 **S2 와 같은 시간에 하지 않는다**(G-01). 설치 확인은 `ls /Applications/Unity/Hub/Editor` · `ls /Applications/Blender.app` · `dotnet --version`.
5. **R1**: 이 세션이 끝난 뒤 `git -C z.docs/Defense.Logs log -1` 에 새 `chore: 세션 로그` 커밋이 있는지(작업 공간 루트에서). 10-29 16:08 `7c6c0cd` 뒤로 훅 커밋이 없고 미커밋 변경 3건이 남아 있다(2026-10-30 실측).

## 현재 상태 (덮어쓰기)

_갱신: 2026-10-30_

| 항목 | 상태 |
|---|---|
| 검토 | 검토서 2026-10-29 ✔ |
| 결정 | D-01~D-03 · 공통 G-01~G-10 · 미결 `_공통` Q-01~Q-05 · 이 과제 계획서 7절 #1~#8 |
| 계획 | 계획서 1차 2026-10-30 — S1 B1 · S2 D1 · S3 D2 · S4 B2 · F0 · S5 F · R1 |
| 저장소 변경 | `Defense.Planning` · `Defense.Design` · `Defense.Logs` · `_공통` 모두 `main` 로컬, 원격 없음. 커밋 작성자 이메일이 전부 noreply 아님(계획서 1절 #9) |
| 환경 | 2026-10-30 실측: Unity · Unity Hub · Blender · .NET SDK · `csharp-ls` · git-lfs · git-filter-repo 없음. gh ✔ `devman-kr`. `brew list --cask` 비어 있음. 디스크 여유 333 GiB |
| Claude Code 플러그인 | 설치됨 `session-report` · `microsoft-docs` · `csharp-lsp`(.NET SDK 없어 미동작). Unity 플러그인 `unity@claude-plugins-official` 은 카탈로그에만 |
| 훅 | 프롬프트 · 다이제스트 동작 ✔. `SessionEnd` 커밋은 1회(`7c6c0cd`)만 확인 → R1 |
| GitHub MCP | 작업 공간 루트 `.mcp.json`(git 밖) — 공식 원격 서버 `https://api.githubcopilot.com/mcp/`, 헤더 `Authorization: Bearer ${GITHUB_PAT}` · `X-MCP-Toolsets: context,repos,issues,pull_requests,actions`. `.claude/settings.json` 에 `enabledMcpjsonServers: ["github"]` · `permissions.deny` `delete_repository` · `permissions.ask` 24개(저장소 생성 · 포크 · 파일 쓰기/삭제 · 브랜치 · PR 생성/수정/머지/리뷰 · 이슈 · 하위 이슈 · 댓글 · 워크플로 실행). **연결 ✔ 2026-10-29** — `get_me` 로그인 `devman-kr`. `gh auth status` 범위 `repo` · `workflow` · `read:org` · `gist` |

## 사용자 대기 (덮어쓰기)

- 계획서 7절 #1~#8 — 작성자 이메일 · E 이관 · 번들 ID · 라이선스 · Blender 형식 · S2 센서 · LFS · .NET.
- `_공통` 실행 요청 1(Unity) · 2(Blender) · 4(.NET — 「권장」으로 올림) · Q-01~Q-03(S5 선행).

---

## 함정 · 주의 (누적)

- GitHub MCP 도구 이름은 서버 판마다 바뀐다(2026-10-29 실측: `issue_write` · `sub_issue_write` · `actions_run_trigger` · `pull_request_review_write` · `delete_repository` 가 세션 2 의 예상 목록에 없었다). **서버를 다시 연결하거나 도구 목록이 바뀌면 쓰기 도구가 전부 `permissions.ask` · `deny` 에 있는지 다시 대조한다** — 빠진 도구는 확인 없이 원격에 쓴다.

- 이 세션(훅 설치 세션)은 상위 `Games/` 에서 열려 있어 Defense 의 훅이 돌지 않았다. 다음부터는 `Games/Defense/` 에서 연다.
- 2026-10-29 첫 골격은 루트 단일 `games.planning`(InvestBuddy 판 기반)이었고 사용자 지시로 게임별 분리 · EasyCheck 원본 기준으로 다시 만들었다(G-06). 옛 골격은 삭제했다 — 내용은 이 과제와 `_공통` 에 옮겼다.

## 발견 로그 (누적, 최신 위)

- 2026-10-30 — S1 세션 센서(sonnet, 2라운드): 지적 11 · 고침 7 · 범위 밖 3 → H-01 · 미해결 0. 폴더 `03_작업기록/코드리뷰_20261030_S1/`. 1라운드 고침이 2라운드에서 회귀(점이 든 일반 단어를 파일로)를 만들었다 — 확장자 목록을 없애는 쪽보다 목록 + 경계 정규식이 맞았고, 실제 처리표 430칸 비교가 합성 사례보다 회귀를 잘 잡았다. ✔
- 2026-10-30 — 커밋 작성자 이메일이 네 저장소 전부 noreply 가 아닌 한 주소다(`git log --format=%ae` 종류 1 · `noreply` 일치 0 — 값은 출력하지 않음). 공개 GitHub 에서는 모든 커밋에 드러난다. 바꾸려면 원격이 없는 지금 이력 재작성(커밋 26 · 문서 해시 참조 34줄) → 계획서 7절 #1. ✔
- 2026-10-30 — 설치된 `csharp-lsp` 플러그인은 .NET SDK 6+ 와 `csharp-ls` 를 요구한다(`~/.claude/plugins/cache/claude-plugins-official/csharp-lsp/1.0.0/README.md`). 지금은 C# 진단이 돌지 않는다 → 실행 요청 4 를 「권장」으로. ✔
- 2026-10-30 — Unity 공식 플러그인은 `unity@claude-plugins-official`(원본 `github.com/Unity-Technologies/unity-agent-plugin`) — 스킬에 `unity-cli` · `new-unity-project` 포함, 상시 컨텍스트 약 5.9K 토큰(`~/.claude/plugins/plugin-catalog-cache.json` 수치). 비용 · 계정 요구는 S2 에서 확인. ✔(카탈로그) · △(동작)
- 2026-10-30 — `_도구/코드리뷰_집계.py:26` 의 `AREAS` 가 EasyCheck 영역 코드 10개(`AUTH` · `AUTHZ` · `LIMIT` …)로 고정돼 있다 — 가이드 부록 A 를 바꾸면 같이 바꿔야 집계가 맞다 → S1. ✔

- 2026-10-29 — `Defense.Planning/README.md` 가 0바이트로 첫 커밋 `07e187b` 에 들어가 있었다(AirShooter · RideShooter 판은 11.6 KB). AirShooter 판에서 이름만 바꿔 복원하고 현황판 · 8절을 Defense 기준으로 고쳤다. ✔
- 2026-10-29 — GitHub MCP 는 OAuth 대신 PAT 헤더 방식으로 등록했다. 토큰은 파일에 쓰지 않고 `gh auth token`(키체인)을 환경 변수로 넘긴다 — gh 로그인 한 번으로 `gh` · MCP 가 같이 된다. [추정] VS Code 를 Dock 에서 열어도 로그인 셸 환경을 읽으므로 `~/.zshrc` 의 export 가 확장에 전달된다 — 연결 확인 때 검산.

- 2026-10-29 — Unity 공식 Claude Code 플러그인(2026-09-09 블로그 △): 스킬 29개 · `unity-cli` 로 열린 에디터 제어. 비용 · macOS 표기 없음 — D 에서 확인. 구 Unity MCP(AI Assistant 패키지)는 deprecated · AI 도구 체험 · 구독 필요 → 쓰지 않는다.
- 2026-10-29 — Blender Lab 공식 MCP v1.0.3(2026-09-11 △). 구 blender-mcp 는 개명 · CVE 보고(2차). 공식 것만.
- 2026-10-29 — EasyCheck 와 InvestBuddy 템플릿 대조: 7종 전부 다름(계획서 95줄 중 79줄), InvestBuddy 에만 세션 역할 셋 · 종결 검토 · 검산 · 보류작업 템플릿. ✔ → EasyCheck 원본으로 재구성(G-06).

## 미해결 (누적)

- Unity 6 정확한 버전은 설치 뒤.
- Supercent 스타일은 [추정](`_공통/조사/Supercent_스타일보드.md` 3절) — 캡처 뒤 확정(E).
