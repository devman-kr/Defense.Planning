# NOTES — P00 작업 메모

세션이 작업하면서 **다음 세션이 알아야 할 것**을 적는 곳이다. 과제 지도는 [`README.md`](README.md), 결정은 [`결정기록.md`](결정기록.md), 여러 과제에 걸치는 메모는 [`../NOTES.md`](../NOTES.md), 세 게임 공통은 `_공통/README.md`.

**쓰는 법**: 위 세 절은 덮어쓰기(세션 끝에 갱신), 아래 절은 누적(새 항목 위에). 한 줄에 하나, 근거(파일:줄 · 명령 · 실측)를 붙인다. 추정은 **[추정]**, 에이전트 보고를 옮긴 것은 **△**. 비밀값 금지.

---

## 다음 세션 시작 전 확인 (덮어쓰기)

_갱신: 2026-10-30 — 세션 6(Fable 5.1): 코딩 표준 D-06 · D-07 · 계획서 S1b(실행) · S1c(승인 대기). 그 전 세션 7(Opus 5.5): S2 D1 `Defense.Unity` 생성 · 게이트 실측 · 빌드 스모크_

1. **지금 어느 단계**: 실행 — [`02_계획/계획서_20261030.md`](02_계획/계획서_20261030.md). S1 ✔ · **S2 ✔(2026-10-30)** · S4 는 S1 · S2 로 흡수 끝(`_템플릿/Unity_CLAUDE.md` = `Defense.Unity/CLAUDE.md`, diff 0). R1 ✔. 남은 것: S3 D2 Blender MCP · 코딩 표준(6번) · F0 · S5 F(`_공통` Q-01~Q-03 뒤).
2. **S2 결과**: `Defense.Unity`(로컬 `main`, 원격 없음) — `e46ecab` 템플릿 생성물 그대로 · `3d4abc4` 골격(CLAUDE.md · README · ASSETS · LICENSE MIT · `.gitattributes` · Core/Tests asmdef · 스모크 테스트 1 · `com.unity.pipeline` · PlayerSettings · 빌드 프로필 2) · `4ec4f97` · `4fdea24` 빌드 때 에디터 자동 변환 · `a89d77b` 작업 보고 · `59f9a07` 센서 지적 고침 · `4dfe06d` 보고 코드 리뷰 절. 게이트 명령은 `Defense.Unity/CLAUDE.md` 「결정론 게이트」 — 에디터 닫힘 `unity test` 약 20초 · 열림 `unity command` 0.3초. 빌드 장부 `z.builds/BUILDS.md`(Android 개발 APK 42.7 MB · WebGL 14 MB). 작업 보고 `Defense.Unity/z.docs/work_reports/20261030/1_create_저장소_골격.md`. 센서 기록 [`03_작업기록/코드리뷰_20261030_S2/`](03_작업기록/코드리뷰_20261030_S2/).
3. **에디터를 누가 여나**: 이번 세션은 사용자 말(「unity cli 로 당신이 진행하면 될 것 같은데요」)대로 세션이 창 없는 에디터를 직접 띄워 `unity command` 로 다뤘다(D-08). 루트 `CLAUDE.md` · `_공통` 상위 `CLAUDE.md` 는 아직 「에디터는 사용자가 연다」 — 규칙으로 올릴지는 사용자 대기.
4. **다음 세션이 확인할 것**: ① Claude Code `csharp-lsp` 가 `Defense.Unity` 의 `.cs` 에서 정의 이동 · 호버가 되는지 — 이 세션의 LSP 는 프로젝트가 생기기 전에 떠서 문서 심볼만 됐다(`csharp-ls --diagnose` 는 `Defense.Unity.slnx` 로드 ✔) ② Unity 플러그인 상시 컨텍스트 비용(`/context`) — 세션이 볼 수 없어 사용자가 보면 적는다.
5. **결정 끝(2026-10-30)**: G-11(커밋 이메일 noreply — `Defense.Unity` 도 로컬 설정 ✔) · D-04 · D-05 · D-08(S2 실행 세부).
6. **C# 코딩 표준 사본**: 사용자 요청(2026-10-30)으로 EasyCheck.Server `z.docs/dev/csharp_coding_standards.md`(EasyCheck 커밋 `eb7628e6`, `CLAUDE.md:95` 가 가리키는 현행 판)를 **그대로** [`../_템플릿/Unity_csharp_coding_standards.md`](../_템플릿/Unity_csharp_coding_standards.md) 에 두었다(SHA-256 일치 ✔). Unity 화(ASP.NET · DB · `[Developer]` · `>>`/`<<` 로깅 · INI 등 서버 전용 절 정리, `_템플릿/Unity_CLAUDE.md` 「코딩」과 대조)는 **아직 안 했다** — 사용자 「우선 가져오기만」. 자리는 S2 D1 7번 「우리 파일」에 `z.docs/dev/csharp_coding_standards.md` 로 넣는다. 예제가 든 긴 판(32 KB)은 EasyCheck `z.docs/z.old/csharp_coding_standards.md` 에 있다. **검토서 ✔ 2026-10-30** [`01_검토/검토서_20261030_코딩표준.md`](01_검토/검토서_20261030_코딩표준.md) — 절별 처리(유지 2 · 수정 13 · 교체 9 · 신설 7)와 6절 결정 14개(묶음 A 7 · 취향 B 7). **결정 ✔ D-06(묶음 A) · D-07(B)** 2026-10-30 → 계획서 **S1b B1b**(4절) — 사용자 계획 승인 뒤 실행: 표준 덮어쓰기 · `.editorconfig` 템플릿 · 템플릿 「코딩」 분담 · S2 D1 7번 · 센서. S2 는 끝났다(`c543eeb` · Unity `4dfe06d`) — `Defense.Unity` 반영은 **S1c**(사본 2 · `CLAUDE.md` · asmdef `Defense.Core` → `Devman.Core` 개명 · 게이트, 승인 지점). 네임스페이스는 `Devman.Core.*` / `Defense.Game.*`(D-07 ⑤) — 웨이브 디렉터 · 드래프트의 소속은 P01 `DEF-M01` 에서.

