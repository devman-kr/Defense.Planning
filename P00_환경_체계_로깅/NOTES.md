---
id: 20261029-p00-notes
title: NOTES — P00 작업 메모
summary: P00 를 이어받는 세션이 먼저 읽는 메모 — 남은 일 표 ①~⑨(F0 · S5 GitHub · 종결 포함), 환경 · 훅 · GitHub MCP 현재 상태, 사용자 대기, unity CLI 키체인 대화상자 같은 함정, 발견 로그를 담는다.
doc_type: note
status: final
lifecycle: living
created: 2026-10-29
updated: 2026-10-31
work_unit: P00
---
# NOTES — P00 작업 메모

세션이 작업하면서 **다음 세션이 알아야 할 것**을 적는 곳이다. 과제 지도는 [`README.md`](README.md), 결정은 [`결정기록.md`](결정기록.md), 여러 과제에 걸치는 메모는 [`../NOTES.md`](../NOTES.md), 세 게임 공통은 `_공통/README.md`.

**쓰는 법**: 위 세 절은 덮어쓰기(세션 끝에 갱신), 아래 절은 누적(새 항목 위에). 한 줄에 하나, 근거(파일:줄 · 명령 · 실측)를 붙인다. 추정은 **[추정]**, 에이전트 보고를 옮긴 것은 **△**. 비밀값 금지.

---

## 다음 세션 시작 전 확인 (덮어쓰기)

_갱신: 2026-10-30 — 세션 10(Opus 5.5): P00 잔여 작업 정리 — 완료 기준 실측 · 남은 일 표 · F0 비용 재측정 · `csharp-lsp` 확인 · 작업지시서 G-12 잔재. 그 전 세션 9: G-12 에디터는 세션이 연다 · 세션 8: NRE 감지 X-04 · 세션 6: 코딩 표준 S1b · S1c · 세션 7: S2 `Defense.Unity` 생성_

