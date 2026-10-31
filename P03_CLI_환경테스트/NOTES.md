---
id: 20261031-p03-notes
title: NOTES — P03 작업 메모
summary: P03 세션 인계 메모로, 사전 확인(Blender 5.35초 · 사본 프로젝트 클론 7.5초)의 산출물 위치, 결정 대기 8개, 미실측 목록(창 없는 에디터 카메라 렌더 · 클론 Library · Blender MP4 인코딩), 발견 로그(날개 UV · 클립 이름 이중 접두)를 담는다.
doc_type: note
status: final
lifecycle: living
created: 2026-10-31
updated: 2026-10-31
work_unit: P03
---
# NOTES — P03 작업 메모

세션이 작업하면서 **다음 세션이 알아야 할 것**을 적는 곳이다. 과제 지도는 [`README.md`](README.md), 결정은 [`결정기록.md`](결정기록.md), 여러 과제에 걸치는 메모는 [`../NOTES.md`](../NOTES.md).

**쓰는 법**: 위 세 절은 덮어쓰기(세션 끝에 갱신), 아래 절은 누적(새 항목 위에). 한 줄에 하나, 근거(파일:줄 · 명령 · 실측)를 붙인다. 추정은 **[추정]**, 에이전트 보고를 옮긴 것은 **△**. 비밀값 금지.

---

## 다음 세션 시작 전 확인 (덮어쓰기)

_갱신: 2026-10-31 — 세션 a3a90bb0(Fable 5.1): P03 등재 · 검토서 · 사전 확인(Blender 한 바퀴 · 사본 프로젝트 클론). 사용자 지시로 실행은 멈추고 계획으로 — 실행은 다른 세션_

1. **지금 어느 단계**: 검토 — 결정 대기. [검토서](01_검토/검토서_20261031.md) 6절 확인 사항 8개(범위 · Unity 작업 위치 · 에셋 운명 · 캐릭터 · 녹화 형식 · 세션 구성 · 기록 위치 · 완료 기준)의 답을 기다린다. 답이 오면 `결정기록.md` D-01~ → 계획서 → 지시서(S1 Blender · S2 Unity).
2. **사전 확인 산출물(git 밖, 이 세션)**: `z.tmp/p03/blender/make_enemies.py`(사본 `z.captures/20261031/`) · `z.tmp/p03/blender_out/`(슬라임 · 박쥐 · 탑 FBX 각 2변형 `*.fbx` · `*_bst.fbx`, `palette.png` 4×4, 렌더 7장, `p03_enemies.blend`, `run1.log` — 결과 JSON 은 로그의 `P03_RESULT` 줄) · `z.tmp/p03/unity/`(`Defense.Unity` 의 APFS 클론 — `.git` · `Temp` 없음, `Library/` 8.9 GB 포함). 실행 세션은 이것을 이어 쓰거나 지우고 다시 만든다 — 둘 다 싸다(Blender 5초 · 클론 7.5초).
3. **착수 전 확인**: 에디터 · Blender 가 떠 있지 않은지(`pgrep -x Blender` · `pgrep -f 'Unity.app/Contents/MacOS/Unity'`) · 디스크(2026-10-31 295 GB 여유) · 결정 2 가 「사본」이면 `Defense.Unity` 는 읽기만.
4. **미실측(실행 세션이 닫는다)**: ① 창 없는 에디터에서 `capture game_view --source camera` 가 그림을 내는지 ② 클론한 `Library/` 로 다른 경로에서 에디터가 바로 열리는지 ③ Blender 내장 ffmpeg 로 PNG 연속 → MP4 ④ `bake_space_transform` 켠 FBX 의 Unity 루트 회전(P00 미실측 그대로) ⑤ `ModelImporter.clipAnimations` 로 `Rig|Idle` 접두 벗기기.

## 현재 상태 (덮어쓰기)

_갱신: 2026-10-31_