## 현재 상태 (덮어쓰기)

_갱신: 2026-10-30_

| 항목 | 상태 |
|---|---|
| 검토 | 검토서 2026-10-29 ✔ · 코딩 표준 검토서 2026-10-30 ✔(결정 끝 D-06 · D-07) |
| 결정 | D-01~D-05 · D-08 · 공통 G-01~G-11 · 미결 `_공통` Q-01~Q-05 · 코딩 표준 D-06 · D-07 ✔ |
| 계획 | 계획서 1차 2026-10-30 — S1 ✔ · S2 ✔ · S4 흡수 ✔ · R1 ✔ · 남은 S1b(코딩 표준, 실행) · S1c · S3 D2 · F0 · S5 F |
| 저장소 변경 | `Defense.Unity`(2026-10-30 신설) · `Defense.Planning` · `Defense.Design` · `Defense.Logs` · `_공통` 모두 `main` 로컬, 원격 없음. `Defense.Unity` 는 처음부터 noreply 작성자, 나머지는 기존 커밋이 noreply 아님(F0) |
| 환경 | Unity Hub 3.22.5 · Unity **6000.3.27f1 LTS**(arm64) + Android(OpenJDK 17 · SDK · NDK r27c · build-tools 36) · WebGL · Blender 5.2.3 LTS · .NET SDK 10.0.403 · `csharp-ls` 0.28.0(PATH ✔) · Unity CLI 1.0.0-beta.13(`~/.unity/bin`, 로그인 · 라이선스 Personal 활성) · Chrome(헤드리스 캡처) · gh ✔ `devman-kr`. 없음: git-lfs(D-05) · git-filter-repo(F0 때) |
| Claude Code 플러그인 | `unity@claude-plugins-official` 0.1.6-beta ✔(스킬 `unity-cli` 외) · `csharp-lsp`(`csharp-ls` 0.28.0 — 4번 ①) · `session-report` · `microsoft-docs` |
| `Defense.Unity` 패키지 | 템플릿 기본 + `com.unity.pipeline` 0.9.1-exp.1(Unity 레지스트리 · 실험판 · `unity command` 용 — 플레이어 빌드에 런타임 미포함 확인) |
| 훅 | 프롬프트 · 다이제스트 · `SessionEnd` 커밋 동작 ✔(Logs `99e4e35` 등 2026-10-30 — R1 닫음) |
| GitHub MCP | 작업 공간 루트 `.mcp.json`(git 밖) — 공식 원격 서버 `https://api.githubcopilot.com/mcp/`, 헤더 `Authorization: Bearer ${GITHUB_PAT}` · `X-MCP-Toolsets: context,repos,issues,pull_requests,actions`. `.claude/settings.json` 에 `enabledMcpjsonServers: ["github"]` · `permissions.deny` `delete_repository` · `permissions.ask` 24개(저장소 생성 · 포크 · 파일 쓰기/삭제 · 브랜치 · PR 생성/수정/머지/리뷰 · 이슈 · 하위 이슈 · 댓글 · 워크플로 실행). **연결 ✔ 2026-10-29** — `get_me` 로그인 `devman-kr`. `gh auth status` 범위 `repo` · `workflow` · `read:org` · `gist` |

## 사용자 대기 (덮어쓰기)

