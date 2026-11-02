---
id: 20261029-p01-notes
title: NOTES — P01 작업 메모
summary: P01 세션 인계 메모로, 설계 확정 상태와 다음 순서(계획서 1차 · 지시서 S1 승인 → S1 → S2 → 계획서 2차)를 적고, 2차에 넣을 DEF-M01 몫(X-04 NRE 감지 · P00 에서 넘어온 보류 H-05 · H-06)과 DEF-M03 Blender CLI 메모, 누적 함정 · 발견 로그 · 미해결을 담는다.
doc_type: note
status: final
lifecycle: living
created: 2026-10-29
updated: 2026-11-02
work_unit: P01
---
# NOTES — P01 작업 메모

세션이 작업하면서 **다음 세션이 알아야 할 것**을 적는 곳이다. 과제 지도는 [`README.md`](README.md), 결정은 [`결정기록.md`](결정기록.md), 여러 과제에 걸치는 메모는 [`../NOTES.md`](../NOTES.md), 세 게임 공통은 `_공통/README.md`.

**쓰는 법**: 위 세 절은 덮어쓰기(세션 끝에 갱신), 아래 절은 누적(새 항목 위에). 한 줄에 하나, 근거(파일:줄 · 명령 · 실측)를 붙인다. 추정은 **[추정]**, 에이전트 보고를 옮긴 것은 **△**. 비밀값 금지.

---

## 다음 세션 시작 전 확인 (덮어쓰기)

_갱신: 2026-10-30 — 세션 3 이어서: D-07~D-11 확정, 기획 저장소 신설(X-02 → 세 게임 공통 G-10) · 기획서 v0.4 · 룩앤필 목업 v1(사용자 확인) · 계획서 1차 · 지시서 S1 · S2_