1. **지금 어느 단계**: 실행 — [`02_계획/계획서_20261030.md`](02_계획/계획서_20261030.md). 끝: S1 · S1b · S1c · S2 · S4(S1 · S2 로 흡수) · R1, 완료 기준(계획서 8절) 9개 중 5개 ✔. **남은 일은 아래 표가 전부다**(2026-10-30 세션 10 실측).

   | # | 남은 일 | 선행 조건 | 누가 | 승인 지점 | 규모 | 근거 |
   |---|---|---|---|---|---|---|
   | ① | **S3 D2 Blender 공식 MCP** — 공식 저장소에서 출처 · 라이선스 · 설치 방법 확인(지금 △) · Blender 확장 설치 · `.mcp.json` 에 `blender` · `enabledMcpjsonServers` · 쓰기 도구(임의 Python 실행 등) `permissions.ask` · 도구 이름 대조 · 큐브 → FBX 내보내기(D-05) · 설정 사본을 「현재 상태」에 | 없음 — **지금 가능**(Blender 5.2.3 설치 ✔ · Unity 에디터 꺼짐 2026-10-30 19:58) | 세션(확장 설치가 GUI 면 사용자) | `.mcp.json` · `settings.json` 변경 | S | 계획서 4절 S3 |
   | ② | **F0-2 비밀값 검사 도구** `_공통/_도구/비밀값_검사.py`(의존성 0 · 토큰 형태 + 개인 커밋 이메일, 값은 출력하지 않음) → 다섯 저장소 전체 이력 검사. 알려진 노출 1(세션 4 가 작성자 이메일을 한 번 출력 — 「함정」) | 없음 — 지금 가능 | 세션 | 찾으면 멈추고 알림 — 가리기는 ⑥ 재작성과 함께 | S | 계획서 4절 F0 2번 |
   | ③ | **F0-3 `.gitignore` 에 `.DS_Store`** — Planning(파일 있음 · 줄 없음) · Design · Logs(파일 없음). `Defense.Unity` · `_공통` 은 있음 ✔ | 없음 — 지금 가능 | 세션 | — | S | 실측 2026-10-30 |
   | ④ | **다른 두 게임 복사 목록**(D-02 · 완료 기준) — `_템플릿/` · 가이드 3(코드리뷰 · 프롬프트 · 지표) · `_도구/` · `Unity_CLAUDE.md` · 코딩 표준 · `.editorconfig` · `.gitignore` · `.gitattributes` · 비밀값 검사 · 설정 사본(`settings.json` · `.mcp.json`)을 이 NOTES 에 표로 | ② 뒤가 깔끔(비밀값 검사 도구가 아직 없다) | 세션 | — | S | 계획서 8절 |
   | ⑤ | `_공통` **Q-01** 트레일러 · **Q-02** 계정 · 저장소 이름 · **Q-03** Logs 공개 여부 | — | **사용자** | — | — | `_공통/README.md` 3절 |
   | ⑥ | **F0-1 작성자 재작성**(G-11) — `git-filter-repo` 설치(지금 없음) · Planning · Design · Logs · `_공통`(`Defense.Unity` 는 처음부터 noreply ✔) · 다른 세션을 모두 닫고(훅 커밋이 끼지 않게) | ⑤ Q-01 · ⑦ | 세션 | `brew install git-filter-repo` · 이력 재작성 — 하나씩 | S~M | 계획서 4절 F0 1번 |
   | ⑦ | **F0-1 해시 참조 처리 방식** — 재작성으로 해시가 바뀌는 커밋 79, 그 해시를 가리키는 줄 Planning 100 · Logs 364(계획서 추정 34줄의 열 배 넘게). Logs 를 고치면 G-05 와 부딪힌다. 권장: 본문은 두고 커밋 지도 파일 하나 | — | **사용자** | — | — | 결정기록 「미결」 · 계획서 맨 위 추기 |
   | ⑧ | **S5 F GitHub** — 저장소 5 생성(`games-common` · `Defense.Planning` · `Defense.Design` · `Defense.Logs` · `Defense.Unity`) · 원격 · 첫 푸시 · `main` 보호(강제 푸시 · 삭제 금지) · 문서 링크(Planning README 8절 · `Defense.Unity/README.md` · `_공통` 1절) | ② 0건 · ⑤ · ⑥ | 세션 | 저장소 생성 · 푸시 · 보호 규칙 — 저장소마다 | S | 계획서 4절 S5 |
   | ⑨ | **종결** — Planning 루트에서 `python3 -I _도구/코드리뷰_집계.py --task P00` → `지표.md` 한 행 · 작업색인 · 과제 README · 현황판 → `z.completed/` 로 `git mv` | ①~④ · ⑧ | 세션 | — | S | 계획서 5 · 8절 |

   순서 권장: 지금 ① · ② · ③ → ④ / 사용자 ⑤ · ⑦ → ⑥ → ⑧ → ⑨. ① 은 Blender 를 띄우므로 Unity 에디터를 쓰는 세션과 겹치지 않게 한다(G-01).