- **S1c 계획 승인** — `Defense.Unity` 반영(계획서 4절 S1c): 사본 2 · `CLAUDE.md` 「코딩」 · asmdef `Defense.Core` → `Devman.Core` · 게이트. S1b 보고 뒤 저장소 규칙 형식으로 제시한다. 결정은 끝(D-06 · D-07, 2026-10-30).
- **에디터를 여는 주체** — 루트 `CLAUDE.md` 「공유 자원」 · `_공통` 상위 `CLAUDE.md` 「한 기기」의 「Unity 에디터는 사용자가 연다」를 「세션이 Unity CLI 로 창 없는 에디터를 띄워도 된다(Blender 와 동시 금지는 그대로)」로 바꿀지(D-08 은 이 세션 한정). 바꾸면 `_공통` G-nn 과 두 정본(`_공통/_템플릿/Games_CLAUDE.md` · `_템플릿/루트_CLAUDE.md`).
- `Defense.Unity` 실기기 설치(선택) — `z.builds/debug/defense_20261030_3d4abc4_android-dev.apk`.
- `_공통` Q-01~Q-03(S5 선행).

---

## 함정 · 주의 (누적)

- **`unity command` 의 전역 옵션은 `command` 앞에** — `unity command … --no-banner editor status` 처럼 뒤에 두면 `--no-banner` 가 다음 낱말을 값으로 먹어 `status` 만 남는다(2026-10-30). `unity --no-banner command --project-path "$PWD" --caller plugin --skill unity-cli <그룹> <이름>` 꼴로 쓴다(`Defense.Unity/CLAUDE.md` 의 `U`).
- **`build create_profile --platform Web` 은 PlayerSettings 전체 사본(944줄)을 프로필에 넣는다** — 그대로 두면 `ProjectSettings/` 를 바꿔도 Web 빌드에 반영되지 않는다. 내부 `BuildProfile.RemovePlayerSettings(true)` 로는 안 지워졌고 `SerializedObject` 로 `m_PlayerSettingsYaml.m_Settings` 를 비워야 했다(Android 프로필은 사본 없이 생성). `Defense.Unity/CLAUDE.md` 「검토 기준」 한 줄.
- **`build run --profileName` 만 주면 활성 대상(macOS)으로 빌드된다** — pipeline 0.9.1 `Editor/Commands/Build/BuildCommand.cs` 가 대상을 프로필 적용 전에 정하고 개발 빌드도 `options` 로만 받는다. `--target Android --options '["Development"]'` 를 같이 준다. 첫 시도가 `.app` 을 만들어 지웠다(2026-10-30).
- **플랫폼을 바꿔 빌드하면 에디터가 URP 에셋(셰이더 프리필터) · `ProjectSettings.asset`(플랫폼별 배칭)을 다시 저장한다** — 빌드 뒤 `git status`, 「에디터 자동 변환」 커밋으로 따로(`4ec4f97` · `4fdea24`). WebGL 은 Mobile · PC 두 품질 단계를 다 담아(PC 단계는 Android · iPhone 만 제외) 둘 다 바뀐다 · `UniversalRenderPipelineGlobalSettings` 의 `m_RuntimeSettings` 는 빌드 중에만 채워지는 스트리핑 결과라 마지막 빌드 플랫폼이 커밋 내용을 정한다(센서 `P00.S2.UNI.05` · `.07` △ — 소스 `ShaderBuildPreprocessor.cs` · `BuildTargetExtensions.cs`).
- **창 없는 에디터(`Unity -batchmode` 를 `-quit` 없이)는 `unity status` 에 안 나온다** — 준비는 `unity command … editor status` 의 `ready` 로 본다. 끌 때는 `script eval` 로 `EditorApplication.delayCall += () => EditorApplication.Exit(0)`(4초). 에디터가 프로젝트를 잡고 있으면 `unity test` · `unity build` 는 시작 전에 거부된다(종료 6).
- **헤드리스 Chrome `--virtual-time-budget` 으로 Unity WebGL 을 찍으면 스플래시에서 멈춘다**(실제 약 5초만 돈다). `--remote-debugging-port` 로 띄우고 DevTools 프로토콜(`Page.navigate` → 실제 대기 → `Page.captureScreenshot`)로 찍는다 — Node 24 내장 `WebSocket` 으로 40줄. Brotli 빌드는 `.br` 에 `Content-Encoding: br` 를 붙이는 서버가 필요하다(`python3 -m http.server` 로는 안 열린다).

