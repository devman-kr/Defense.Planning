---
id: 20261029-p00-notes
title: NOTES — P00 작업 메모
summary: P00 를 이어받는 세션이 먼저 읽는 메모 — 남은 일 표(⑧ S5 GitHub · ⑨ 종결만 남음), 다른 두 게임 복사 목록(D-02), 환경 · Blender CLI · GitHub MCP 현재 상태, filter-repo · 키체인 같은 함정, 발견 로그를 담는다.
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

_갱신: 2026-10-31 — 세션 10(Opus 5.5) 이어서: F0 실행(첫 푸시 전 비밀값 검사 G-19 · Logs `.gitignore` · 작성자 재작성 G-16) · Blender CLI 확인 기록(D-09) · 다른 두 게임 복사 목록 · 원격 링크. 그 전 2026-10-30 세션 10: 잔여 정리 · 결정 G-13~G-17 · D-09 · H-03 / 세션 9: G-12 / 세션 8: NRE 감지 X-04 / 세션 6: 코딩 표준 S1b · S1c / 세션 7: S2 `Defense.Unity` 생성_

1. **지금 어느 단계**: 실행 — [`02_계획/계획서_20261030.md`](02_계획/계획서_20261030.md)(추기 3차까지). 끝: S1 · S1b · S1c · S2 · S3(D-09 — CLI 확인) · S4(S1 · S2 로 흡수) · R1 · F0. **남은 것은 ⑧ S5 GitHub 와 ⑨ 종결뿐이다.** 2026-10-30 에 정리한 아홉 줄의 처리:

   | # | 남은 일(2026-10-30) | 처리 | 근거 |
   |---|---|---|---|
   | ① | S3 Blender 공식 MCP | ✔ CLI 확인으로 바꿔 끝(2026-10-30) — 「현재 상태」 Blender 행. 공식 MCP 는 보류 H-03 | D-09 · `_공통` G-17 |
   | ② | F0-2 비밀값 검사 | ✔ 2026-10-31 — 일회용 스크립트로 세 게임 11개 저장소(커밋하지 않음). 재작성 뒤 실제 비밀값 0, Logs 리뷰 보고 속 가짜 값만 남아 첫 푸시 질문에 적는다 | `_공통` G-19 |
   | ③ | F0-3 `.gitignore` 에 `.DS_Store` | ✔ Planning `9d5cf0e` · Design `d09c616` · Logs `efc4b12`(재작성 뒤 해시) | 실측 |
   | ④ | 다른 두 게임 복사 목록 | ✔ 아래 2번 | D-02 |
   | ⑤ | `_공통` Q-01~Q-03 | ✔ G-13 · G-14 · G-15(2026-10-30) | `_공통/README.md` 2절 |
   | ⑥ | F0-1 작성자 재작성 | ✔ 2026-10-31 08:04(승인 ②) — 10개 저장소 41커밋 · Logs 다이제스트 3곳 가림 · 검증 10/10 | `_공통` G-16 비고 · 계획서 추기 3차 |
   | ⑦ | F0-1 해시 참조 방식 | ✔ 고치지 않는다 | `_공통` G-16 |
   | ⑧ | **S5 GitHub** — 저장소 5 생성(`games-common` · `Defense.Planning` · `Defense.Design` · `Defense.Logs` · `Defense.Unity`, 공개) · 원격 · 첫 푸시 · `main` 보호(강제 푸시 · 삭제 금지) | **남음** — 승인 지점 셋(생성 · 푸시 · 보호). 문서 링크는 미리 넣었다(Planning README 8절 · Design README 4절 · `Defense.Unity/README.md` 「개발 과정」) | 계획서 4절 S5 |
   | ⑨ | **종결** — `_도구/코드리뷰_집계.py --task P00` → `지표.md` 한 행 · 보류 H-01~H-03 을 P01 로 · 작업색인 · 과제 README · 현황판 → `z.completed/` | **남음** — ⑧ 뒤 | 계획서 5 · 8절 |

