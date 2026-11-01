---
id: 20261031-p03-s1-sample-scene-sonnet
title: P03 S1 실행(Sonnet 5.5) — 박쥐 날개 결함 수정 · FBX 가져오기 · 샘플 씬 · 캡처 2 · 48프레임 MP4
summary: make_enemies.py 의 박쥐 날개 UV 레이어(Float2) 결함을 고치고 FBX 6개를 가져와 P03_CLI_Sample.unity 를 만들어 CLI 캡처 2장과 날갯짓이 나오는 sample_48f_24fps.mp4 를 냈다. 함정 둘 실측값과 센서 1 · 2라운드 처리를 담는다.
doc_type: work_report
status: final
lifecycle: static
created: 2026-10-31
updated: 2026-11-01
work_unit: P03
work_type: create
commits: [7d0c8ef, 546f586, 94591e2, d4ba361]
implements: [20261031-p03-handoff-s1s2-exec]
---

# P03 S1 실행(Sonnet 5.5) — 박쥐 날개 결함 수정 · FBX 가져오기 · 샘플 씬 · 캡처 2 · 48프레임 MP4 — Defense.Unity

## 기본 정보

| 항목 | 내용 |
|------|------|
| 작업일 | 2026-10-31 (Mac M5 16 GB, Claude Sonnet 5.5 — Planning P03 실행 세션 S1) |
| 근거 | Planning P03 [지시서 S1 · S2](../../02_계획/지시서/_old/20261031_S1S2_Unity_P03_실행.md) — Sonnet 5.5 · Opus 5.5 가 같은 본문으로 따로 수행하는 비교 실험의 한쪽. worktree `z.tmp/wt/p03-sonnet`, 브랜치 `p03/exec-sonnet`, 시작 `763866b` |
| 위험 등급 | 저 — 에디터 전용 스크립트(asmdef `includePlatforms: Editor`) · 시험 씬 · 샘플 에셋 · `Tools/Blender/` 스크립트. 고위험 경로(`ProjectSettings/` · `Packages/` · 저장 · 재화) 변경 없음(센서 A 도 같은 판정). 되돌리는 법은 브랜치 삭제 |
| 증거 ① 게이트 | 마지막 수정(`d4ba361`) 직전 에디터 닫힘 `unity test . --mode EditMode --output Logs/editmode-results.xml --timeout 900 -- -logFile Logs/gate-editmode.log` → 종료 0 · 6.1초 · `grep -cE 'warning CS\|error CS'` 가 `Logs/gate-editmode.log` 0 · `Logs/editor-headless-round3.log`(그 세션의 컴파일) 0 · `editmode-results.xml` `result="Passed" total="2" passed="2" failed="0"`. 에디터 열림 동안 `console status` `groundTruth` `compilationFailed:false` `consoleErrors:0` `consoleWarnings:0` · `test run --mode editor` `Total 2 Passed 2 Failed 0`. 같은 게이트를 커밋마다 돌렸다(닫힘 6.7 · 6.6 · 6.1초) |
| 증거 ② 상태 | 커밋 직전 `git status --short` → 미추적 둘(이 보고서 · `코드리뷰_sonnet/`)뿐. 보고 커밋 뒤 빈 출력 · 에디터 · Blender 프로세스 없음(3절 「마무리 점검」) |
| 증거 ③ 캡처 | `z.captures/20261031/sonnet/capture_portrait_1080x1920.png` · `capture_landscape_1920x1080.png` · `sample_48f_24fps.mp4`(251,437 바이트, Blender 로 다시 읽어 프레임 수 48 · 일곱 프레임 순번 일치 · 평균 색 차이 0.0027) — 파일을 열어 섬 · 탑 · 슬라임 8 · 박쥐 4 확인 ✔. 박쥐 날갯짓은 경계 상자 · 면적 변동 실측과 확대 비교 이미지로 확인 ✔(`evidence/bat_wing_before_after_strip.png`). 확인 안 한 것은 6절. 확인 페이지 [claude.ai 비공개](https://claude.ai/artifact/EX4vYAbprcfxuCUfzE6wky) |

## 1. 바꾼 것

| 커밋 | 무엇 | 전 | 후 |
|---|---|---|---|
| `7d0c8ef` | `Tools/Blender/make_enemies.py`(+40 −4) | 박쥐 날개 면이 UV 레이어 `UVMap` 의 (0,0) = 셀 0(슬라임 초록)을 가리킴. 박쥐 포즈 렌더는 +X 쪽 비스듬한 카메라 | `set_cell` 이 UV 레이어를 `UVMap` 하나로 맞춤(날개 UV 가 셀 6 중심 (0.625, 0.375)). `P03_RESULT` 에 `bat.uv_layers` · `wing_uv` · `wing_cell_center` · `flap_wing_tip` 추가. 박쥐 포즈 렌더만 정면 카메라 |
| `546f586` | Unity 쪽 42파일(+3,535) | `Assets/00_Scenes` · `Assets/30_Assets` 비어 있음, `Assets/10_Scripts/Editor` 없음 | `Assets/10_Scripts/Editor/Defense.Editor.asmdef` + `Editor/P03/` C# 8개(`P03Paths` · `P03ClipNames` · `P03ModelInfo` · `P03Measure` · `P03ModelImporter` · `P03SceneBuilder` · `P03Capture` · `P03Runner`) · `Assets/30_Assets/Models/P03_CLI/` FBX 6 · `palette.png` · `palette.mat` · `grass.mat` · `Assets/00_Scenes/P03_CLI_Sample.unity`(+ `.meta` 짝 전부) |
| `94591e2` | 센서 1라운드 반영(4파일 +52 −17) | `ImportModels` 의 「벗기기 전」 클립 이름이 설정이 바꾼 이름에서 읽힘. `DumpFrames` 가 `BuildScene` 과 따로 `baked` 인자를 받음. `new[]` | `P03Measure.TakeNames`(`defaultClipAnimations` 의 `takeName`)로 읽고 이름 목록을 정렬 — 재실행 JSON 이 바이트까지 같다. `DumpFrames(directory)` 가 각 인스턴스가 온 FBX 에서 클립을 찾음(`PrefabUtility.GetPrefabAssetPathOfNearestInstanceRoot`). `new bool[]` (UNI.02 · 03 · 08) |
| `d4ba361` | 판정 반론 반영(4파일 +40 −11) | 프레임에서 박쥐 날개가 움직이지 않음. 섬 머티리얼 `grass.mat` | `DumpFrames` 가 렌더 전에 `SkinnedMeshRenderer.forceMatrixRecalculationPerRender` 를 켜고 끝나면 되돌림. 섬 머티리얼 `Grass.mat`(GUID 유지, §17 PascalCase). 프레임 48장 · MP4 를 다시 만듦(UNI.01 · 09) |

**날개 결함 둘의 진단(✔ 직접 확인).**
- 결함 1 — 박쥐 메시 UV 레이어가 둘(`UVMap` · `Float2`). Blender 5.2 에서 bmesh `layers.uv.verify()` 가 UV 없는 메시에 만드는 레이어 이름이 `Float2` 라서 프리미티브(`UVMap`)와 `join` 할 때 갈라졌다. 날개 면의 `UVMap` 값 (0,0), `Float2` 값 (0.625, 0.375) 을 진단 스크립트로 읽었다(`evidence/diag_bat_blender.py` · 출력 `diag_bat_before_fix_output.json`).
- 결함 2 — 시작판 코드에서 재현되지 않았다. `rot_about_world` 가 이미 뼈 기준 축으로 옮겨 두 날개를 몸의 앞뒤 축(월드 Y)으로 돌린다. 진단 값: 위 f1 에서 두 날개 정점의 최고 높이 0.467 · 0.467, 아래 f6 에서 −0.139 · −0.139(아래 자세의 정점 범위는 −0.309 ~ −0.139 이고 −0.139 는 가장 높은 정점이지 날개 끝이 아니다 — 센서 UNI.05), 날개 앞뒤 폭(y −0.052~0.262) 불변, FBX 두 변형을 Blender 로 다시 읽어도 같음(`diag_fbx_before_fix_output.json`). S0 렌더(`render_bat_Flap_f01/f06.png`)에서 한쪽만 눕는 것처럼 보인 것은 카메라가 박쥐의 정면에서 +X 쪽으로 치우친 탓이다(가까운 쪽 날개는 시선 방향으로 겹쳐 가는 선으로, 먼 쪽 날개는 넓게 보인다. 날개 끝 화면 높이를 손으로 계산해 렌더와 맞는 것을 확인). 회전 계산은 건드리지 않고 박쥐 포즈 렌더만 정면 카메라로 바꿨다. 지시서의 「결함 둘」 가정과 다른 점이라 7절에도 적었다. 이 판단은 판정 반론(UNI.04)이 수락했다.

**녹화에서 날갯짓이 안 나왔던 문제(센서 UNI.01 — 내 판정을 번복).** 처음 만든 MP4(179,232 바이트)에서 박쥐 날개는 움직이지 않았다. 한 에디터 프레임 안에서 `SampleAnimation` → `camera.Render()` 를 48번 되풀이하면 스킨 행렬이 첫 포즈에 머물러, 루트 뼈의 이동 · 크기(슬라임 Hop · Idle 의 몸통, `BatRoot` ±0.03 m 흔들림)만 화면에 나오고 자식 뼈(날개) 회전은 나오지 않는다. 센서가 이것을 `blocking · plausible` 로 짚었고 나는 「프레임 PNG 48장의 해시가 모두 다르고 변화 픽셀이 수천이다」를 근거로 「틀림」으로 닫았다. 판정 반론이 반박했다 — 해시 · 변화 픽셀은 루트 뼈 움직임만으로도 생기므로 날갯짓을 증명하지 못한다. 직접 재어 보니 반론이 맞았다.

| 박쥐(보라 영역) | 날갯짓 한 주기(프레임 0~11) 동안 경계 상자 y 변동 · 면적 변동 — 수정 전 → 후 |
|---|---|
| 위(Bat_01) | 2 px · 1.7% → 11 px · 14.0% |
| 아래(Bat_03) | 1 px · 0.9% → y 끝 7 px · 9.0% |
| 왼쪽(Bat_04) | 2 px · 0.8% → 20 px · 12.9% |
| 오른쪽(Bat_02) | 2 px · 0.6% → 19 px · 12.2% |

수정 전에는 변동이 `BatRoot` 흔들림 크기(1~2 px)였고, 수정 뒤에는 날개 끝이 20 px 안팎 오르내린다. 변화 주기는 Flap 클립의 11프레임(프레임 11 = 프레임 0)이다. 확대 비교 이미지(`evidence/bat_wing_before_after_strip.png` — 위 줄 수정 전, 아래 줄 수정 후)에서도 날개가 펴지고 접힌다. 앞서 쓴 `BakeMesh` 진단은 매번 스킨을 새로 계산하므로 렌더 경로를 증명하지 못했다. 수정 전 프레임 · MP4 는 `z.captures/20261031/sonnet/_before_fix/` 에 근거로 남겼다. 근거 파일: `bat_wing_motion_before_fix.json` · `bat_wing_motion_after_fix.json` · `frame_change_counts_before_fix.json` · `frame_change_counts_after_fix.json`.

## 2. 함정 둘 실측값 (Unity 6000.3.27f1 · 기본 가져오기 직후)

**(a) 가져온 직후 클립 이름 — 벗기기 전**(✔ `evidence/unity_import_report.json` — 1차 실행값. 수정한 `ImportModels` 로 설정된 프로젝트에서 다시 돌려도 같은 이름 집합이 나왔다)

| 모델(두 변형 같음) | Unity 가 처음 읽은 이름 | 설정 뒤 |
|---|---|---|
| slime · slime_bst | `SlimeRig\|Hit` · `SlimeRig\|Hop` · `SlimeRig\|Idle` · `SlimeRig\|Die` | `Hit` · `Hop` · `Idle` · `Die` |
| bat · bat_bst | `BatRig\|Flap` · `BatRig\|Hit.001` | `Flap` · `Hit` |
| tower · tower_bst | 없음 | 없음 |

접두는 뼈대 이름 한 번이다. 박쥐 `Hit.001` 은 슬라임에도 `Hit` 가 있어 Blender 가 이름 충돌을 피하려 붙인 접미다 — 지시서가 적은 두 함정(접두 · 루트 회전) 밖의 셋째 함정이다. `P03ClipNames.Strip` 이 마지막 `\|` 뒤를 취하고 끝의 `.NNN` 도 뗀다. `clipAnimations` 를 코드로 설정한 뒤 `loopTime` 은 Idle · Hop · Flap 만 True(진단 `evidence/unity_clip_probe.txt` ✔). `asset get_import_settings` 는 `clipAnimations` 를 내지 않아(키 목록에 없음) 스크립트 출력으로 확인했다.

**(b) 변형별 루트 회전 · 스케일 · 뼈 수**(✔ 같은 파일. 모델을 씬에 세운 인스턴스에서 측정)

| FBX | 모델 루트(회전 · 스케일) | 메시 노드 | 리그 노드 → 첫 뼈 | 스킨 뼈 | Transform | 월드 크기 m |
|---|---|---|---|---|---|---|
| slime.fbx | 0° · 1 | Slime X 270.02° | SlimeRig X 270.02° → SlimeRoot X 89.98° | 2 | 5 | 1.00 × 0.80 × 1.03 |
| slime_bst.fbx | 0° · 1 | Slime 0° | SlimeRig X 270.02° → SlimeRoot X 89.98° | 2 | 5 | 1.00 × 0.80 × 1.03 |
| bat.fbx | 0° · 1 | Bat X 270.02° | BatRig X 270.02° → BatRoot X 89.98° | 3 | 6 | 1.41 × 0.66 × 0.54 |
| bat_bst.fbx | 0° · 1 | Bat 0° | BatRig X 270.02° → BatRoot X 89.98° | 3 | 6 | 1.41 × 0.66 × 0.54 |
| tower.fbx | X 270.02° · 1 | 루트가 메시 | — | 0 | 1 | 1.48 × 3.07 × 1.48 |
| tower_bst.fbx | 0° · 1 | 루트가 메시 | — | 0 | 1 | 1.48 × 3.07 × 1.48 |

스케일은 모든 노드가 1 이고 월드 크기가 Blender 미터와 맞는다. 두 변형의 차이는 메시 노드와 정적 모델 루트의 X 270° 뿐이다. 모델 정면은 두 변형 모두 Unity +Z 다(슬라임 정점 z 범위 −0.50 ~ +0.53, 눈동자 쪽이 0.53).

클립을 샘플링한 정점 높이를 Unity(`SampleAnimation` + `BakeMesh`)와 Blender 로 대조했다(✔ `evidence/unity_clip_probe.txt`). 이 대조는 클립 데이터가 두 변형에서 같다는 것의 근거이고, 화면 렌더에서 날개가 움직이는지의 근거는 아니다(1절):

| 포즈 | Blender | Unity 기본 | Unity `_bst` |
|---|---|---|---|
| 슬라임 Hop f1 · y 최소~최대 | 0.025 ~ 0.825 | 0.025 ~ 0.825 | 0.025 ~ 0.825 |
| 슬라임 Hop f13 | 0.575 ~ 1.375 | 0.575 ~ 1.375 | 0.575 ~ 1.375 |
| 슬라임 Die f18 | 0.001 ~ 0.049 | 0.002 ~ 0.050 | 0.002 ~ 0.050 |
| 박쥐 Flap f1 날개 정점 최고 높이 왼 / 오 | 0.467 / 0.467 | 0.467 / 0.467 | 0.467 / 0.467 |
| 박쥐 Flap f6 날개 정점 최고 높이 왼 / 오 | −0.139 / −0.139 | −0.139 / −0.139 | −0.139 / −0.139 |

**(c) 씬에 쓴 변형과 이유.** `_bst`(bake_space_transform 켬)를 썼다. 모델 루트와 메시 노드 회전이 0 이라 인스턴스를 놓고 돌릴 때 보정이 필요 없다(기본 변형의 탑은 루트가 X 270° 라 `Place` 가 그 회전 위에 방향을 합성해야 한다 — `P03SceneBuilder.Place`). 위 표처럼 클립 샘플링 값이 두 변형 모두 Blender 와 같았다. 다만 Blender 5.2.3 은 이 옵션 설명에 "WARNING! experimental option, use at own risk, known to be broken with armatures/animations" 라고 적어 둔다(✔ 옵션 RNA 설명문을 직접 읽음). 이번 리그(뼈 2~3 · 회전 · 이동 · 크기 키)에서는 차이가 없었지만 더 복잡한 리그의 근거가 아니다 — 8절.

## 3. 단계별 걸린 시간 · 마무리 점검

벽시계 초, Mac M5 16 GB, 에디터와 Blender 는 겹쳐 띄우지 않았다(띄우기 전 `pgrep` 로 확인). ✔ `evidence/timings.txt`.

| 단계 | 초 | 비고 |
|---|---|---|
| Blender 실행(수정판 정식) | 3.2 | 스크립트 내부 3.06(렌더 2.9). 수정 전 기준 실행도 4.4 |
| 에디터 기동(창 없음) | 14.6 | `Library/` 클론이라 재임포트 없음. 에디터 로그의 초기 에셋 새로고침 7.6 |
| 스크립트 컴파일(첫) + 도메인 리로드 | 약 20 이하 | 요청 11:43:07 → 완료 확인 11:43:27 UTC(측정창을 놓쳐 상한). 도메인 리로드 1.3(로그) |
| 재컴파일(수정 뒤) | 2.1 | |
| 가져오기 + 설정 + 실측 | 0.5 | FBX 6 · 팔레트 · 머티리얼 2 |
| 샘플 씬 생성 · 저장 | 0.6 | |
| 정지 캡처 2 | 0.5 | 세로 0.3 · 가로 0.2 |
| 프레임 48장(720×1280) | 1.4 → 1.5 | 처음 · 날갯짓 수정 뒤 |
| 에디터 끄기 | 1.2 | |
| MP4 인코딩(Blender) | 0.9 → 0.8 | 처음 · 수정 뒤. 인코딩 자체 0.35 · 0.34. 첫 시도는 `media_type` 때문에 실패(8절) |
| 게이트 — 열림 `test run` · 닫힘 `unity test` | 0.4 · 6.1~6.7 | 닫힘은 커밋마다 6.7 · 6.6 · 6.1 |

센서 지적 반영 이후(에디터 두 번 더 기동):

| 단계 | 초 | 비고 |
|---|---|---|
| 에디터 재기동(센서 지적 검증 · 날갯짓 수정 검증) | 14.9 · 15.7 | 수정한 스크립트는 기동 중에 컴파일돼 따로 요청하면 `up_to_date` |
| `ImportModels` 재실행 · 재컴파일(정렬 추가) | 0.6 · 2.1 | 재실행 JSON 이 두 번 연속 바이트 동일 |
| `DumpFrames` 재실행(시그니처 검증 · 날갯짓 수정) | 1.6 · 1.5 | 시그니처 검증의 48장이 기존과 SHA-256 전부 일치 |
| 코드 리뷰(에이전트 실행 시간) | 센서 A 25분 6초 · 반론 D 17분 26초 · 2라운드 A 15분 30초 | 둘째와 셋째는 겹쳐 돌았다 |

**세션 총계**(✔ 세션 기록 집계 — `코드리뷰_sonnet/tokens_dedup.json`, 계산 스크립트 git 밖 `evidence/token_usage.py`). 첫 지시 20:25:21 → 최종 보고 21:52:56 KST, 1시간 27분 35초(커밋 ① 20:35:42 · ② 20:50:45 · 센서 반영 21:23:50 · 날갯짓 수정 21:44:43 · 보고 21:51:50). 토큰은 고유 요청 하나를 한 번만 세고 새 토큰은 cache_creation + input + output 이다. 메인(Sonnet 5.5) 1,291,012(요청 147 · 출력 496,016) + 서브에이전트 셋(Opus 5.5) 1,126,775(요청 90 · 출력 356,933) = 2,417,787. 캐시 읽기를 더한 총합은 82,817,294(메인 73,697,307 + 서브 9,119,987). 줄마다 더하는 방식은 한 응답이 여러 줄로 기록돼 메인 3.6배 · 서브 2.0~2.3배로 부풀려지므로 쓰지 않았다.

**마무리 점검** — 에디터 · Blender 프로세스 `pgrep` 로 없음 확인. 에디터가 `NewScene` 호출로 만든 `ProjectSettings/SceneTemplateSettings.json`(기본값 목록, 미추적)은 커밋하지 않고 지웠다(센서 UNI.25 — 작업 트리에 남으면 `git add -A` 한 번으로 계약 위반 커밋이 된다). `git add` 는 모든 커밋에서 파일 이름으로만 했다. 보고 커밋 뒤 `git status --short` 는 빈 출력이다.

## 4. 코드 리뷰

위험 등급: 저(지시서 세 칸 기준 — 센서 A 도 고위험 경로 변경 없음으로 판정). 결정론 게이트: 컴파일 오류 0 · 새 경고 0 · EditMode 2 → 2 통과, 실패 증가 0 · PlayMode 없음.

| 저장소 | 범위 | 크기 | 구성 | 에이전트 · 새 토큰 · 시간 | 지적 | 고침 | 틀림 | 의도 | 범위 밖 | 처리 안 함 | 미해결 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Unity | `763866b..546f586` | 12파일 +929/−4 | 세션 센서(A opus) → 판정 반론(D opus) | 2 · 863,953 · 25분 6초 + 17분 26초 | 26 | 5 | 0 | 1 | 3 | 17 | 0 |
| Unity 2라운드 | `546f586..94591e2` | 4파일 +52/−17 | 세션 센서(A opus) | 1 · 262,822 · 15분 30초 | 5 | 0 | 0 | 0 | 0 | 5 | 0 |

새 토큰은 고유 요청 하나를 한 번만 센 값이다(cache_creation + input + output). 처음에는 추출 도구가 줄마다 더한 값(1,873,984 · 582,109)을 적었는데 한 응답이 여러 줄로 기록돼 2배 안팎으로 부풀려져 있어 정정했다(`코드리뷰_sonnet/README.md` 추기).

원본 · 처리표: `z.docs/work_reports/20261031/코드리뷰_sonnet/`(처리.md 31행 · 에이전트 표 `README.md`). `d4ba361`(반론 뒤 수정)은 3라운드 금지라 센서 재검토를 받지 않았고 실측 · 확대 비교 · 닫힘 게이트로 검증했다.

사람이 볼 행(`blocking` · `important` 이면서 `new`, 미해결, 데이터 손상 · 비밀값 — 해당 없음):

| 식별자 | 종류 · 심각도 · 기원 | 영역 | 유형 | 파일:줄 | 처리 | 근거 · 커밋 · 반론 |
|---|---|---|---|---|---|---|
| P03.S1.UNI.01 | issue · blocking · new | BUILD | 한 프레임 안에서 렌더를 되풀이할 때 스킨 메시가 갱신되지 않음 | `P03Capture.cs:59-72` | 고침 | `d4ba361`. 내가 「틀림」으로 닫았으나 반론 D 가 반박해 번복 — 1절 |
| P03.S1.UNI.02 | issue · important · new | BUILD | 「가져온 직후 이름」을 설정이 반영된 뒤의 이름에서 읽음 | `P03Runner.cs:23 · 29-37` · `P03Measure.cs:12-24` | 고침 | `94591e2` |
| P03.S1.UNI.03 | suggestion · important · new | BUILD | 같은 뜻의 인자를 두 호출에서 따로 받고 일치 여부를 검사하지 않음 | `P03Runner.cs:55-58 · 68-70` · `P03Capture.cs:56-58` | 고침 | `94591e2`(센서는 plausible, 코드 확인 뒤 고침) |
| P03.S1.UNI.04 | question · important · new | CONTRACT | 알려진 결함을 코드 수정 대신 렌더 시점만 바꿔 처리 | `make_enemies.py:435-438` | 의도 | 지시서 성공 기준 1 · 시작판 진단 · 반론 수락. 사람이 `render_bat_Flap_f01.png` · `_f06.png` 를 열어 대칭 V · 역V 를 확인하면 닫힌다 |

판정 반론: 「틀림」 1 · 「의도」 2 → UNI.01 반박(고침으로 번복) · UNI.04 수락 · UNI.09 는 palette.mat 수락 · grass.mat 반박(→ `Grass.mat`). 범위 밖 3(UNI.24 폴더 `.meta` · UNI.25 미추적 파일 — 지움 · UNI.26 `Tools/Blender/README.md` 문장 — 후속). nit 22건 처리 안 함(상한 밖 13건 포함). 종료 조건 충족, 3라운드 없음.

## 5. 성공 기준 대조

| # | 기준 | 결과 |
|---|---|---|
| 1 | Blender 다듬기 | ✔ 종료 0, 날개 셀 6, 위/아래 렌더를 열어 확인, `P03_RESULT` 는 `evidence/P03_RESULT.json` |
| 2 | 가져오기 | ✔ FBX 6 · 팔레트가 `Models/P03_CLI/`, 클립 `Idle · Hop · Hit · Die` / `Flap · Hit`, loopTime 은 Idle · Hop · Flap |
| 3 | 함정 둘 실측값 표 | ✔ 2절 |
| 4 | 샘플 씬 | ✔ `get_hierarchy` 루트 6 · 오브젝트 71(Island · LanternTower+Lantern Light · Slimes 8 · Bats 4 · Main Camera · Directional Light). 섬은 프리미티브라 팔레트 셀을 못 가리켜 단색 `Grass.mat` 을 따로 둠(7절) |
| 5 | 정지 캡처 2 | ✔ CLI `capture game_view --source camera` 로 창 없는 에디터에서 성공(`source: camera:Main Camera`). 저장 경로는 `Assets/` 아래만 받아 `Assets/Temp/` 에 찍고 옮긴 뒤 `AssetDatabase.DeleteAsset` 으로 지움. 대체 경로(카메라 → RenderTexture → PNG)는 프레임 렌더에 쓰임 |
| 6 | 녹화 | ✔ 48프레임 · 24 fps · 720×1280, 슬라임 Idle · Hop 섞음(Slime_01 · 03 · 05 · 07 Idle, 02 · 04 · 06 · 08 Hop — 개체 사이 섞기, 7절) · 개체마다 위상 · 박쥐 Flap. Blender 내장 ffmpeg 인코딩, Blender 가 다시 읽은 `frame_duration` 48. **날갯짓이 안 나오던 첫 판을 센서 반론으로 찾아 고쳤다(1절)** |
| 7 | 게이트 · 보고 · 센서 · 커밋 | ✔ 게이트 · 커밋 4(Blender 1 · Unity 1 · 센서 반영 2) + 보고 · 센서 기록 커밋 · 센서 1라운드 · 반론 · 2라운드 |
| 8 | 확인 페이지 | ✔ 기본 정보 표의 URL(날갯짓 수정 뒤 값으로 다시 게시) |

## 6. 확인하지 않은 것 · 추정한 것

- 실기기 · 플레이 모드 화면은 범위 밖이라 보지 않았다. 캡처는 편집 모드의 카메라 렌더다.
- 슬라임 Idle · Hit 클립의 정점 높이는 Blender 와 대조하지 않았다(Hop · Die · Flap 만). 박쥐 Hit 도 마찬가지. 슬라임 몸통 아래쪽 자식 뼈(`SlimeTop`) 회전이 수정 뒤 프레임에 나오는지는 따로 재지 않았다(루트 뼈 변화만 수정 전에도 보였다).
- 녹화를 사람의 눈으로 재생해 보지는 못했다. 수정 뒤 프레임은 박쥐 확대 비교(0 · 3 · 6 · 9)를 눈으로 보았고, 48장 해시가 모두 다르며, Blender 로 MP4 의 일곱 프레임(1 · 7 · 13 · 20 · 31 · 40 · 48)을 디코딩해 모두 같은 순번의 원본과 가장 가깝다는 것(평균 색 차이 0.0027 — `evidence/mp4_verify.txt` ✔)까지 확인했다. 움직임이 부드러운지는 판단하지 못했다.
- 첫 컴파일 시간은 측정창을 놓쳐 상한(약 20초 이하)으로만 적었다. 에디터 로그에는 줄 단위 시각이 없다.
- EEVEE 렌더는 같은 스크립트로 돌려도 바이트가 달라 S0 렌더와 해시로 비교하지 못했다. 슬라임 · 탑 렌더는 파일 크기(±55바이트)와 눈으로 같다고 보았다.
- [추정] `ProjectSettings/SceneTemplateSettings.json` 은 `EditorSceneManager.NewScene` 호출이 만든 것으로 보인다(첫 `BuildScene` 시각 20:46 과 파일 시각이 같다). 어느 호출인지는 가려 보지 않았다.
- `Place` 의 회전 합성(`rotation * instance.transform.rotation`)은 씬에 쓴 `_bst` 변형에서는 모델 루트가 항등이라 결과가 달라지지 않는다. 기본 변형의 탑(루트 X 270°)을 세웠을 때 방향이 맞는지는 시험하지 못했다.
- [추정] 스킨 행렬이 루트 뼈 변환만 반영한 이유(렌더 시점에 루트 뼈 행렬이 적용되고 자식 뼈 행렬은 에디터 프레임마다 한 번만 계산됨)는 실측 결과(경계 상자 · 면적)와 `forceMatrixRecalculationPerRender` 로 해결된다는 사실에서 추정했다. Unity 내부 구현은 확인하지 않았다.
- `d4ba361` 은 센서 재검토를 받지 않았다. 실측으로 날갯짓이 나오는 것은 확인했지만 그 수정 줄 자체를 리뷰어가 읽지는 않았다.

## 7. 지시서와 다른 점 · 더 나은 방법 · 범위 밖 제안

**지시서와 다른 점**
- 결함 2(날갯짓 회전축)는 시작판 코드에서 재현되지 않았다(1절). 회전 계산은 바꾸지 않았고, 박쥐 포즈 렌더만 정면 카메라로 바꿨다. 지시서 성공 기준 1 의 확인(「날갯짓이 몸을 축으로 위아래로 움직인다」)은 새 렌더와 `flap_wing_tip` 수치로 충족한다(판정 반론이 수락).
- 머티리얼이 둘이다. 팔레트 머티리얼 `palette.mat` 은 모델 셋이 하나를 공유하고(계약 충족), 섬(Unity 프리미티브 원통)은 UV 가 팔레트 셀 하나를 가리킬 수 없어 단색 `Grass.mat` 을 따로 둔다. 성공 기준 4 의 「머티리얼 하나」를 모델에 대한 말로 읽었다.
- 이름 규칙: FBX · 팔레트 텍스처는 지시서가 적은 대로 소문자(`slime.fbx` · `palette.png`)로 두어 코딩 표준 §17(PascalCase)과 다르다. `palette.mat` 은 §17 의 「같은 대상은 같은 이름」에 따라 `palette.png` 와 맞췄고, 짝이 없는 섬 머티리얼은 §17 PascalCase 대로 `Grass.mat` 으로 했다(처음 `grass.mat` 으로 만들었다가 판정 반론이 지적해 `d4ba361` 에서 바꿈).
- 성공 기준 6 의 「슬라임은 Idle · Hop 을 섞고」를 개체 사이 섞기(Slime_01 · 03 · 05 · 07 이 Idle, 02 · 04 · 06 · 08 이 Hop)로 읽었다. 한 개체 안에서 전환하는 것이 뜻이었다면 미달이다(센서 UNI.22).
- 세션 시작 규칙(루트 `CLAUDE.md`)에 따라 Planning 루트 `README.md` 를 지시서의 격리 조건을 읽기 전에 읽었다. P03 폴더의 다른 문서와 Planning `NOTES.md` 는 열지 않았다.
- 센서 리뷰어는 `Plan` 에이전트 유형(쓰기 도구 없음)에 모델 `opus` 로 띄웠다 — 「리뷰어에게 쓰기 권한은 쓰지 않는다」를 도구 수준에서 지키려고. 2라운드를 한 번 돌렸고 반론 뒤 수정 `d4ba361` 은 재검토 없이 두었다(3라운드 금지).
- 지시서 산출물에 없는 `z.captures/20261031/sonnet/evidence/`(측정 JSON · 진단 스크립트)와 `_before_fix/`(날갯짓이 안 나오던 첫 프레임 · MP4), `encode_mp4.py` 를 허용 영역(`z.captures/<날짜>/<모델>/`) 안에 두었다. 인코딩 스크립트는 `Tools/Blender/` 가 허용 영역 밖이라 저장소에 넣지 않았다.
- 에디터가 만든 `ProjectSettings/SceneTemplateSettings.json` 은 읽기 전용 영역이라 커밋하지 않고 지웠다.
- 센서 지적으로 `DumpFrames` 의 시그니처가 `DumpFrames(directory, baked)` 에서 `DumpFrames(directory)` 로 바뀌었다(`94591e2`).

**더 나은 방법** — 에디터 도구를 CLI 로 구동할 때 `script run --file` 보다 asmdef 안의 public 정적 진입점 + `script eval` 이 재현하기 쉽다(컴파일이 한 번이고 호출이 한 줄). 애니메이션을 렌더로 확인할 때는 정점 값(`BakeMesh`)이 아니라 렌더된 픽셀(경계 상자 · 면적 · 확대 이미지)로 잰다.

**범위 밖 제안(하지 않음)** — ① `Tools/Blender/README.md` 의 「알려진 결함 둘」 문장 갱신(허용 영역 밖). ② `ASSETS.md` 에 P03 샘플 모델(자체 제작 · 코드 생성) 행 추가. ③ `make_enemies.py` 의 `Material.use_nodes` · `World.use_nodes`(Blender 6.0 제거 예정 폐기 경고)와 `wing_tip_z` 이름(실제 뜻은 날개 정점의 최고 높이), 회귀 단언(`wing_uv == [wing_cell_center]` 를 종료 코드에 연결). ④ 슬라임 · 박쥐 Hit 이름 충돌을 Blender 에서 모델 접두로 푸는 방법(8절). ⑤ `capture` 가 `Assets/` 안만 받으므로 `Temp/` 대신 도구 전용 임시 폴더를 둘지.

## 8. 발견 — `DEF-M03` 에 넘길 것

- **스킨 메시를 한 에디터 프레임 안에서 샘플링 · 렌더할 때**: `AnimationClip.SampleAnimation` → `Camera.Render` 를 되풀이하면 스킨 행렬이 렌더마다 갱신되지 않아 루트 뼈의 이동 · 크기만 화면에 나오고 자식 뼈 회전(날개)은 첫 포즈에 머문다. `SkinnedMeshRenderer.forceMatrixRecalculationPerRender = true`(직렬화되지 않아 씬 파일은 그대로)로 해결했다. 실측: 박쥐 경계 상자 y 변동 1~2 px → 11~26 px. `BakeMesh` 로 정점 위치를 재는 진단은 이 결함을 못 잡는다 — 렌더 픽셀로 확인해야 한다.
- **Blender 5.2 bmesh**: `bm.loops.layers.uv.verify()` 는 UV 없는 메시에 `Float2` 라는 이름의 레이어를 만든다. 프리미티브(`UVMap`)와 `join` 하면 레이어가 둘로 갈라져 한쪽 면이 UV (0,0) 을 가리킨다. 이름을 명시(`get("UVMap")` · `new("UVMap")`)하고, 결과 JSON 에 `uv_layers` 를 남겨 확인한다.
- **Blender 5.x 동영상**: `image_settings.file_format = 'FFMPEG'` 를 바로 지정하면 TypeError. `image_settings.media_type = 'VIDEO'` 가 먼저다. VSE 는 `scene.sequence_editor.strips.new_image` 와 `strip.elements.append`. 720×1280 · 48프레임 H.264 MP4 가 251 KB, 인코딩 0.34초.
- **Blender 6.0**: `Material.use_nodes` · `World.use_nodes` 가 제거 예정(DeprecationWarning). `make_enemies.py` 38 · 394줄.
- **FBX 클립 이름**: 형식은 `<뼈대>|<동작>`, 같은 이름의 동작이 둘이면 Blender 가 `.001` 을 붙인다. Unity `clipAnimations` 는 `takeName` 을 두고 `name` 만 바꾸면 된다. 「벗기기 전」 이름을 측정하려면 가져온 클립 하위 에셋이 아니라 `ModelImporter.defaultClipAnimations[].takeName` 을 읽어야 설정과 무관하다. 동작 이름을 모델마다 유일하게 정하면 정리 규칙이 단순해진다.
- **`bake_space_transform`**: Blender 설명문에 실험 · 리그 파손 경고. 이 리그에서는 Unity 클립 샘플링 값이 기본 변형과 같았다(0.001 이내). 뼈가 많은 리그 · 복잡한 동작에서 기본 변형 + Unity `ModelImporter.bakeAxisConversion` 과 다시 비교할 것(이번에는 시험하지 않음).
- **머티리얼 공유**: FBX 가져오기 설정 `externalObjects` 에 `Palette`(Blender 머티리얼 이름) → `palette.mat` 을 `AddRemap` 하면 모든 FBX 인스턴스가 공유 머티리얼을 쓴다. 팔레트는 Point 필터 · 밉맵 없음 · Clamp.
- **Unity CLI(1.0.0-beta.13)**: 창 없는 에디터 기동 14.6~15.7초(키체인 대화상자 없음). `script eval` 이 asmdef 에디터 어셈블리의 public 타입을 부른다. `capture game_view --source camera` 는 창 없는 에디터에서 동작(장당 0.2~0.3초)하지만 저장 경로는 `Assets/` 아래만(`..` · 프로젝트 밖 절대 경로는 `must not contain '..'` · `outside the project root` 로 거부) — 찍은 파일이 임포트되므로 지워야 한다. FBX 6 + 팔레트 가져오기와 설정은 0.5초. 에디터가 닫힌 사이 바꾼 스크립트는 기동 중에 컴파일된다.
- **프레임 렌더**: 에디터 모드에서 `AnimationClip.SampleAnimation` 이 Generic 클립에 동작하고 씬을 dirty 로 만들지 않았다. RenderTexture(MSAA 4) 720×1280 48장에 1.5초. 렌더가 결정적이어서 같은 씬 · 같은 코드의 재실행 48장이 SHA-256 전부 일치했다. 임포트의 키프레임 감축(25~33%)이 켜진 채로 Blender 와 0.001 이내.
- **`NewScene` 부산물**: `ProjectSettings/SceneTemplateSettings.json` 이 새로 생긴다. 「`ProjectSettings/` 는 읽기 전용」과 부딪히므로 `DEF-M01` 이 이 파일의 취급(커밋 · `.gitignore`)을 정해야 한다.
- **git · macOS**: 이 저장소는 `core.ignorecase=true` 라서 에셋 이름의 대소문자만 바꾸면 git 이 내용 변경으로 보고 인덱스 경로 대소문자를 바꾸지 않는다 — `git rm --cached` 로 옛 경로를 뺀 뒤 `git add` 로 새 경로를 넣어야 이름 변경(R099 · R100)으로 기록된다. Unity 쪽은 임시 이름을 거치는 `AssetDatabase.MoveAsset` 두 번으로 GUID 를 유지한 채 바꿨다.
- **네임스페이스**: asmdef 이름 = 루트 네임스페이스 규칙으로 `Defense.Editor` 가 되면 `Defense.*` 안에서 `Editor` 가 `UnityEditor.Editor` 를 가려 `class X : Editor` 가 CS0118 이 난다(센서 UNI.19). 에디터 코드가 늘면 완전 한정 이름을 쓰거나 asmdef 이름을 다시 정해야 한다.
- **에셋 이름**: Blender 출력(소문자 `slime.fbx`)과 코딩 표준 §17(PascalCase)이 다르다 — 출력 이름 규칙을 정할 것.
