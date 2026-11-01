---
id: 20261031-p03-s1-ac5b1a74-final
title: 코드리뷰 S1 — 에이전트 ac5b1a74 최종 보고 원문
summary: 「세션 센서 — 코드 리뷰어 A(opus)」 에이전트(claude-opus-5-5 · 도구 호출 31)가 돌려준 최종 보고 원문 — 출처 SubagentHandback.
doc_type: review
status: final
lifecycle: static
created: 2026-10-31
updated: 2026-10-31
work_unit: P03
---
| # | 종류 | 심각도 | 기원 | 유형 | 파일:줄 | 실패 시나리오(입력 → 잘못된 결과) | 확신 |
|---|---|---|---|---|---|---|---|
| 1 | issue | blocking | new | 한 프레임 안에서 렌더를 되풀이할 때 스킨 메시가 갱신되지 않음 | `P03Capture.cs:59-72`(65 · 69 · 71) | `DumpFrames` 한 번의 호출(에디터 한 프레임) 안에서 `SampleAnimation` → `camera.Render()` 를 48번 되풀이한다 → `SkinnedMeshRenderer` 는 기본값(`forceMatrixRecalculationPerRender = false`)에서 스킨 행렬을 프레임마다 한 번만 계산한다. 그러면 뼈 Transform 은 바뀌어도 48장이 모두 같은 포즈일 수 있다 → MP4 가 정지 화면이어도 「Blender 로 다시 읽어 48프레임」 검사는 통과한다(성공 기준 6 의 위상 차이 · 클립 섞기 내용 미달). 프레임 PNG 해시가 서로 다른지 보면 바로 판정되고, 고친다면 루프 전에 씬의 SMR 에 `forceMatrixRecalculationPerRender = true` 를 켠다 | plausible |
| 2 | issue | important | new | 「가져온 직후 이름」을 설정이 반영된 뒤의 이름에서 읽음(재현할 수 없는 측정) | `P03Runner.cs:23 · 29-37` · `P03Measure.cs:12-24` | `clipsRaw` 를 FBX 의 `AnimationClip` 하위 에셋 이름으로 읽는데, 이 이름은 `clipAnimations[].name` 을 따른다. 커밋된 `.meta`(name: Idle · takeName: `SlimeRig\|Idle`)가 있는 상태 — 새로 클론 · 두 번째 실행 · Blender 출력만 다시 복사 — 에서 `ImportModels` 를 돌리면 → `clipsRaw` 가 `[Die, Hit, Hop, Idle]` 로 나온다 → 성공 기준 3(a) 함정 표가 「접두 없음」으로 찍히고, 첫 실행 값을 다시 만들 수 없다. `ModelImporter.defaultClipAnimations[].takeName`(또는 `importedTakeInfos`)은 이 설정과 무관하다 | confirmed |
| 3 | suggestion | important | new | 같은 뜻의 인자를 두 호출에서 따로 받고 일치 여부를 검사하지 않음 | `P03Runner.cs:55-58 · 68-70` · `P03Capture.cs:56-58` | 씬에는 어느 변형을 세웠는지 기록이 없는데 `BuildScene(baked)` 와 `DumpFrames(dir, baked)` 가 이 값을 각각 받는다 → `BuildScene(true)` 뒤에 `DumpFrames(dir, false)` 를 부르면 비-bst FBX 의 클립을 bst 인스턴스에 샘플링한다(뼈대 노드 · 첫 뼈의 로컬 변환이 변형마다 다름) → 개체가 90° 돌아가 누운 프레임이 오류 없이 나온다. 인스턴스의 원본 경로(`PrefabUtility.GetPrefabAssetPathOfNearestInstanceRoot`)에서 클립을 찾으면 이 인자가 필요 없다 | plausible |
| 4 | question | important | new | 알려진 결함을 코드 수정 대신 렌더 시점만 바꿔 처리 | `make_enemies.py:435-438`(회전 계산 `247-254 · 315-316` 은 pre-existing) · `Tools/Blender/README.md:33` | README 와 지시서는 「날갯짓 회전축」을 결함으로 보았다. 이 diff 는 회전 코드를 그대로 두고 박쥐 렌더 카메라만 정면으로 바꿨다. 검산: WingL(+X 방향, roll 0) 뼈의 로컬 X 는 월드 −Y, WingR 은 월드 +Y 다. 따라서 `rot_about_world(..., (0,1,0), ±θ)` 는 로컬 X 성분만 있는 오일러이고, 키 사이 보간도 몸의 앞뒤 축(Y) 위에 머문다. 작성자 판단과 일치하며, f1 끝 높이 0.467 도 같은 계산으로 재현된다. 그래도 성공 기준 1 은 렌더를 열어 보는 판정이므로, 「결함이 아니었다」는 판정은 사람이 `render_bat_Flap_f01/_f06.png` 를 보고 확인해야 닫힌다 | confirmed |
| 5 | issue | nit | new | 측정값 이름과 내용이 다름(최고점을 끝 높이로 보고) | `make_enemies.py:347-356 · 359` | `wing_tip_z` 는 x 절댓값이 0.3 보다 큰 정점 가운데 최고 z 를 「날개 끝」으로 돌려준다 → 아래 자세(f6)에서는 바깥 날개 중 가장 안쪽 정점이 최고점이다(계산값 -0.139, 커밋 설명의 값과 같음). 실제 날개 끝은 약 -0.28 이다 → 커밋 설명의 「아래 -0.139」가 끝 높이로 읽혀 진폭이 절반 정도로 보고된다. 좌우 대칭 결론에는 영향이 없다(아래 자세는 min z 를 써야 맞다) | confirmed |
| 6 | suggestion | nit | new | 활성 레이어 대신 이름 리터럴에 의존 | `make_enemies.py:57-59` | `set_cell` 이 활성 UV 레이어가 아니라 이름이 `UVMap` 인 레이어에 쓴다. 지금 입력(프리미티브 = UVMap, 날개 = UV 없음)에서는 `verify()` 와 결과가 같다. 하지만 활성 레이어 이름이 다른 메시가 들어오면 → `UVMap` 이 둘째 레이어로 새로 생기고, 내보내기의 첫 UV(Unity UV0)는 그대로 남는다 → 이번에 고친 「레이어 갈라짐 → 셀 0」 결함이 다시 난다. 「활성 레이어가 있으면 그것, 없으면 `new("UVMap")`」으로 하면 두 경우 모두 맞다 | plausible |
| 7 | suggestion | nit | new | 회귀 검사가 출력에만 있고 종료 코드에 걸리지 않음 | `make_enemies.py:125-134 · 222-225` | 날개 UV 가 다시 셀 0 을 가리켜도 `wing_uv` 에 `[[0.125, 0.125]]` 가 찍힐 뿐 종료 코드는 0 이다 → `--python-exit-code 1` 이 이 회귀를 못 잡는다(`wing_uv == [wing_cell_center]` 를 단언하면 잡힌다) | confirmed |
| 8 | issue | nit | new | §5.6 `new` 뒤 타입 생략 | `P03ModelImporter.cs:45` · `P03Runner.cs:32 · 45` | `new[] { false, true }` — 표준 §5.6 「new 뒤 명시적 타입」 위반(`new bool[] { … }` 로 써야 함) | confirmed |
| 9 | issue | nit | new | §17 에셋 이름 PascalCase 위반 | `Assets/30_Assets/Models/P03_CLI/palette.mat` · `grass.mat`(`P03Paths.cs:8-9`) | 작성자가 정한 머티리얼 이름이 소문자다 → §17(접두 없는 PascalCase, 예: `Palette.png` · `TowerBase.mat`) 위반. FBX · PNG 의 소문자는 지시서가 정한 이름이라 §17 의 「같은 대상은 같은 이름」(palette.png ↔ palette.mat)과 충돌한다 — 어느 규칙을 따랐는지 기록이 필요하다 | confirmed |
| 10 | issue | nit | new | §1 메서드 이름(동사 + 명사) · 줄임말 규칙 위반 | `P03Paths.cs:16`(`Fbx`) · `P03Measure.cs:12`(`ClipNames`) · `P03Capture.cs:18`(`SavePng`) · `:38`(`Stills`) · `:50`(`Frames`) · `P03SceneBuilder.cs:63`(`FacingTower`) | 메서드 이름이 명사형이다(§1 「동사 + 명사」). 단독 줄임말은 대문자로 쓴다(§1 `OrderID` → `SavePNG` · `FBX`) | confirmed |
| 11 | issue | nit | new | §1.3 이름 리터럴이 파일마다 흩어져 있어, 어긋나면 조용히 빈 결과 | `P03SceneBuilder.cs:38 · 40 · 45 · 47 · 53 · 107` · `P03Capture.cs:54-58 · 89-104` · `P03ModelImporter.cs:14-16` | 그룹 이름 `"Slimes"` · `"Bats"` 를 빌더와 캡처가 각자 리터럴로 쓴다 → 한쪽만 바꾸면 `GroupChildren` 이 빈 목록을 돌려주고, 애니메이션 없는 48장이 오류 없이 나온다. 클립 이름(`Idle` · `Hop` · `Flap`), 모델 이름(`"tower"` · `"slime"` · `"bat"` — `P03Paths.MODELS` 와 중복), 태그 `"MainCamera"` 도 상수 클래스(`P03Paths`) 밖의 리터럴이다(§1.3) | confirmed |
| 12 | issue | nit | new | §6.9 가정 단언 누락 · 단언 실패 뒤에도 그대로 진행 | `P03ModelImporter.cs:22 · 32 · 42 · 47 · 86` · `P03SceneBuilder.cs:25 · 52 · 72 · 88` | 파일이 없거나 셰이더를 못 찾으면: `(TextureImporter)` · `(ModelImporter)` 캐스트 결과가 null 이라 메시지 없는 NRE, `Shader.Find` 가 null 이라 `new Material` 에서 예외, 잔디 머티리얼이 null 이라 섬이 자홍색. `Debug.Assert` 는 에디터에서 로그만 남기고 계속 진행하므로(팔레트가 null 이면 `AddRemap(…, null)`) CLI 가 받는 JSON 에는 실패가 보이지 않는다. `BAT_HEIGHTS.Length == BAT_COUNT` 도 단언이 없다 | confirmed |
| 13 | suggestion | nit | new | 예외 경로에서 상태 복원 · 자원 해제 누락 | `P03Capture.cs:18-35`(29-34) | `File.WriteAllBytes` 가 예외(권한 · 디스크)를 내면 → `camera.targetTexture` 와 `RenderTexture.active` 가 복원되지 않고 RT · Texture2D 가 해제되지 않은 채 남는다. 요약 주석이 약속한 「되돌린다」와 다르다(try/finally 필요) | confirmed |
| 14 | issue | nit | new | 이스케이프 없는 수동 JSON 조립 | `P03Runner.cs:64 · 71-72` · `P03SceneBuilder.cs:59-60` | `directory` 에 `"` 나 `\` 가 들어 있으면 → 반환 JSON 이 깨져 CLI 쪽 파싱이 실패한다(같은 클래스의 `ImportModels` 는 `JsonUtility` 를 써서 안전) | plausible |
| 15 | question | nit | new | 성공 기준 4 「머티리얼 하나」의 해석 · 색 값 손 복사 | `P03ModelImporter.cs:17 · 34` · `P03SceneBuilder.cs:88` · `make_enemies.py:28` | 섬에 텍스처 없는 별도 머티리얼 `grass.mat` 을 썼다. 기준 4 「머티리얼은 URP Lit 하나에 팔레트 텍스처를 공유」를 「모델용 팔레트 머티리얼 하나」로 읽은 것인지 확인이 필요하다. 또 `GRASS_COLOR` 는 Blender `PAL[12]` 값을 손으로 옮긴 것이라 → 팔레트를 바꾸면 섬 색만 따로 남는다 | confirmed |
| 16 | issue | nit | new | §8.1 색 · 조명 수치가 코드 리터럴, 모델 치수를 손 복사 | `P03SceneBuilder.cs:24 · 26-29 · 99-100 · 111-112 · 127 · 129` · `P03ModelImporter.cs:17 · 90` | §8.1(색 · 수치는 데이터 에셋에)에 어긋나고, 일부만 이름 붙은 상수다(`4f` · `9f` · `1.1f` · `(50, -30, 0)` 은 인라인). `LAMP_HEIGHT = 2f` 는 Blender 등불집 높이(`make_enemies.py:233`)를 옮겨 적은 값이라 → 모델을 바꾸면 점광이 등불 밖에 남는다. 시험 씬 생성기이므로 예외로 둘지는 판단할 일 | confirmed |
| 17 | issue | nit | new | §5.2 반환 변수 이름 `retval` · 선언 위치 | `P03Measure.cs:14 · 32` · `P03ModelImporter.cs:65` · `P03Capture.cs:91` · `P03Runner.cs:42` | 반환 변수 이름이 `retval` 이 아니고(`names` · `info` · `clips` · `children` · `report`), `Measure` 와 `ImportModels` 는 메서드 중간에서 선언한다(§5.2) | confirmed |
| 18 | issue | nit | new | §19.1 public 멤버의 `<summary>` 누락 | `P03Paths.cs:16` · `P03ModelInfo.cs:21-27` | public 메서드 `Fbx` 와 중첩 public 클래스 `Node` 에 요약 주석이 없다 | confirmed |
| 19 | thought | nit | new | 네임스페이스 이름이 Unity 타입 이름을 가림 | `Defense.Editor.asmdef:2-3` · `P03/*.cs` 의 `namespace Defense.Editor.P03` | `Defense.*` 네임스페이스 안에서 `Editor` 는 `UnityEditor.Editor` 보다 네임스페이스 `Defense.Editor` 로 먼저 해석된다 → 이 어셈블리에 커스텀 인스펙터 `class X : Editor` 를 만들면 CS0118 컴파일 오류가 난다(완전 한정 이름 필요). 이 이름은 지시서와 CLAUDE.md(asmdef 이름 = 루트 네임스페이스)가 정한 것이라, DEF-M03 이후 에디터 코드가 늘어날 때의 함정으로 기록해 둔다 | confirmed |
| 20 | question | nit | new | 전제의 근거가 불분명 · 묻지 않고 열린 씬을 버림 | `P03Measure.cs:26` · `P03Runner.cs:41` · `P03SceneBuilder.cs:34` · `P03Capture.cs:77` | `Measure` 는 인스턴스를 세웠다가 바로 지우는데 주석은 「열린 씬이 비어 있어야 한다」고 한다 — 그 이유가 무엇인지. 이 전제를 위해 부르는 `NewScene(Single)`(그리고 `Build` 의 `NewScene` · `OpenScene(Single)`)은 GUI 에디터에서 저장하지 않은 씬이 열려 있으면 묻지 않고 버린다(`SaveCurrentModifiedScenesIfUserWantsTo` 없음) | confirmed |
| 21 | question | nit | new | 모델 구분 없는 거르개 + 접미 제거 → 이름 충돌 가능 | `P03ModelImporter.cs:16 · 63-78` · `P03ClipNames.cs:8 · 17` | 세 모델이 `KEPT_CLIPS` 하나를 함께 쓰고 `.001` 을 지운다. 그래서 다른 뼈대의 동작이 FBX 에 같이 실리면(예: bat.fbx 에 슬라임의 Hit 와 박쥐의 Hit.001) → 이름이 `Hit` 인 클립이 둘 생기고 `FindClip` 은 먼저 나온 쪽을 고른다. 지금 `.meta` 에는 자기 뼈대의 동작만 있어 실제 피해는 없다 — 이 거르개가 무엇을 버리려는 것인지 | plausible |
| 22 | question | nit | new | 성공 기준 6 「섞고」의 해석 | `P03Capture.cs:62-66` | 슬라임마다 클립 하나를 48프레임 내내 고정했다(짝수 Idle · 홀수 Hop). 기준이 「한 개체 안에서 Idle · Hop 을 섞기(전환)」를 뜻했다면 미달이다. 개체 사이의 섞기로 읽은 근거를 확인할 것 | confirmed |
| 23 | thought | nit | new | 고위험 경로 대조 — 이름 패턴의 거짓 양성 후보 | `Assets/10_Scripts/Editor/P03/P03SceneBuilder.cs`(및 `P03Runner.BuildScene`) | diff 에 `Save*` · `30_Assets/Data/` · `ProjectSettings/` · `Packages/` · 빌드 프로필 · 서명 · `.github/workflows/` 변경은 없다. 다만 `*` 가 `/` 를 넘는 glob(fnmatch 류)으로 `Assets/10_Scripts/Editor/*Build*` 를 대조하면 이 파일이 고위험으로 잡힌다. 내용은 씬 생성이고 빌드 설정 · 플랫폼과는 무관하다 | confirmed |
| 24 | thought | nit | out-of-scope | 수정 허용 영역을 글자 그대로 읽으면 그 밖에 있는 폴더 `.meta` | `Assets/10_Scripts/Editor.meta` · `Assets/30_Assets/Models.meta` · `Assets/30_Assets/Models/P03_CLI.meta` | 허용 영역(`Editor/**` · `Models/P03_CLI/**`) 바깥 자리지만, 새 폴더에 Unity 가 반드시 만드는 짝 파일이다 — 범위 대조 때 허용으로 처리할지 표시해 둔다 | confirmed |
| 25 | thought | nit | out-of-scope | 읽기 전용 영역에 미추적 파일이 남아 있음 | `ProjectSettings/SceneTemplateSettings.json`(작업 트리 `??`) | 에디터가 `NewScene` 때 만든 파일을 커밋하지 않은 것은 맞다. 하지만 작업 트리에 남아 있어서 이후 `git add -A` 한 번이면 계약(ProjectSettings 수정 금지) 위반 커밋이 된다 | confirmed |
| 26 | thought | nit | out-of-scope | 문서가 코드 상태와 어긋남 | `Tools/Blender/README.md:33` | 「알려진 결함 둘(날개 셀 · 날갯짓 회전축)은 P03 실행 세션이 고친다」가 이 diff 뒤에도 그대로다 → 날개는 고쳤고 회전축은 결함이 아니라고 판정했는데, 다음 사람은 아직 미해결로 읽는다. README 는 수정 허용 영역 밖이라 작성자가 고칠 수 없다 — 후속 처리가 필요하다 | confirmed |

### 확인하지 않은 것 · 추정한 것
- 경로 기준: 저장소 루트 `/Users/devman/_Projects/_Personal/Games/Defense/z.tmp/wt/p03-sonnet`, 줄 번호는 `546f586` 기준. 표의 `P03*.cs` 는 `Assets/10_Scripts/Editor/P03/`, `make_enemies.py` 는 `Tools/Blender/` 아래에 있다.
- 실행하지 않음: Unity · Blender 를 띄우지 않았고 컴파일 · 테스트 · 스크립트도 돌리지 않았다. 그래서 컴파일 경고 0 여부와 실제 출력(P03_RESULT · 캡처 · 프레임)은 확인하지 못했다. 격리 조건의 「다른 모델 폴더」가 어느 쪽인지 모호해 `z.captures/` 는 어느 폴더도 열지 않았다 — #1 · #4 의 시각 판정은 사람 몫이다.
- #1: SMR 이 「스킨 행렬을 프레임마다 한 번만 계산한다」는 것은 `SkinnedMeshRenderer.forceMatrixRecalculationPerRender` API 의 의미에서 추정했다. 프레임 PNG 들이 서로 다르면 「틀림」으로 닫으면 된다.
- #2: Unity 가 `clipAnimations[].name` 으로 하위 `AnimationClip` 이름을 정한다는 것은 Unity 의 일반 동작과 커밋된 `.meta`(name ↔ takeName)를 보고 판단했다. 재실행해 보지는 않았다.
- #3: 변형마다 클립 커브가 다르다는 것은 Blender FBX 내보내기(`bake_space_transform`, 그리고 `bake_anim_simplify_factor=0.0` 일 때 모든 대상에 키를 강제로 넣는 동작)에 대한 지식에서 추정했다. FBX 바이너리는 열지 않았다.
- FBX 계층 추정: Blender 내보내기가 뼈대에 붙은 메시를 뼈대의 형제(최상위 노드)로 쓴다는 지식과 `P03SceneBuilder.cs:76` 주석(루트 X 270° 는 탑만 해당)을 근거로, 슬라임 · 박쥐 클립에는 루트("" 경로) 커브가 없어서 `SampleAnimation` 이 인스턴스의 위치 · 방향을 덮어쓰지 않는다고 보았다. 이 추정이 틀리면 프레임에서 모든 개체가 원점(탑 자리)으로 모인다. 추정이라 표에는 올리지 않았다.
- #4 · #5 의 수치(뼈 로컬 축, 아래 자세의 끝 높이 약 -0.28)는 스크립트 좌표로 손 계산했다. 같은 식으로 커밋 설명의 0.467 · -0.139 가 재현된다. 렌더는 보지 않았다.
- 가정한 것: URP 의 `Camera.Render()` 와 MSAA RenderTexture 의 `ReadPixels` 가 창 없는 에디터(Metal)에서 그림을 낸다. Blender 5.2.3 에서 `MeshUVLoopLayer.data` 가 여전히 있고 bmesh 의 기본 UV 레이어 이름이 `Float2` 라는 점은 작성자 설명(P03_RESULT 에 `wing_uv` 가 나왔다는 커밋 설명)을 믿었다.
- 범위에 없어 보지 않은 것: MP4 인코딩(VSE · ffmpeg) 코드, 작업 보고 · 센서 기록(이 범위보다 뒤의 커밋).
- 연결 확인(모두 일치):
  - 6개 `*.fbx.meta` 의 `externalObjects` 에서 `Palette` → `palette.mat`(guid `931255fd…`).
  - `palette.mat` 의 `_BaseMap` → `palette.png`(`ee40b6ba…`).
  - 씬의 섬 → `grass.mat`(`b1121e39…`).
  - 씬의 프리팹 인스턴스 13개(탑 1 · 슬라임 8 · 박쥐 4) → `*_bst.fbx` guid.
  - `clipAnimations` 이름(Idle · Hop · Hit · Die / Flap · Hit), `loopTime`(Idle · Hop · Flap), 탑의 `importAnimation: 0` · `animationType: 0` 이 코드 상수와 같다.
  - 팔레트 임포트 설정(Point · 밉맵 없음 · Clamp · 비압축)도 코드와 같다.
  - 셰이더 guid `933532a4…` 가 URP Lit 이라는 것은 기억에 의존한 판단이다.
- 해당 없음:
  - CLAUDE.md 「검토 기준」의 빌드 프로필 PlayerSettings 사본 · `ENABLE_RUNTIME_PIPELINE` 항목과 표준 §9 · §10 · §12 · §14 는 대응하는 코드가 없다.
  - §15: `P03ClipNames.Strip` 은 순수 로직이지만 지시서가 요청하지 않은 테스트를 금지하므로 지적하지 않았다.
  - §7.1: public 필드가 있는 `P03ModelInfo` 는 MonoBehaviour 가 아닌 JSON 보고 DTO 라 §12.1 예외에 준한다고 보고 올리지 않았다.