2. **P01 로 넘기는 것** — P00 종결을 막지 않는다. P01 계획서 2차 `DEF-M01` 에 넣도록 `../P01_게임설계_코어/NOTES.md` 4번에 적었다: X-04 남은 확인 2([기술근거](01_검토/기술근거_20261030_NRE감지.md) 4절 — 콘솔 개별 메시지 명령 · `csharp-ls` 분석기 진단) · [`보류작업.md`](보류작업.md) H-01 도구 견고성(첫 코드 센서 전) · H-02 ① PC 품질 단계 WebGL 제외 ② 빌드 프로필 사본 테스트(③ 은 `_공통` Q-05 · `DEF-M05`) · `Defense.Game` asmdef · `Devman.Core.Tests.EditMode` 어셈블리 · 템플릿 잔재 `Assets/TutorialInfo/` 정리.
3. **에디터는 세션이 연다 — `_공통` G-12**: 세션이 Unity CLI 로 창 없는 에디터를 띄워 `unity command` 로 다루고 끈다. 명령은 `Defense.Unity/CLAUDE.md` 「결정론 게이트」(`e227f1f` — 띄우기 4초 · 끄기 1초 실측). 사용자가 연 에디터의 종료 · 재시작은 승인 지점. 사용자 GUI 에디터를 쓰는 경로는 아직 실측 없음.
4. **`Defense.Unity` 지금 모습**: 로컬 `main`, 원격 없음 — S2 `e46ecab`..`4dfe06d` · S1c `aeccdae` · `6130ea4` · `4d20f5b` · G-12 `e227f1f` · `e5741e3`. 게이트 에디터 닫힘 `unity test` 약 20초 · 열림 `unity command` 0.3초. 빌드 장부 `z.builds/BUILDS.md`(Android 개발 APK 42.7 MB · WebGL 14 MB). 작업 보고 `Defense.Unity/z.docs/work_reports/20261030/` 3편 · 센서 기록 `03_작업기록/코드리뷰_20261030_S1` · `_S1b` · `_S1c` · `_S2`. 코딩 표준 정본 `../_템플릿/Unity_csharp_coding_standards.md`(D-06 · D-07) = 사본 `Defense.Unity/z.docs/dev/csharp_coding_standards.md`, 네임스페이스 `Devman.Core.*` / `Defense.Game.*`.
5. **닫은 확인(2026-10-30 세션 10)**: `csharp-lsp` 가 `Defense.Unity` 의 `.cs` 에서 호버(`GateSmokeTests.cs:20` → `Assembly core`) · 정의 이동(`:20` → `:13`) ✔ — 이 세션은 프로젝트가 생긴 뒤 열렸다. 개명 전 생성물 `Defense.Core.csproj`(17:30, git 밖)가 남아 있지만 `Defense.Unity.slnx` 는 `Devman.Core.csproj` 만 문다.
6. **P02(문서 프론트매터, G-18)에서 넘겨받을 것**(2026-10-31 종결, 세션 af266641 — 기록 `../z.completed/P02_문서_프론트매터/`): ④ 복사 목록 — 세 작업 공간 `.claude/settings.json` 에는 PostToolUse 훅(`fm_lint.py --hook`)이 이미 들어 있고, `_템플릿/` 은 프론트매터 골격이 붙은 판이며, `Unity_README.md` 는 복사할 때 블록을 뗀다(`_공통/문서규약.md` 10절). ② 비밀값 검사 대상에 P02 의 새 파일이 든다 — `_공통/_도구/fm_lint.py` · `fm_migrate.py` · `tests/`(픽스처 포함) · `_공통/문서규약.md` · 이 과제 폴더. 세션 종료 5번에 문서 검사(`fm_lint.py --strict`)가 들어갔다. 새 세션을 처음 열면 프론트매터가 붙은 CLAUDE.md 를 그대로 따르는지 본다(P02 계획서 6절 — S3 에서 하네스가 블록을 떼고 읽는 것을 한 번 봄). GitHub 이 프론트매터를 표로 그리는지는 ⑧ 공개 뒤 화면으로 본다. 이 파일을 고칠 때마다 훅이 「Supercent 스타일은 [추정]」으로 시작하는 줄에 L20 경고를 낸다 — 괄호 표기가 링크 꼴이라서다(지난 기록이라 P02 는 고치지 않았다 — `]` 뒤를 띄우면 사라진다).

## 현재 상태 (덮어쓰기)

_갱신: 2026-10-30_