2. **다른 두 게임 복사 목록**(D-02 — AirShooter · RideShooter 의 P00 이 가져갈 것, 2026-10-31 실측). 「다르다 · 같다」는 게임 이름을 맞춰 바이트로 비교한 결과다.

   | 무엇 | Defense 원본 | 다른 두 게임 지금 | 가져갈 때 |
   |---|---|---|---|
   | Planning 템플릿 6 — `검토서` · `계획서` · `과제_NOTES` · `과제_README` · `리뷰어_지시` · `작업지시서` | `Defense.Planning/_템플릿/` — Unity 저장소 하나 기준(X-03) | EasyCheck 사본 + 프론트매터 — 다르다 | 덮어쓰고 `Defense` · `DEF-` 를 그 게임 이름 · 마일스톤 접두로 바꾼다 |
   | `_템플릿/결정기록.md` | 같은 폴더 | 같다 | 할 일 없음 |
   | Unity 템플릿 4 — `Unity_CLAUDE.md` · `Unity_README.md` · `Unity_csharp_coding_standards.md` · `Unity_.editorconfig` | 같은 폴더 | 없다 | 복사한다. `Unity_CLAUDE.md` 의 게이트 명령 · 시간은 그 게임 Unity 저장소를 만든 뒤 실측해 고친다. `Unity_README.md` 는 Unity 저장소로 옮길 때 프론트매터 블록을 뗀다(`_공통/문서규약.md` 10절) |
   | 루트 `CLAUDE.md` 정본 `_템플릿/루트_CLAUDE.md` | 같은 폴더 | 그 게임 판이 따로 있다(G-12 · G-18 반영) | 덮어쓰지 않고 세 곳만 합친다 — 첫 단락의 git 밖 설정 문장 · 「푸시」의 GitHub MCP 단락 · 「코드 리뷰」의 X-03 문구와 고위험 경로(가이드 5절). 합친 뒤 작업 공간 `CLAUDE.md` 로 복사(X-01) |
   | 가이드 3 — `코드리뷰_가이드.md` · `프롬프트_작성_가이드.md` · `지표.md` | Planning 루트 | EasyCheck 사본 + 프론트매터 — 다르다 | 덮어쓰고 이름을 바꾼다. 본문의 EasyCheck 선례 번호(X-11 · X-12 · P02 · P05)는 그대로 둔다(Planning README 8절) |
   | 도구 2 — `_도구/센서기록_추출.py` · `코드리뷰_집계.py` | Planning `_도구/`(241 · 285줄 — 영역 코드 · 프론트매터 블록 쓰기) | EasyCheck 판(141 · 168줄) | 덮어쓴다. 보류 H-01(견고성)은 Defense `DEF-M01` 에서 고친 판을 가져간다 |
   | 작업 공간 `.claude/settings.json` | 훅 4(프롬프트 · 다이제스트 · 세션 종료 커밋 · 문서 검사) + GitHub MCP 권한(`ask` 24 · `deny` 1 · `enabledMcpjsonServers`) | 훅 4 ✔(P02) · 권한 없음 | GitHub MCP 를 쓸 때 `permissions` · `enabledMcpjsonServers` 를 복사하고 도구 이름을 대조한다(「함정」) |
   | 작업 공간 `.mcp.json` | GitHub 공식 원격 서버(토큰은 환경 변수 `GITHUB_PAT` — 파일에 값 없음) | 없다 | 그대로 복사 |
   | 저장소 `.gitignore` | Planning · Design `.DS_Store` · Logs `hook_errors.log` · `.DS_Store` · Unity 저장소 `.gitignore` · `.gitattributes` | Planning · Logs 는 `.DS_Store` 줄이 없고 Design 은 파일이 없다 | `.DS_Store` 줄을 더한다. Unity 저장소 두 파일은 그 저장소를 만들 때 |
   | 로컬 `user.email`(noreply) | 저장소마다 | 셋 다 ✔(G-11) | Unity 저장소를 만들 때 바로 |
   | 비밀값 검사 도구 | 없음(G-19 — 남기지 않았다) | — | 가져갈 것 없음. 처음 올릴 때 다시 검사할지는 그 게임 P00 |
   | 가져가지 않는 것 | Planning `README.md`(7절 X-nn 은 게임마다) · `.claude/settings.local.json`(이 Mac 의 세션 허용 기록) · 코드 `Devman.Core`(그 게임 첫 마일스톤에서 — G-07, README 「출처」에 원본 커밋) | — | — |

