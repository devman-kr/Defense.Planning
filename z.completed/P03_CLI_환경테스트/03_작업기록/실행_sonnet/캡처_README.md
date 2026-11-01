---
id: 20261031-captures-p03-sonnet
title: P03 S1 캡처 대응표 — Sonnet 5.5 샘플 씬 렌더 · 캡처 · 녹화
summary: P03 S1(Sonnet 5.5)이 만든 Blender 렌더 7장 · Unity CLI 정지 캡처 2장 · 프레임 48장 · sample_48f_24fps.mp4 와 날갯짓 수정 전 판의 원본 · 내용 · git 사본(없음), 근거 파일을 잇는 대응표다.
doc_type: register
status: final
lifecycle: living
created: 2026-10-31
updated: 2026-10-31
work_unit: P03
---
# P03 S1 캡처 대응표 — Sonnet 5.5 (2026-10-31)

Planning P03 지시서 `20261031-p03-handoff-s1s2-exec` 를 Sonnet 5.5 세션이 worktree `z.tmp/wt/p03-sonnet`(브랜치 `p03/exec-sonnet`, 시작 `763866b`)에서 수행하며 만든 파일이다. 전부 git 밖이고 git 사본은 없다. 캡처 · 렌더는 열어 보고 게임 장면 말고 비밀값 · 다른 앱 정보가 없음을 확인했다. SHA-256 은 앞 16자다. 프레임 · MP4 는 박쥐 날갯짓이 렌더에 나오지 않던 첫 판을 센서 반론으로 찾아 고친 뒤의 판이고(커밋 `d4ba361`), 첫 판은 `_before_fix/` 에 근거로 남겼다.

## 정지 캡처 · 녹화 — Unity 샘플 씬 `Assets/00_Scenes/P03_CLI_Sample.unity`(`_bst` 변형)

| 원본 | 내용 | git 사본 |
|---|---|---|
| `capture_portrait_1080x1920.png` | CLI `capture game_view --source camera`(소스 `camera:Main Camera`)로 찍은 세로 정지 캡처. 섬 · 등불 탑 · 슬라임 8 · 박쥐 4가 모두 보인다. 649,459 바이트, `2dca3c7227472062` | 없음 |
| `capture_landscape_1920x1080.png` | 같은 카메라의 가로 정지 캡처. 303,165 바이트, `c4243f60e7ff2f08` | 없음 |
| `frames/frame_000.png` ~ `frame_047.png` | 클립을 시간으로 샘플링해(`AnimationClip.SampleAnimation`, 렌더마다 스킨 행렬 재계산) 그린 48프레임, 720×1280, 24 fps 기준. 해시가 48장 모두 다르고 박쥐 날개가 프레임마다 움직인다(11프레임 주기). 약 15 MB | 없음 |
| `sample_48f_24fps.mp4` | 위 프레임을 Blender 내장 ffmpeg(VSE 이미지 스트립 → FFMPEG · MPEG4 · H264)로 인코딩. 720×1280, 24 fps, 251,437 바이트, `a4656e1aa658f1c2`. Blender 로 다시 읽어 프레임 수 48 · 일곱 프레임 순번 일치 | 없음 |
| `_before_fix/frames/` · `_before_fix/sample_48f_24fps.mp4` | 수정 전(첫 판) 프레임 48장과 MP4(179,232 바이트, `f0da1a4980044b58`). 박쥐 날개가 움직이지 않는다 — 센서 지적 P03.S1.UNI.01 의 근거로만 둔다. 프레임 000 만 수정 후와 같다 | 없음 |

## Blender 렌더 — `Tools/Blender/make_enemies.py`(수정 뒤 정식 실행)

| 원본 | 내용 | git 사본 |
|---|---|---|
| `render_lineup.png` | 슬라임 · 박쥐 · 등불 탑 라인업, 960×540. 박쥐 날개가 어두운 보라(팔레트 셀 6). `bb149d2a8a4723a6` | 없음 |
| `render_bat_Flap_f01.png` | 박쥐 Flap 1프레임(위), 정면 카메라 480×480. 좌우 날개가 대칭으로 올라간 V. `1ebf4ae85b96b4bd` | 없음 |
| `render_bat_Flap_f06.png` | 박쥐 Flap 6프레임(아래), 정면 카메라 480×480. 좌우 날개가 내려간 역V. `b708b8f3c55008ee` | 없음 |
| `render_slime_Idle_f12.png` | 슬라임 Idle 12프레임. `6545826d228dfc2d` | 없음 |
| `render_slime_Hop_f08.png` | 슬라임 Hop 8프레임. `6c17448f67de25cc` | 없음 |
| `render_slime_Hit_f03.png` | 슬라임 Hit 3프레임. `002b443b34f70ba2` | 없음 |
| `render_slime_Die_f18.png` | 슬라임 Die 18프레임. `7640cffd097b544b` | 없음 |