| 항목 | 상태 |
|---|---|
| 검토 | 검토서 2026-10-29 ✔ · 코딩 표준 검토서 2026-10-30 ✔ · NRE 감지 기술근거 2026-10-30 ✔ |
| 결정 | D-01~D-08 · 공통 G-01~G-12 ✔ · 미결 `_공통` Q-01~Q-05 · 이 과제 미결 1(F0 해시 참조 방식 — 결정기록 「미결」) |
| 계획 | 계획서 1차 2026-10-30 — S1 · S1b · S1c · S2 · S4(흡수) · R1 ✔ · 남은 일 1번 표 ①~⑨ |
| 저장소 변경 | `Defense.Unity`(2026-10-30 신설) · `Defense.Planning` · `Defense.Design` · `Defense.Logs` · `_공통` 모두 `main` 로컬, 원격 없음. noreply 아닌 커밋: Planning 23/52 · Design 4/4 · Logs 2/15 · `_공통` 4/8 · Unity 0/13(2026-10-30 세션 10 — 개수만, 값은 출력하지 않음) |
| 환경 | Unity Hub 3.22.5 · Unity **6000.3.27f1 LTS**(arm64) + Android(OpenJDK 17 · SDK · NDK r27c · build-tools 36) · WebGL · Blender 5.2.3 LTS · .NET SDK 10.0.403 · `csharp-ls` 0.28.0(PATH ✔) · Unity CLI 1.0.0-beta.13(`~/.unity/bin`, 로그인 · 라이선스 Personal 활성 · 키체인 「항상 허용」 ✔) · Chrome(헤드리스 캡처) · gh ✔ `devman-kr`. 없음: git-lfs(D-05) · git-filter-repo(⑥ 때) |
| Claude Code 플러그인 | `unity@claude-plugins-official` 0.1.6-beta ✔(스킬 `unity-cli` 외) · `csharp-lsp`(`csharp-ls` 0.28.0 — 호버 · 정의 이동 ✔ 2026-10-30) · `session-report` · `microsoft-docs` |
| `Defense.Unity` 패키지 | 템플릿 기본 + `com.unity.pipeline` 0.9.1-exp.1(Unity 레지스트리 · 실험판 · `unity command` 용 — 플레이어 빌드에 런타임 미포함 확인) |
| 훅 | 프롬프트 · 다이제스트 · `SessionEnd` 커밋 동작 ✔(Logs `99e4e35` 등 2026-10-30 — R1 닫음) |
| GitHub MCP | 작업 공간 루트 `.mcp.json`(git 밖) — 공식 원격 서버 `https://api.githubcopilot.com/mcp/`, 헤더 `Authorization: Bearer ${GITHUB_PAT}` · `X-MCP-Toolsets: context,repos,issues,pull_requests,actions`. `.claude/settings.json` 에 `enabledMcpjsonServers: ["github"]` · `permissions.deny` `delete_repository` · `permissions.ask` 24개(저장소 생성 · 포크 · 파일 쓰기/삭제 · 브랜치 · PR 생성/수정/머지/리뷰 · 이슈 · 하위 이슈 · 댓글 · 워크플로 실행). **연결 ✔ 2026-10-29** — `get_me` 로그인 `devman-kr`. `gh auth status` 범위 `repo` · `workflow` · `read:org` · `gist` |
| Blender MCP | 미등록 — `.mcp.json` 은 `github` 하나(2026-10-30 실측) → 1번 표 ① |

## 사용자 대기 (덮어쓰기)

- `_공통` Q-01~Q-03 — S5 선행(1번 표 ⑤).
- F0 해시 참조 처리 방식 — 작성자 재작성 전(1번 표 ⑦, 결정기록 「미결」).
- Unity 플러그인 상시 컨텍스트 비용 — 세션이 `/context` 를 볼 수 없어 사용자가 보면 「현재 상태」에 적는다(P00 을 막지 않음).
- `Defense.Unity` 실기기 설치(선택) — `z.builds/debug/defense_20261030_3d4abc4_android-dev.apk`.

---

## 함정 · 주의 (누적)

- **`unity` CLI 는 실행마다 macOS 키체인 접근 대화상자를 띄운다**(저장된 로그인 토큰 읽기 — Hub `broker-audit` 「stored-token-valid」). 사용자가 「항상 허용」을 누르기 전까지 batchmode 게이트도 그 응답을 기다린다 — 2026-10-30 19:28:33 프롬프트 → 19:35:16 허용(403초), 실제 게이트 7초. 세션은 게이트를 돌릴 때 대화상자를 알리고 시간에서 뺀다. 사용자 결정 2026-10-30: **다음에 뜨면 「항상 허용」을 누른다** — 그 뒤 첫 `unity` 실행에서 대화상자가 안 뜨는지(실행 시간이 7초 안팎인지) 다음 세션이 확인하고 이 항목을 「닫음」으로. **닫음 2026-10-30 19:47** — 세션 9 에서 대화상자 두 번(19:45:57 게이트 · 19:47:31 `unity auth status`), 둘째에 「항상 허용」, 셋째 실행은 대화상자 없이 1초(`securityd` 새 기록 0). `securityd` 로그 확인: `/usr/bin/log show --predicate 'process == "securityd"' | grep 'keychain prompt'`(zsh 의 `log` 는 내장 명령이라 `/usr/bin/log`).
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