3. **P01 로 넘기는 것** — P00 종결을 막지 않는다. `../P01_게임설계_코어/NOTES.md` 4번에 적었다: X-04 남은 확인 2([기술근거](01_검토/기술근거_20261030_NRE감지.md) 4절) · [`보류작업.md`](보류작업.md) H-01 도구 견고성(첫 코드 센서 전) · H-02 ① PC 품질 단계 WebGL 제외 ② 빌드 프로필 사본 테스트(③ 은 `_공통` Q-05 · `DEF-M05`) · `Defense.Game` asmdef · `Devman.Core.Tests.EditMode` 어셈블리 · 템플릿 잔재 `Assets/TutorialInfo/` 정리. **종결 때 더할 것**: H-03 Blender 공식 MCP 보류 · Blender CLI → Unity 의 두 가지(`DEF-M03`) — 클립 이름에 뼈대 이름이 붙고(`Rig|Idle`) 루트에 X 270° 가 남는다. 내보낼 때 `bake_space_transform` 이나 가져올 때 `bakeAxisConversion` 으로 정리한다(둘 다 미실측).
4. **에디터는 세션이 연다 — `_공통` G-12**: 세션이 Unity CLI 로 창 없는 에디터를 띄워 `unity command` 로 다루고 끈다. 명령은 `Defense.Unity/CLAUDE.md` 「결정론 게이트」(`e227f1f` — 띄우기 4초 · 끄기 1초 실측). 사용자가 연 에디터의 종료 · 재시작은 승인 지점. 사용자 GUI 에디터를 쓰는 경로는 아직 실측 없음.
5. **`Defense.Unity` 지금 모습**: 로컬 `main`, 원격 없음(→ ⑧) — S2 `e46ecab`..`4dfe06d` · S1c `aeccdae` · `6130ea4` · `4d20f5b` · G-12 `e227f1f` · `e5741e3` · G-13 `4aa5df9` · P02 `26584fb` · `0ca28f8`. 재작성 대상이 아니어서 해시가 그대로다. 게이트 에디터 닫힘 `unity test` 약 20초 · 열림 `unity command` 0.3초. 빌드 장부 `z.builds/BUILDS.md`(Android 개발 APK 42.7 MB · WebGL 14 MB). 작업 보고 `Defense.Unity/z.docs/work_reports/20261030/` 3편 · `20261031/` 2편 · 센서 기록 `03_작업기록/코드리뷰_20261030_S1` · `_S1b` · `_S1c` · `_S2`. 코딩 표준 정본 `../_템플릿/Unity_csharp_coding_standards.md`(D-06 · D-07) = 사본 `Defense.Unity/z.docs/dev/csharp_coding_standards.md`, 네임스페이스 `Devman.Core.*` / `Defense.Game.*`.
6. **P02(문서 프론트매터, G-18)에서 넘겨받은 것 — 처리(2026-10-31)**: 복사 목록(2번)에 훅 · 프론트매터 템플릿 · `Unity_README.md` 블록 떼기를 넣었다 ✔. P02 의 새 파일이 비밀값 검사에 들었다 — `_공통/_도구/tests/` 의 이메일은 `@example.invalid` 시험 주소 ✔. 하네스는 `CLAUDE.md` 의 프론트매터 블록을 떼고 읽는다 — 이 세션이 2026-10-31 받은 `Defense.Unity/CLAUDE.md` 내용이 블록 없이 `# Defense.Unity` 로 시작했다 ✔. **남음**: GitHub 이 프론트매터를 표로 그리는지는 ⑧ 푸시 뒤 화면으로 본다. 이 파일 「미해결」의 L20 경고 줄은 P02 판단대로 그대로 둔다.

## 현재 상태 (덮어쓰기)

_갱신: 2026-10-31_

