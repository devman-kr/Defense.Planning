---
id: 20261031-p03-s1-a3ff2b61-final
title: 코드리뷰 S1 — 에이전트 a3ff2b61 최종 보고 원문
summary: 「2라운드 센서 — 수정 커밋 리뷰어 A(opus)」 에이전트(claude-opus-5-5 · 도구 호출 44)가 돌려준 최종 보고 원문 — 출처 SubagentHandback.
doc_type: review
status: final
lifecycle: static
created: 2026-10-31
updated: 2026-10-31
work_unit: P03
---
| # | 종류 | 심각도 | 기원 | 유형 | 파일:줄 | 실패 시나리오(입력 → 잘못된 결과) | 확신 |
|---|---|---|---|---|---|---|---|
| 1 | suggestion | nit | new | 가정 단언 누락(§6.9). `AssetImporter.GetAtPath` 결과를 검사하지 않고 `(ModelImporter)` 로 캐스트한다 | `/Users/devman/_Projects/_Personal/Games/Defense/z.tmp/wt/p03-sonnet/Assets/10_Scripts/Editor/P03/P03Measure.cs:17-19` | FBX 여섯 개 중 하나가 아직 복사되지 않았거나 이름이 다른 상태에서 `P03Runner.ImportModels()` 를 부른다 → `GetAtPath` 가 null 을 돌려준다(설치된 `UnityEditor.CoreModule.xml`: "or null if the asset doesn't exist"). null 캐스트는 그대로 통과한다 → 19행 `importer.defaultClipAnimations` 에서 `NullReferenceException` 이 나는데, 어느 파일인지는 나오지 않는다. 퇴행은 아니다. 수정 전에는 `ClipNames` 가 빈 배열을 내고, 같은 꼴의 NRE 가 `ConfigurePalette` 가 설정을 바꾼 뒤 같은 폴더의 `P03ModelImporter.cs:47-48`(같은 미검사 캐스트, pre-existing)에서 났다. 지금은 오히려 부수 효과 전에 멈춘다. 다만 새 줄이 단언 없이 같은 패턴을 하나 더 만들었다 | confirmed |
| 2 | nitpick | nit | new | 메서드 이름 규칙 위반(§1 표: 메서드는 「동사 + 명사」) | `/Users/devman/_Projects/_Personal/Games/Defense/z.tmp/wt/p03-sonnet/Assets/10_Scripts/Editor/P03/P03Capture.cs:113` · `/Users/devman/_Projects/_Personal/Games/Defense/z.tmp/wt/p03-sonnet/Assets/10_Scripts/Editor/P03/P03Measure.cs:15` | 동작 결함은 아니다. `SourceAssetPath` 는 동사가 없는 명사구다. `TakeNames` 는 뜻이 「take 의 이름」(명사구)인데, `Take` 가 동사로 읽혀 「이름을 가져온다」로 오독될 수 있다. 같은 꼴인 `ClipNames`(P03Measure.cs 28행)와 `P03Paths.Fbx` 는 546f586 부터 있던 것이다 | confirmed |
| 3 | thought | nit | new | 1라운드 지적 ①~③ 밖의 출력 변경(이름 목록 정렬) | `/Users/devman/_Projects/_Personal/Games/Defense/z.tmp/wt/p03-sonnet/Assets/10_Scripts/Editor/P03/P03Measure.cs:23` · `/Users/devman/_Projects/_Personal/Games/Defense/z.tmp/wt/p03-sonnet/Assets/10_Scripts/Editor/P03/P03Measure.cs:39` | 1차(546f586 코드)의 `ImportModels` JSON 과 지금 JSON 을 바이트로 비교하면 `clipsRaw` · `clips` 의 순서가 달라 맞지 않는다. Ordinal 정렬로 `SlimeRig\|Die` 가 맨 앞에 오는데, 미커밋 보고서 초안 46행의 1차 표기는 `Hit · Hop · Idle · Die` 순이다. 커밋 설명이 「1차와 집합까지 같고」라고 인정했고, 목적이 재실행끼리의 바이트 일치이므로 결함은 아니다. 다만 39행 `ClipNames`(설정 뒤 이름)의 정렬은 지적 ①(벗기기 전 이름)의 대상이 아니었다 | confirmed |
| 4 | nitpick | nit | new(선언 줄은 546f586 부터 있었고, 이 diff 가 호출처를 없앴다) | 호출처가 사라진 뒤에도 남은 `public` | `/Users/devman/_Projects/_Personal/Games/Defense/z.tmp/wt/p03-sonnet/Assets/10_Scripts/Editor/P03/P03Measure.cs:28` | 수정 전 유일한 외부 호출처(546f586 `P03Runner.cs:35` `rawClips[path] = P03Measure.ClipNames(path);`)가 `TakeNames` 로 바뀌었다. 그래서 지금은 같은 클래스의 `Measure`(52행)만 부른다(94591e2 에서 `git grep` 으로 확인). 설정 뒤 이름을 「벗기기 전」 자리에 다시 넣는 오용(지적 ① 의 원인)을 막으려면 `private` 로 좁힐 수 있다. 동작 결함은 아니다 | confirmed |
| 5 | thought | nit | new | 고위험 경로 · 수정 허용 영역 대조: 해당 없음 | `/Users/devman/_Projects/_Personal/Games/Defense/z.tmp/wt/p03-sonnet/Assets/10_Scripts/Editor/P03/`(범위 4파일 전체) | 해당 없음. 제외 패턴 없이 본 `git diff --stat 546f586..94591e2` 도 `P03Capture.cs` · `P03Measure.cs` · `P03ModelImporter.cs` · `P03Runner.cs` 4파일뿐이고, 모두 수정 허용 영역 `Assets/10_Scripts/Editor/**` 안에 있다. 저장 데이터 · 재화 · 업그레이드 수치 · `ProjectSettings/` · 빌드 프로필 · `Packages/` · 서명 · `.github/workflows/` 변경은 없다 | confirmed |