- 2026-10-30 — 세션 10 잔여 정리: 계획서 8절 완료 기준 중 넷(Unity 버전 · S2 커밋 · 게이트 명령 · R1)은 이미 끝났는데 체크가 안 돼 있었다 — 세션마다 결과를 NOTES 6번 같은 긴 줄에 덧붙이고 8절은 S1c 만 고쳤다. 과제 README 「다음 행동」은 S1b · S1c 줄이 끼어들어 같은 문구가 두 번 들어가 있었다. F0 1번 비용은 계획 때 「문서 해시 참조 34줄」이었지만 작성자 재작성은 첫 커밋부터 해시를 바꿔(네 저장소 모두 첫 커밋부터 noreply 아님) 바뀌는 커밋 79 · 참조 줄 Planning 100 · Logs 364 다 — 세션이 하루 만에 열 배 넘게 키웠다. `_템플릿/작업지시서.md:29` 에 G-12 이전 문구 「사용자가 연 에디터」가 남아 있어 고쳤다(`04dfe9b` 는 21줄 승인 지점만 고쳤다). ✔
- 2026-10-30 — 세션 9: G-12 열림 경로를 문서 명령 그대로 실측 — Blender 확인 → 창 없는 에디터 `ready` 4초(`Library/` 캐시) → `U test run --mode editor` 실패 0 → `script eval` 로 `EditorApplication.Exit(0)` 1초. 사용자 GUI 에디터를 쓰는 경로는 아직 실측 없음. ✔
- 2026-10-30 — 세션 8(Opus 5.5) NRE 조기 감지 웹 조사 → X-04 · [`01_검토/기술근거_20261030_NRE감지.md`](01_검토/기술근거_20261030_NRE감지.md). 첫 제안의 Nullable 참조 형식은 코딩 표준 §5.5(`#nullable` 금지)와 충돌해 뺐다 — 웹 조사 전에 저장소 표준 · 작업 보고를 먼저 대조했어야 했다(S2 가 이미 끝나 「S2 에서 확인할 것」 셋 중 둘은 실측으로 답이 있었다). 공식 내장 직렬화 참조 검증 도구는 찾지 못했다(웹 검색 기준 △).
- 2026-10-30 — S1c 세션 센서(sonnet 1): 폴더 [`03_작업기록/코드리뷰_20261030_S1c/`](03_작업기록/코드리뷰_20261030_S1c/) · 미해결 0 · H 후보 없음. 장부(G-02)에 문서 · AI 생성 사본도 적어야 한다는 지적 — 코드 아닌 파일을 장부 대상으로 생각하지 못했다. 둘째 게이트 실행 410초(첫 14초)는 `unity` CLI 의 키체인 접근 대화상자를 사용자가 6분 43초 뒤에 허용한 시간 — `securityd` 로그로 확인 ✔(「함정」). 세션 창이 닫혀도 서브에이전트 전사는 `subagents/` 에 남아 추출 도구가 그대로 뽑았다 ✔
- 2026-10-30 — S1b 세션 센서(sonnet, 2라운드 + 반론 D): 폴더 [`03_작업기록/코드리뷰_20261030_S1b/`](03_작업기록/코드리뷰_20261030_S1b/) · 미해결 0 · H 후보 없음(S1c 몫 1). 문서 리뷰에 Unity 매뉴얼 WebFetch 대조를 넣으니 「왜」의 사실 오류 2(파일 이름 · MPB)와 근거 없는 「왜」 6줄을 잡았다 — 결정 D-07 ⑦ 「매뉴얼로 확인한 것만」이 규칙으로 있어서 센서가 그 기준으로 대조할 수 있었다. 2라운드의 「처리표 고침 표본 검산」이 「부분만 고침」 4건을 되돌려 줬다. 분량 목표(12 KB)는 결정 항목(신설 7절 · 「왜」 · 근거)만으로 넘는 추정 오류였다 ✔
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