| 항목 | 상태 |
|---|---|
| 검토 | 검토서 2026-10-31 초안 ✔(결정 대기) |
| 결정 | 미결 1~8 |
| 계획 | 없음 — 결정 뒤 |
| 저장소 변경 | `Defense.Planning` 만(등재). `Defense.Unity` · Design · `_공통` 변경 없음 |
| 환경 | Unity 6000.3.27f1 · Unity CLI 1.0.0-beta.13 · `com.unity.pipeline` 0.9.1-exp.1 · Blender 5.2.3 LTS(내장 ffmpeg H264 · MPEG4 · WEBM) · 인코더 ffmpeg · ImageMagick · PIL 없음 · 에디터 꺼짐 · 활성 플랫폼 WebGL [추정, P00 마지막 빌드] |

## 사용자 대기 (덮어쓰기)

- 검토서 6절 확인 사항 1~8.

---

## 함정 · 주의 (누적)

- 한 기기(G-01) — Blender(약 0.4 GB) 와 에디터를 같이 띄우지 않는다. 동영상 인코딩(Blender)은 에디터를 끈 뒤.
- `bpy` 스크립트를 공개 저장소에 두면 그 폴더가 GPL-3.0-or-later(G-17) — P03 동안 git 밖(`z.tmp` · `z.captures`).
- 사본 프로젝트에서 에디터를 띄울 때 `--project-path` 를 사본 경로로 준다. `Defense.Unity` 를 연 에디터와 사본을 연 에디터를 같이 띄우지 않는다(메모리 · 혼동).
- 기획서 9절은 적 모델을 Quaternius 1순위로 적었다 — P03 은 기획서를 고치지 않는다(시험). 들이면 `DEF-M03` D-nn → 기획서.

## 발견 로그 (누적, 최신 위)

- 2026-10-31 — Blender 5.2.3 창 없이 `make_enemies.py` 한 번에 5.35초 · 최대 RSS 417 MB — 모델 3 · 동작 6 · FBX 6 · EEVEE 렌더 7장(4.28초) · 재임포트 클립 4. P00 D-09 스모크 방식(`keyframe_insert` 로 동작 자동 생성 · 슬롯 지정 · NLA 트랙 뮤트 · `bake_anim_use_all_actions`)이 그대로 산다. ✔
- 2026-10-31 — 렌더 결함 둘(파이프라인 아님 · 스크립트 수치): 박쥐 날개가 팔레트 셀 6(보라)이 아니라 초록 — `from_pydata` 메시에 `set_cell` 한 UV 가 join 뒤 0 으로 간 듯 [추정]. 날갯짓 회전축이 어색(한쪽 날개가 접힘) — 월드 Y 축을 뼈 공간으로 옮긴 `rot_about_world` 의 부호 · 축 확인 필요. 슬라임(스쿼시 · 점프 · 피격 · 납작) · 탑은 의도대로. ✔
- 2026-10-31 — Blender 가 자기 FBX 를 다시 읽으면 클립 이름이 `SlimeRig|SlimeRig|Idle`(뼈대 이름 두 번). Unity 는 P00 실측 `Rig|Idle`(한 번). 뼈 이름을 모델마다 다르게(`SlimeRoot` · `BatRoot`) 두어 `bake_anim_use_all_actions` 가 다른 모델의 동작을 섞어 내보내지 않게 했다. ✔
- 2026-10-31 — `com.unity.pipeline` 0.9.1 명령 목록(`Runtime/Common/CommandNames.cs`): `capture game_view`(source camera · screen, `save_path`, 1280×720 기본 · 4096 상한) · `capture scene_view` · `script run --file`(프로젝트 밖 `.cs` 도 메모리 컴파일) · `scene` · `gameobject` · `asset` · `material` · `prefab` · `animation.animator` · `animation.clip` · `editor.playmode` · `wait_for --capture` · `job batch`. ✔
- 2026-10-31 — `Defense.Unity` → `z.tmp/p03/unity/` APFS 클론 `cp -c -R` 7.5초(8.9 GB, 실제 공간 거의 0). 인코더: ffmpeg · ImageMagick · gifsicle · PIL 없음, Blender `bpy.app.ffmpeg.supported` 참(codec H264 · AV1 · WEBM …, format MPEG4 · MKV · WEBM …). ✔

## 미해결 (누적)

- 창 없는 에디터의 카메라 렌더 · 플레이 모드 `source=screen` 캡처 가능 여부 — 실행 세션 실측.
- 샘플 에셋을 들일지 — 결정 3 · `DEF-M03`.