1. **지금 어느 단계**: 계획 — 설계 확정, 미결 없음. 기획 정본은 `../../Defense.Design/기획서.md`. 이 폴더의 검토서는 시점 기록(추기만). 코드는 P00 D(`Defense.Unity` 생성) 뒤.
2. **다음 할 일 순서**: 계획서 1차(`02_계획/계획서_20261030.md`) · 지시서 S1 승인(사용자) → [S1](02_계획/지시서/20261030_S1_Design_데이터표.md) 데이터 표 · 곡선 목업 → [S2](02_계획/지시서/20261030_S2_Design_플레이검사체크리스트.md) 플레이검사 체크리스트 → 계획서 2차(P00 B · D 뒤 — 게이트 · 고위험 경로가 정해져야 구현 단계 검증 절을 쓴다). **P00 B · D 끝(2026-10-30 S2) — 계획서 2차 착수 가능**: 게이트 명령은 `Defense.Unity/CLAUDE.md` 「결정론 게이트」, 고위험 경로는 `코드리뷰_가이드.md` 5절. `Defense.Unity` 에는 `Assets/10_Scripts/Core/` · `Tests/EditMode/` asmdef 와 스모크 테스트 하나만 있다(나머지 폴더 · 코어 코드는 `DEF-M01`).
3. **착수 전 확인**: 기획을 바꾸는 지시는 결정기록 D-nn → 기획서 순서(검토서는 고치지 않는다). 새 기획안 · 신기능은 목업으로 먼저 보인다(사용자 2026-10-30 — 제작 템플릿은 작업 공간 루트 `NOTES.md` 할 일). 에셋 라이선스는 전부 △(`_공통/조사/무료_3D에셋_후보.md`) — 내려받을 때 팩 안 파일로 ✔. 제목 「Lantern Rush!」 스토어 직접 검색 · 상표는 공개(M05) 전.
4. **계획서 2차에 넣을 것(2026-10-30 세션 8)**: `DEF-M01` 범위에 NRE 조기 감지 장치 — Planning README 7절 X-04(분석기 DLL + `Default.ruleset` · `[Required]` · `validate_references` `[CliCommand]` · 같은 검증의 EditMode 테스트 · PlayMode 스모크 · 빌드 전 검증)와 그 게이트 명령. 근거 · 남은 확인 2는 [`../z.completed/P00_환경_체계_로깅/01_검토/기술근거_20261030_NRE감지.md`](../z.completed/P00_환경_체계_로깅/01_검토/기술근거_20261030_NRE감지.md). 분석기 DLL 은 외부 파일(`ASSETS.md`), 나머지는 직접 작성. **P00 에서 넘어온 `DEF-M01` 몫도 함께(2026-10-30 잔여 정리 · 2026-10-31 P00 종결 때 보류 이관)**: [`보류작업.md`](보류작업.md) H-05 Planning 도구 견고성(첫 코드 센서 기록 전 — P00 H-01) · H-06 ① PC 품질 단계에서 WebGL 제외 ② 빌드 프로필 PlayerSettings 사본 테스트(③ 은 `_공통` Q-05 · `DEF-M05` — P00 H-02) · `Defense.Game` asmdef · `Devman.Core.Tests.EditMode` 어셈블리 · 템플릿 잔재 `Defense.Unity/Assets/TutorialInfo/` 정리. **`DEF-M03`(아트)에 넣을 것(P03 종결 2026-11-01 로 갱신)**: Blender 는 CLI 로 다룬다(`_공통` G-17) — 파이프라인 한 바퀴(Blender `bpy` → FBX → 창 없는 에디터 → 샘플 씬 → CLI 캡처 · 프레임 → Blender ffmpeg MP4)는 P03 이 끝까지 돌렸다. 정본 스크립트 `Defense.Unity/Tools/Blender/make_enemies.py`, 가져오기 · 씬 · 녹화 코드 `Assets/10_Scripts/Editor/P03/`, 샘플 씬 `Assets/00_Scenes/P03_CLI_Sample.unity`, 명령 · 시간은 `Defense.Unity/CLAUDE.md` 「결정론 게이트」 캡처 줄(D-07). 실측 함정(Sonnet · Opus 두 세션이 같은 값): ① 클립 이름은 `SlimeRig|Idle`(뼈대 한 번) + 같은 이름 동작은 `.001`(`BatRig|Hit.001`) — `ModelImporter.clipAnimations` 의 `name` 만 바꾸고 `takeName` 은 두며 반복 클립은 `loopTime`. ② `bake_space_transform` 은 메시 · 정적 루트의 X 270° 만 없애고 뼈대 오브젝트 X 270° 는 남는다 — 굽힘은 두 변형이 같으니 `_bst` 하나만 내보낸다(`bakeAxisConversion` 은 시험 안 함). ③ 팔레트는 Point · 밉맵 끔 · 비압축 · Clamp, FBX 머티리얼은 `AddRemap` 으로 하나를 공유, 프리미티브는 UV 를 셀 중심으로 모은 메시 사본(`island.asset`). ④ 녹화는 `SampleAnimation` + 카메라 렌더 — 스킨 메시는 `forceMatrixRecalculationPerRender` 를 켠다(Sonnet 세션에서 날개가 안 움직임을 재현, Opus 는 미재현 · 원인 미확인). ⑤ `NewScene` 이 `ProjectSettings/SceneTemplateSettings.json` 을 만든다 — `DEF-M01` 이 취급을 정한다. ⑥ asmdef `Defense.Editor` 가 `UnityEditor.Editor` 를 가린다(`: Editor` 상속 CS0118) · 고위험 패턴 `Editor/*Build*` 에 `*Builder*` 가 걸릴 수 있다 · Blender 출력 소문자 이름 ↔ §17 PascalCase · 빌더로 씬을 통째 다시 만들면 diff 를 못 읽는다. 전체는 P03 [비교표](../z.completed/P03_CLI_환경테스트/03_작업기록/비교표_20261101.md) 5절. 샘플 모델을 본편에 쓸지는 `DEF-M03` D-nn → 기획서(지금 9절은 Quaternius 1순위). P00 의 첫 확인은 [`../z.completed/P00_환경_체계_로깅/NOTES.md`](../z.completed/P00_환경_체계_로깅/NOTES.md) 「현재 상태」 Blender 행. 실시간 공동 작업용 공식 MCP 는 보류 H-07(P00 H-03). **매끈한 모델 시험은 P04**(2026-11-02 등재 — 서브디비전 매끈 판 · 해골 궁수 · 좀비 · Lit · Unlit · 셀 캡처): 결과가 나오면 「샘플 모델을 본편에 쓸지」와 기획서 9절 모델 · 셰이딩 결정의 근거가 된다 — [`../P04_매끈_모델_시험/README.md`](../P04_매끈_모델_시험/README.md).

