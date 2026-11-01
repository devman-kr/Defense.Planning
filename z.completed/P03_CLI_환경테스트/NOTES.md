---
id: 20261031-p03-notes
title: NOTES — P03 작업 메모
summary: P03 세션 인계 메모 — 2026-11-01 종결 상태(Opus 브랜치 머지 39266b4 · 비교표), 미실측 5 가 어떻게 닫혔는지, 비교 실험의 격리 함정, 발견 로그(캡처 경로 · 스킨 행렬 · 토큰 집계 부풀림).
doc_type: note
status: final
lifecycle: living
created: 2026-10-31
updated: 2026-11-01
work_unit: P03
---
# NOTES — P03 작업 메모

세션이 작업하면서 **다음 세션이 알아야 할 것**을 적는 곳이다. 과제 지도는 [`README.md`](README.md), 결정은 [`결정기록.md`](결정기록.md), 여러 과제에 걸치는 메모는 [`../../NOTES.md`](../../NOTES.md).

**쓰는 법**: 위 세 절은 덮어쓰기(세션 끝에 갱신), 아래 절은 누적(새 항목 위에). 한 줄에 하나, 근거(파일:줄 · 명령 · 실측)를 붙인다. 추정은 **[추정]**, 에이전트 보고를 옮긴 것은 **△**. 비밀값 금지.

---

## 다음 세션 시작 전 확인 (덮어쓰기)

_갱신: 2026-11-01 — 세션 a3a90bb0(Fable 5.1) S3: 두 브랜치 검산 · 비교표 · 사용자 선택(Opus) · 머지 `39266b4` · `CLAUDE.md` 캡처 줄 · 기록 이관 · `DEF-M03` 메모 · 지표 · 종결. 그 전 2026-10-31 같은 세션: 등재 · D-01~D-10 · S0 · 지시서; S1 Sonnet 5.5(세션 0a5dd05e) · S2 Opus 5.5(세션 3aa03a8d) 실행_

1. **종결(2026-11-01)** — 이 과제에서 더 할 일은 없다. 이어지는 일은 `DEF-M03`(아트) 계획 때 P01 NOTES 4번 메모와 [비교표](03_작업기록/비교표_20261101.md) 5절을 읽는 것.
2. **머지된 것**(`Defense.Unity` `main` `39266b4`, S2 Opus 5.5): `Assets/00_Scenes/P03_CLI_Sample.unity` · `Assets/10_Scripts/Editor/P03/`(`P03ModelImport` · `P03SampleSceneBuilder` · `P03FrameRecorder`, asmdef `Defense.Editor`) · `Assets/30_Assets/Models/P03_CLI/`(FBX 6 · 팔레트 · `palette.mat` · `island.asset`) · `Tools/Blender/make_enemies.py` 수정 · 작업 보고 · 센서 기록. 안 쓰게 되면 폴더 단위로 지운다(D-02).
3. **미실측 5 는 이렇게 닫혔다**: ① 창 없는 에디터 `capture game_view --source camera` — 된다(두 세션, 한 장 0.3초, `--save_path` 는 `Assets/` 기준) ② 클론 `Library/` — 다른 경로에서 바로 열림 12~15초 ③ Blender ffmpeg MP4 — 된다(`media_type = 'VIDEO'` 먼저, 48프레임 251 KB · 180 KB) ④ `bake_space_transform` — 메시 · 정적 루트만 0°, 뼈대 오브젝트 X 270° 는 남음, 굽힘은 같음 ⑤ `clipAnimations` — `takeName` 두고 `name` 만 바꾸면 접두 · `.001` 이 벗겨진다.
4. **도구 버그** — `_도구/센서기록_추출.py` 새 토큰 2.0~3.6배 부풀림(두 세션 독립 확인) → P01 보류 H-05 ④. P00 · P03 지표 행의 새 토큰은 그 값이라 고친 뒤 다시 센다.
5. 번들 `z.tmp/p03_results/<모델>/exec-<모델>.bundle` 과 캡처 `z.captures/20261031/<모델>/` 은 git 밖에 남아 있다 — 작업 공간 정리 때 지워도 된다(비교표 · Planning 사본 · `main` 이 정본).

## 현재 상태 (덮어쓰기)