### 확인하지 않은 것 · 추정한 것
- **커밋 설명의 실행 결과는 확인하지 않았다.** 대상은 재컴파일 오류 0 · 경고 0, `ImportModels` 재실행 결과가 1차와 집합까지 같음, `.meta` 불변, 새 `DumpFrames` 48장이 기존과 SHA-256 일치, `unity test` 종료 0 이다. 지시대로 에디터와 테스트를 돌리지 않았다.
  - 코드에서는 이 주장과 모순되는 점이 없다. 클립 선택(짝수는 Idle, 홀수는 Hop, 박쥐는 Flap)과 위상 식이 수정 전과 같다.
  - 씬 인스턴스 13개는 모두 `_bst` FBX 의 모델 프리팹 인스턴스다. 씬 YAML 의 `m_SourcePrefab` fileID 100100000 guid 가 `slime_bst` 8 · `bat_bst` 4 · `tower_bst` 1 이다. 따라서 옛 `BuildScene(true)` + `DumpFrames(…, true)` 와 같은 클립이 잡힌다.
- **`PrefabUtility.GetPrefabAssetPathOfNearestInstanceRoot` 의 반환값은 API 문서로 확인하지 못했다.**
  - 116행의 `path.Length == 0` 은 프리팹 인스턴스가 아닌 객체에 null 이 아니라 빈 문자열이 온다고 가정한다. 설치된 `/Applications/Unity/Hub/Editor/6000.3.27f1/Unity.app/Contents/Resources/Scripting/Managed/UnityEngine/UnityEditor.CoreModule.xml` 에는 "The asset path." 라고만 적혀 있다. `AssetDatabase.GetAssetPath(null)` 이 "" 를 돌려주는 관례를 근거로 빈 문자열이라고 추정했다. null 이면 이 분기는 의도한 문구 대신 NRE 가 된다.
  - 모델 프리팹 인스턴스에 `.fbx` 경로를 돌려준다는 것도 동작 지식에 기댄 추정이다. 커밋의 SHA-256 일치 주장이 맞다면 실측으로 뒷받침된다.
  - 지금 씬의 Slimes · Bats 자식은 모두 모델 프리팹 인스턴스라 116행 분기를 타지 않는다.
- **탑에서 `defaultClipAnimations` 가 설정 전과 같은 take 목록을 내는지 확인하지 못했다.** 탑은 `importAnimation=false` · `animationType=None` 으로 설정된다(`P03ModelImporter.cs:49-53`).
  - P03Runner.cs:23 주석의 「가져오기 설정과 무관하게」는 API 문서("based on TakeInfo")상 `clipAnimations` 에 대해서만 뒷받침된다.
  - 작업 트리의 미커밋 초안 `/Users/devman/_Projects/_Personal/Games/Defense/z.tmp/wt/p03-sonnet/z.docs/work_reports/20261031/4_create_P03_샘플씬_sonnet.md` 48행은 1차 실행의 탑 이름을 「없음」으로 적었다. 탑 FBX 에 take 가 없다면 양쪽 모두 빈 배열이라 같다고 추정한다.
  - 탑 FBX 가 take 를 갖게 되면(Blender 쪽 변경) 재실행 값이 달라질 수 있다.
- **옛 시그니처 `DumpFrames(directory, baked)` 의 잔재**는 94591e2 트리 전체(`git grep`)와 위 미커밋 초안에는 없음을 확인했다. 저자 세션의 CLI 호출 기록과 `z.captures/` 의 README 는 격리 조건에 따라 보지 않았다.
- **`AssetDatabase.LoadAllAssetsAtPath` 의 동작 두 가지는 확인하지 않았다.**
  - 없는 경로에서 예외 없이 빈 배열을 돌려준다는 것은 추정이다. 1행에서 수정 전 실패가 뒤로 미뤄졌다고 한 비교의 전제다.
  - 재가져오기 사이에 하위 에셋 순서가 안정적인지도 확인하지 않았다. 3행의 `ClipNames` 정렬이 꼭 필요했는지와 관련된다.