## 현재 상태 (덮어쓰기)

_갱신: 2026-10-30_

| 항목 | 상태 |
|---|---|
| 검토 | 검토서 2026-10-29 ✔(2026-10-30 추기) |
| 결정 | D-01~D-11. 미결 없음 |
| 기획 | `Defense.Design/기획서.md` v0.4 ✔ · 목업 v1 ✔ 사용자 확인(비공개 링크 — 목업 README) |
| 계획 | 계획서 1차 2026-10-30(설계 단계 확정 · 구현 단계 윤곽) — 승인 대기. 지시서 S1 · S2 |
| 저장소 변경 | `Defense.Planning` `main` · `Defense.Design` `main`(신설) — 해시는 작업색인 |
| 환경 | Unity 미설치 — P00 |

## 사용자 대기 (덮어쓰기)

- 계획서 1차 · 지시서 S1 승인.

---

## 함정 · 주의 (누적)

- 계획서 없이 대화로만 진행하면 `02_계획/` 이 비어 진행 흐름이 문서로 안 보인다(사용자 2026-10-30 지적). 설계 단계도 계획서를 먼저 쓰고 남은 일은 지시서로 연다. 이미 끝낸 일의 지시서를 뒤늦게 만들지는 않는다 — 그 기록은 결정기록 · 작업색인 · NOTES 에 있다.
- 목업 HTML 은 claude.ai 페이지 규격(문서 뼈대 태그 없이 본문부터)이다. 확인 스크린샷은 뼈대로 감싼 사본으로 찍어야 공개 때와 같은 표준 모드가 된다.
- 기획을 고칠 때 검토서를 고치지 않는다 — 정본은 `Defense.Design/기획서.md`, 검토서는 2026-10-29 시점 기록(추기만). 순서는 결정기록 D-nn → 기획서(X-02).
- DOTween 무료판 · Asset Store 트윈 · UI 팩은 EULA 라 공개 저장소에 못 올린다(G-02). 트윈은 직접 작성하거나 MIT 패키지(UPM git · OpenUPM)로.

## 발견 로그 (누적, 최신 위)

- 2026-10-30 — 헤드리스 Chrome(`--headless=new --use-angle=swiftshader --enable-unsafe-swiftshader`, 별도 `--user-data-dir`)으로 three.js 목업을 찍을 수 있다. 창 최소 너비가 약 500px 라 430px 로 지정하면 오른쪽이 잘리고, `--virtual-time-budget` 에서는 프레임이 적어 프레임당 시간 상한(0.05초)을 둔 게임 시계가 덜 간다. ✔
- 2026-10-30 — Supercent 제목은 쉬운 영어 두 단어 + 느낌표(「Burger Please!」 · 「Pizza Ready!」 · 「Outlet Rush」)이고, 한국 스토어 이름은 발음 그대로다(App Store 한국 「버거 플리즈!」). 제목 후보 8개의 이름 겹침을 웹 검색(standard)으로 확인 — 「Tower Pop!」은 App Store 동명 퍼즐이라 철회. ✔
- 2026-10-30 — 「The Tower — Idle Tower Defense」는 판 안 Cash(능력치 강화, 죽으면 초기화) · 판 밖 Coins(Workshop 영구 강화) 구조다(팬 위키 · 가이드 △). 판 안 골드 능력치 버튼을 뺀 근거(D-09).
- 2026-10-29 — 레퍼런스 3종 중 처치 · 성장 루프는 XP 히어로, 「돈 내고 올리기」 손맛은 피자 레디 · 버거 플리즈(`_공통/조사/Supercent_스타일보드.md` 2절). 두 축을 「드래프트 + 슬롯 건설」로 나눠 설계했다(검토서 4.3).

## 미해결 (누적)

- 성능 목표(적 300 · 중급 Android 60fps)는 측정 전 목표 — `DEF-M04` 실기기 측정.
- WebGL 게시처는 세 게임 공통 — `_공통` Q-05.
- 제목 「Lantern Rush!」의 Google Play · App Store 직접 검색 · 상표 확인 — `DEF-M05` 공개 전.