| 항목 | 상태 |
|---|---|
| 검토 | 검토서 2026-10-29 ✔ · 코딩 표준 검토서 2026-10-30 ✔ · NRE 감지 기술근거 2026-10-30 ✔ |
| 결정 | D-01~D-09 · 공통 G-01~G-19 ✔ · 이 과제 미결 없음(`_공통` Q-04 · Q-05 는 P00 을 막지 않는다) |
| 계획 | 계획서 1차 + 추기 3차(2026-10-31) — 남은 1번 표 ⑧ · ⑨ |
| 저장소 변경 | `Defense.Unity` · `Defense.Planning` · `Defense.Design` · `Defense.Logs` · `_공통` 모두 `main` 로컬, 원격 없음(→ ⑧). 2026-10-31 작성자 재작성 뒤 noreply 아닌 커밋 0 — 세 게임 11개 저장소 전부(`git log --all --format='%ae%n%ce' \| grep -vc noreply` — 값은 출력하지 않음). 재작성 전 백업 bundle 은 세션 스크래치패드에만(종결 때 지운다) |
| 환경 | Unity Hub 3.22.5 · Unity **6000.3.27f1 LTS**(arm64) + Android(OpenJDK 17 · SDK · NDK r27c · build-tools 36) · WebGL · Blender 5.2.3 LTS · .NET SDK 10.0.403 · `csharp-ls` 0.28.0(PATH ✔) · Unity CLI 1.0.0-beta.13(`~/.unity/bin`, 로그인 · 라이선스 Personal 활성 · 키체인 「항상 허용」 ✔) · Chrome(헤드리스 캡처) · gh ✔ `devman-kr` · git-filter-repo 2.47.0(Homebrew, 2026-10-30). 없음: git-lfs(D-05) |
| Claude Code 플러그인 | `unity@claude-plugins-official` 0.1.6-beta ✔(스킬 `unity-cli` 외) · `csharp-lsp`(`csharp-ls` 0.28.0 — 호버 · 정의 이동 ✔ 2026-10-30) · `session-report` · `microsoft-docs` |
| `Defense.Unity` 패키지 | 템플릿 기본 + `com.unity.pipeline` 0.9.1-exp.1(Unity 레지스트리 · 실험판 · `unity command` 용 — 플레이어 빌드에 런타임 미포함 확인) |
| 훅 | 프롬프트 · 다이제스트 · `SessionEnd` 커밋 · 문서 검사(`PostToolUse` `fm_lint.py --hook`, P02 2026-10-31) 동작 ✔ |
| GitHub MCP | 작업 공간 루트 `.mcp.json`(git 밖) — 공식 원격 서버 `https://api.githubcopilot.com/mcp/`, 헤더 `Authorization: Bearer ${GITHUB_PAT}` · `X-MCP-Toolsets: context,repos,issues,pull_requests,actions`. `.claude/settings.json` 에 `enabledMcpjsonServers: ["github"]` · `permissions.deny` `delete_repository` · `permissions.ask` 24개(저장소 생성 · 포크 · 파일 쓰기/삭제 · 브랜치 · PR 생성/수정/머지/리뷰 · 이슈 · 하위 이슈 · 댓글 · 워크플로 실행). **연결 ✔ 2026-10-29** — `get_me` 로그인 `devman-kr`. `gh auth status` 범위 `repo` · `workflow` · `read:org` · `gist` |
| Blender | **CLI**(`_공통` G-17 · D-09) — 2026-10-30 확인: 창 없는 Blender 5.2.3(`Blender -b --factory-startup -noaudio --python-exit-code 1 --python <스크립트> -- <인자>`)로 로우폴리 탑(꼭짓점 80 · 면 84) · 팔레트 UV(지붕 17 · 덮개 17 · 벽 50 면) · 뼈 2 자동 가중치(Root 24 · Top 56 꼭짓점) · 동작 2(Idle 1~25 · Hit 1~10 프레임, NLA) · FBX 59,948 B · EEVEE · Workbench 렌더 — 한 번에 3.78초 · 최대 RSS 390 MB(Mac M5). FBX → 일회용 Unity 6000.3.27f1 프로젝트 batchmode 가져오기: Generic · 클립 `Rig\|Idle` 1.000초 · `Rig\|Hit` 0.375초(24fps) · 뼈 2 · 루트 X 270°. 렌더 · 스크립트는 `z.captures/20261030/`(git 밖). 공식 MCP 는 미등록(보류 H-03) |

## 사용자 대기 (덮어쓰기)

- ⑧ S5 승인 지점 셋 — 저장소 생성 · 첫 푸시(가짜 값 목록 포함) · `main` 보호. 세션이 하나씩 묻는다.
- Unity 플러그인 상시 컨텍스트 비용 — 세션이 `/context` 를 볼 수 없어 사용자가 보면 「현재 상태」에 적는다(P00 을 막지 않음).
- `Defense.Unity` 실기기 설치(선택) — `z.builds/debug/defense_20261030_3d4abc4_android-dev.apk`.