_갱신: 2026-11-01_

| 항목 | 상태 |
|---|---|
| 검토 | 검토서 2026-10-31 ✔ |
| 결정 | D-01~D-11 ✔ · 미결 없음 · 사용자 확인(D-08) ✔ 「봤고 둘 다 괜찮다」 |
| 계획 | 계획서 ✔ · 지시서 S1·S2 · S3 `_old/` |
| S0 | ✔ `763866b`(시작 커밋) |
| S1 · S2 | ✔ 둘 다 성공 기준 8 · 게이트 통과(판정 세션 재실행 포함) · `p03/exec-sonnet` 번들 보관 뒤 삭제 · `p03/exec-opus` 머지 뒤 삭제 |
| S3 | ✔ 비교표 · 머지 `39266b4` · 머지 뒤 닫힘 게이트 2/2 · 경고 0 · `CLAUDE.md` 캡처 줄(정본 = 사본) · 기록 이관 · `DEF-M03` 메모 · H-05 ④ · 지표 한 행 · `z.completed/` |
| 저장소 변경 | `Defense.Unity` `main`(S0 3 + S2 4 + 머지 1 + S3 문서 1 — 미푸시) · `Defense.Planning` `main`(등재 · 계획 · 종결 — 미푸시) |
| 환경 | Unity 6000.3.27f1 · Unity CLI 1.0.0-beta.13 · pipeline 0.9.1 · Blender 5.2.3 · 에디터 꺼짐 |

## 사용자 대기 (덮어쓰기)

- 푸시 허락(세션 끝 질문) — `Defense.Unity` · `Defense.Planning` · `Defense.Logs`.

---

## 함정 · 주의 (누적)

- **비교 실험의 격리는 사용자 손 절차에 기대지 않는다** — (b) 번들 · 삭제를 건너뛰어 S2 동안 S1 브랜치 · worktree 가 보였다(접근 흔적은 없음). 다음에는 지시서가 `git worktree list` · `git branch` 를 금지하는 것으로 충분했지만, 격리를 세게 하려면 S1 뒤 판정 세션이 (b) 를 한다.
- **루트 `CLAUDE.md` 「세션 시작」 1번(Planning README · NOTES 읽기)이 지시서의 「Planning 은 이 지시서 말고 열지 않는다」와 부딪힌다** — S1 이 README 를 읽고 보고에 적었다. 격리 실행 지시서는 첫 줄에 「루트 CLAUDE.md 세션 시작 1~2번은 건너뛴다」를 넣는다.
- **`센서기록_추출.py` 토큰 부풀림**(H-05 ④) — 고치기 전까지 지표의 새 토큰은 상대 비교에만 쓴다.
- 한 기기(G-01) — Blender(약 0.4 GB) 와 에디터를 같이 띄우지 않는다. 동영상 인코딩(Blender)은 에디터를 끈 뒤.
- `bpy` 스크립트를 공개 저장소에 두면 그 폴더가 GPL-3.0-or-later(G-17) — `Tools/Blender/` 만.
- 기획서 9절은 적 모델을 Quaternius 1순위로 적었다 — P03 은 기획서를 고치지 않았다(시험). 본편에 쓰면 `DEF-M03` D-nn → 기획서.
- `EditorSceneManager.NewScene` 이 `ProjectSettings/SceneTemplateSettings.json` 을 만든다 — 두 세션 모두 지웠다. `DEF-M01` 이 취급을 정한다.

## 발견 로그 (누적, 최신 위)