- **Unity 에디터 프로세스의 명령줄을 출력하지 않는다**(`pgrep -fl Unity` · `ps aux`) — Hub 가 띄운 에디터는 `-accessToken <값>` 을 인자로 받는다. 2026-10-30 세션 4 가 한 번 출력했다(다이제스트는 도구 결과 앞 600자만 남겨 Logs 에는 0건 — `grep -c accessToken` 으로 확인). 실행 여부는 `pgrep -q -f 'Unity.app/Contents/MacOS/Unity' && echo 실행 중` 처럼 개수 · 참거짓만 본다.
- Homebrew 에 `csharp-ls` formula 가 없다(2026-10-30 — `brew install csharp-ls` 가 비슷한 이름의 cask 만 제안). `dotnet tool install --global csharp-ls` 로 `~/.dotnet/tools` 에 설치한다. .NET 설치기가 만든 `/etc/paths.d/dotnet-cli-tools` 는 `~/.dotnet/tools` 를 문자 그대로 담아 macOS `path_helper` 가 풀지 못한다 — 셸 설정에 `export PATH="$PATH:$HOME/.dotnet/tools"` 가 따로 필요하다(세션의 `~/.zshrc` 수정은 권한 정책에 막혀 사용자가 넣는다).
- Unity Hub 「권장」 표시는 LTS 가 아니다 — 2026-10-30 Hub 가 권장한 `6000.6.7f1` 은 stream `SUPPORTED`, LTS 는 `6000.3.27f1`. Hub 캐시(`~/Library/Application Support/UnityHub/graphqlCache/*-data.json` 의 `UnityRelease:<버전>.stream`) 또는 `unity releases --stream lts` 로 확인한다.
- **커밋 작성자를 확인할 때 `%ae` 를 찍지 않는다** — G-11 이전 커밋은 개인 이메일이라 그대로 출력되고, 출력은 세션 다이제스트(Logs)에 남는다. noreply 여부만 `grep -c noreply` 로 센다. 2026-10-30 세션 4 가 `git log --format='%h %ae %s' -3` 으로 한 번 노출 → F0 비밀값 검사 대상에 넣었다.
- GitHub MCP 도구 이름은 서버 판마다 바뀐다(2026-10-29 실측: `issue_write` · `sub_issue_write` · `actions_run_trigger` · `pull_request_review_write` · `delete_repository` 가 세션 2 의 예상 목록에 없었다). **서버를 다시 연결하거나 도구 목록이 바뀌면 쓰기 도구가 전부 `permissions.ask` · `deny` 에 있는지 다시 대조한다** — 빠진 도구는 확인 없이 원격에 쓴다.

- 이 세션(훅 설치 세션)은 상위 `Games/` 에서 열려 있어 Defense 의 훅이 돌지 않았다. 다음부터는 `Games/Defense/` 에서 연다.
- 2026-10-29 첫 골격은 루트 단일 `games.planning`(InvestBuddy 판 기반)이었고 사용자 지시로 게임별 분리 · EasyCheck 원본 기준으로 다시 만들었다(G-06). 옛 골격은 삭제했다 — 내용은 이 과제와 `_공통` 에 옮겼다.

## 발견 로그 (누적, 최신 위)

- 2026-10-30 — S2 세션 센서(sonnet) + 판정 반론 1: 폴더 `03_작업기록/코드리뷰_20261030_S2/` · 미해결 0 · H 후보 H-02(PC 품질 단계 WebGL 제외 · 프로필 사본 테스트 · WebGL 게시처 압축). 고침 커밋 `Defense.Unity` `59f9a07`. ✔
- 2026-10-30 — S2: `com.unity.pipeline` 런타임 어셈블리는 `defineConstraints` 가 `UNITY_EDITOR || ENABLE_RUNTIME_PIPELINE(_DEV)` 라 플레이어에 안 들어간다 — Android APK `global-metadata.dat` 에서 `Unity.Pipeline` 0건 · `Defense.Core` 1건으로 확인. 라이선스는 Unity Terms of Service(패키지 `LICENSE.md`), 템플릿 `com.unity.template.urp-blank` 17.1.0 은 Unity Companion License. ✔
- 2026-10-30 — S2: Unity 6000.3.27f1 의 「Universal 3D」 템플릿은 URP 17.1 에셋으로 만들어져 17.3 에디터가 처음 열 때 · 빌드할 때 다시 저장한다(에셋 버전 12→13 · 머티리얼 버전 9→10). batchmode 라 「URP Material upgrade」 대화상자는 취소 로그만 남는다(Assets 에 머티리얼 0개). ✔
- 2026-10-30 — S2: 게이트 실측(Mac M5) — 에디터 닫힘 `unity test --mode EditMode` 18~20초 · 컴파일 오류는 종료 6 `TEST_RUN_ERROR` · 열림 `test run` 0.34초 · Android 개발 APK(IL2CPP) 첫 빌드 240초 · WebGL 377초(전환 재임포트 포함) · 프로젝트 생성 72초. ✔

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

- ~~Unity 6 정확한 버전은 설치 뒤.~~ → 6000.3.27f1 LTS(2026-10-30).
- Supercent 스타일은 [추정](`_공통/조사/Supercent_스타일보드.md` 3절) — 캡처 뒤 확정(E).