## 근거 파일 — `evidence/`

| 원본 | 내용 | git 사본 |
|---|---|---|
| `evidence/P03_RESULT.json` | 최종 Blender 실행의 표준 출력 `P03_RESULT` 줄(접두를 뗀 JSON). `models.bat.uv_layers` · `wing_uv` · `flap_wing_tip` 포함 | 없음 |
| `evidence/unity_import_report.json` · `evidence/import_report_round2.json` | `P03Runner.ImportModels()` 결과 — 모델 6개의 클립 이름(벗기기 전 · 후) · 루트 회전 · 스케일 · 뼈 수 · 월드 크기. 앞은 1차 실행, 뒤는 센서 지적 반영 뒤 설정된 프로젝트에서 재실행한 값(이름 집합 동일, 정렬됨) | 없음 |
| `evidence/unity_clip_probe.txt` | 클립을 샘플링한 정점 높이(Unity 두 변형)와 임포터의 클립 설정(loopTime · 프레임 범위). 진단 출력을 옮긴 것 | 없음 |
| `evidence/P03Diag.cs` | 위 진단을 낸 일회용 C#(`unity command script run --file`로 실행, 저장소에 넣지 않음) | 없음 |
| `evidence/diag_bat_blender.py` · `diag_fbx_blender.py` · `diag_bat_before_fix_output.json` · `diag_fbx_before_fix_output.json` | 날개 UV 레이어와 날갯짓 높이를 Blender 에서 확인한 일회용 진단과 수정 전 스크립트가 만든 `.blend` · FBX 에 대한 출력 | 없음 |
| `evidence/scene_hierarchy.json` | `unity command scene get_hierarchy` 결과(루트 6, 오브젝트 71) | 없음 |
| `evidence/bat_wing_motion.py` · `bat_wing_motion_before_fix.json` · `bat_wing_motion_after_fix.json` | 박쥐 네 마리의 보라 픽셀 경계 상자 · 면적을 프레임 0~23 에서 잰 것. 수정 전 y 변동 1~2 px · 면적 0.6~1.7%, 수정 후 11~26 px · 9~14% | 없음 |
| `evidence/frame_change_counts.py` · `frame_change_counts_before_fix.json` · `frame_change_counts_after_fix.json` | 프레임 000 대비 · 직전 프레임 대비 변화 픽셀 수. 수정 전 직전 대비 3,019~5,090, 수정 후 6,446~10,655(동일 프레임 0장) | 없음 |
| `evidence/bat_wing_before_after_strip.png` · `evidence/make_strip.py` | 왼쪽 박쥐(Bat_04)를 프레임 0 · 3 · 6 · 9 에서 잘라 3배 확대한 비교 이미지. 위 줄 수정 전, 아래 줄 수정 후 | 없음 |
| `evidence/mp4_verify.txt` · `evidence/mp4_verify_before_fix.txt` · `evidence/verify_mp4.py` · `evidence/verify_mp4_order.py` | Blender 로 MP4 일곱 프레임을 디코딩해 원본 프레임과 대조한 결과(평균 색 차이 0.0027, 순번 일곱 모두 일치)와 그 일회용 스크립트. 앞은 수정 후, 뒤는 수정 전 MP4 | 없음 |
| `evidence/timings.txt` · `evidence/encode_stdout.txt` · `evidence/encode_stdout_after_fix.txt` | 단계별 벽시계 초 기록(첫 컴파일 줄 `compile_scripts_sec=0.1` 은 측정창을 놓친 값이라 쓰지 않는다) · MP4 인코딩 표준 출력(처음 · 수정 뒤) | 없음 |
| `encode_mp4.py` | Blender 로 프레임을 MP4 로 만드는 일회용 스크립트(Blender 5.x 는 `image_settings.media_type = 'VIDEO'` 가 먼저 필요). 저장소 허용 영역 밖이라 넣지 않았다 | 없음 |