- 2026-11-01 — 판정 검산: 두 MP4 모두 48프레임 · 24 fps · 720×1280(Blender 재읽기), 두 worktree 닫힘 게이트 2/2 · 경고 0, 씬 YAML 의 오브젝트 수 · 이름이 두 보고와 같음(71 · 72), `.meta` 의 클립 `takeName` · `name` · `loopTime` 여섯 모델 동일, 커밋 트레일러 모델 이름 맞음. 보고와 실제가 다른 곳은 Opus 보고의 리뷰 토큰(2.3배 — S3 가 정정)뿐. ✔
- 2026-11-01 — 두 세션이 독립적으로 같은 판정: 「날갯짓 회전축 결함」은 결함이 아니라 S0 렌더의 사선 카메라 원근 착시(두 날개 끝 높이 0.444/0.444 · Unity `BakeMesh` 도 같음). 회전 코드는 둘 다 안 고쳤다. ✔
- 2026-11-01 — Sonnet 세션에서 한 에디터 프레임 안 `SampleAnimation` → `Camera.Render` 되풀이 때 자식 뼈 회전이 첫 포즈에 머무는 현상 재현(날개 경계 상자 y 1~2 px) · `forceMatrixRecalculationPerRender` 로 해결(11~26 px). Opus 세션의 같은 구조 녹화에서는 미재현(픽셀 차 1,710 px) — 원인 차이 미확인. ✔(사본 그림 `z.captures/20261031/sonnet/evidence/bat_wing_before_after_strip.png`)
- 2026-11-01 — `capture game_view --save_path` 는 `Assets/` 기준 — `Temp/x.png` 도 `Assets/Temp/x.png` 로 가져와지고 프로젝트 밖 · `..` 는 400 거부. 두 세션 모두 「찍고 옮기고 `DeleteAsset`」로 해결. ✔
- 2026-10-31 — Blender 5.2.3 창 없이 `make_enemies.py` 한 번에 5.35초 · 최대 RSS 417 MB — 모델 3 · 동작 6 · FBX 6 · EEVEE 렌더 7장(4.28초) · 재임포트 클립 4. P00 D-09 스모크 방식(`keyframe_insert` 로 동작 자동 생성 · 슬롯 지정 · NLA 트랙 뮤트 · `bake_anim_use_all_actions`)이 그대로 산다. ✔
- 2026-10-31 — 렌더 결함 둘(파이프라인 아님 · 스크립트 수치): 박쥐 날개가 팔레트 셀 6(보라)이 아니라 초록 — 원인은 bmesh `uv.verify()` 가 만든 층 이름 `Float2`(S1 · S2 확인). 날갯짓 회전축 — 결함 아님(위). 슬라임 · 탑은 의도대로. ✔
- 2026-10-31 — Blender 가 자기 FBX 를 다시 읽으면 클립 이름이 `SlimeRig|SlimeRig|Idle`(뼈대 이름 두 번). Unity 는 `SlimeRig|Idle`(한 번 — S1 · S2 실측). 뼈 이름을 모델마다 다르게(`SlimeRoot` · `BatRoot`) 두어 `bake_anim_use_all_actions` 가 다른 모델의 동작을 섞어 내보내지 않게 했다. 동작 이름이 같으면(`Hit`) Blender 가 `.001` 을 붙인다. ✔
- 2026-10-31 — `com.unity.pipeline` 0.9.1 명령 목록(`Runtime/Common/CommandNames.cs`): `capture game_view`(source camera · screen, `save_path`, 1280×720 기본 · 4096 상한) · `capture scene_view` · `script run --file`(프로젝트 밖 `.cs` 도 메모리 컴파일) · `scene` · `gameobject` · `asset` · `material` · `prefab` · `animation.animator` · `animation.clip` · `editor.playmode` · `wait_for --capture` · `job batch`. ✔
- 2026-10-31 — `Defense.Unity` → `z.tmp/p03/unity/` APFS 클론 `cp -c -R` 7.5초(8.9 GB, 실제 공간 거의 0). 인코더: ffmpeg · ImageMagick · gifsicle · PIL 없음, Blender `bpy.app.ffmpeg.supported` 참(codec H264 · AV1 · WEBM …, format MPEG4 · MKV · WEBM …). ✔

## 미해결 (누적)

- ~~창 없는 에디터의 카메라 렌더 캡처 가능 여부~~ → 된다(2026-10-31 두 세션). 플레이 모드 `source=screen` 캡처는 범위 밖이라 시험하지 않았다 — `DEF-M05` 전에.
- ~~샘플 에셋을 들일지~~ → 저장소에 들어갔다(D-02 · 머지 `39266b4`). 본편 사용은 `DEF-M03`.
- 스킨 행렬 갱신 현상이 Sonnet 쪽 녹화에서만 재현된 원인 — `DEF-M03` 녹화 도구를 만들 때 플래그를 기본으로 켜고 넘어간다.