---

## 함정 · 주의 (누적)

- **`git filter-repo` 는 기본으로 커밋 메시지 속 옛 해시를 새 해시로 바꿔 쓴다** — 메시지를 그대로 두려면 `--preserve-commit-hashes`(2026-10-31 복사본 예행에서 Planning 메시지 2곳이 바뀌어 검증이 잡았다). 이력 재작성은 복사본(`cp -Rp`)에서 같은 명령 · 같은 검증으로 먼저 돌려 본다.
- **가린 개인 이메일은 옛 세션을 이어 열면 돌아온다** — `Stop` · `SessionEnd` 훅이 그 세션 전사로 다이제스트를 통째로 다시 쓰는데, 세션 7a119d3c · f4cc0549 · 0f0e49ba 의 전사에는 이메일이 그대로 있다. 이 셋은 이어 열지 않는다. 열었다면 푸시 전에 `grep -c -F "$(git config --global user.email)" sessions/*.md` 로 개수만 본다(명령에 값을 쓰지 않는다).
- **서브에이전트 보고는 프롬프트 로그에 실린다** — 보고가 사용자 차례(「Subagent handback」)로 들어와 `UserPromptSubmit` 훅이 `prompts/` 에 쓴다. 비밀값 검사 도구의 리뷰어가 실패 시나리오로 쓴 가짜 비밀번호 · 개인 키 머리줄이 공개 Logs `prompts/20261030.md` 에 남은 까닭이다(2026-10-31 검사).
- **zsh 는 따옴표 없는 변수를 낱말로 나누지 않는다** — `R="a b"; cmd $R` 는 인자 하나다. 경로 여럿은 배열(`R=(a b)` · `"${R[@]}"`)로 넘긴다(2026-10-31 예행 첫 시도가 경로 하나로 넘어가 실패 — 바뀐 것 없음).
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

- 2026-10-31 — 세션 10 F0 실행: P02 종결 확인 → 11개 저장소 재검사(차단 34 — 41커밋 신원 · 다이제스트 3곳 개인 이메일 · 리뷰 보고 가짜 값) → Logs `.gitignore` · 훅 출력 미커밋분 커밋 → 복사본 10개 예행 → 실제 bundle 백업 → 승인 ② → `filter-repo` 2초 · 검증 10/10 · 새 HEAD 가 예행과 같음 → 재검사 차단 10(전부 가짜 값) · 확인 17(시험 주소 · 변수 이름 예시). 비밀값 결정 번호는 P02 가 G-18 을 먼저 써서 G-19. ✔
- 2026-10-31 — 비밀값 검사 「확인」 판정(값은 가리고 앞뒤 맥락만 봄): `_공통/_도구/tests/test_log_frontmatter.py:395` 와 P02 다이제스트 `sessions/20261030_af266641.md:3147` 은 `@example.invalid` 시험 주소, 세션 10 다이제스트 `:2899` 는 도구 주석 속 변수 이름 예시, `prompts/20261030.md:1978~1984` 는 도구 리뷰 보고의 시험용 값 · `.test` 주소 — 모두 가짜 ✔
- 2026-10-30 — Blender CLI 확인(D-09)의 첫 렌더에 보인 틈 · 이상한 자세는 Blender 가 아니라 스크립트 탓이었다 — 동작 사이에 자세를 초기화하지 않았고, 포즈 뼈 축은 뼈 기준(Y 가 뼈 방향)인데 월드 축으로 늘렸고, 팔레트 분류를 로컬 좌표로 했다. `smoke2.py` 에서 고쳤고 지붕 아래 띠는 회색 배경 렌더로 그림자임을 확인 ✔. 기록이 2026-10-31 로 늦은 것은 P02 를 기다려서다.
- 2026-10-30 — `csharp-lsp` 가 `Defense.Unity` 의 `.cs` 에서 호버(`GateSmokeTests.cs:20` → `Assembly core`) · 정의 이동(`:20` → `:13`) ✔. 개명 전 생성물 `Defense.Core.csproj`(17:30, git 밖)가 남아 있지만 `Defense.Unity.slnx` 는 `Devman.Core.csproj` 만 문다(옛 1번 5에서 옮김).
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
