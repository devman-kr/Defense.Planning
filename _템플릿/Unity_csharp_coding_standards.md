# C# 코딩 표준 — Unity

Defense(Lantern Rush!)와 뒤이은 게임들의 Unity C# 규칙이다. EasyCheck.Server 의 C# 코딩 표준(POCU C# 표준 계열 — 원문은 Planning 커밋 `caf8ac8`)을 Unity 6 · 모바일 · 오프라인 · 공개 포트폴리오 전제로 고쳤다(Planning P00 검토서 2026-10-30 · 결정 D-06 · D-07). 정본은 Planning `_템플릿/Unity_csharp_coding_standards.md`, 사본은 `Defense.Unity/z.docs/dev/csharp_coding_standards.md` — 고칠 때는 정본을 고치고 복사한다.

**읽는 법**: 규칙은 한 줄. Unity 전용 규칙에는 「왜」 한 줄이 붙고, 번호는 끝의 「근거」 표다. 절 머리의 대괄호는 코드리뷰 가이드 영역 코드(`SAVE` · `ECON` · `LIFE` · `TIME` · `PERF` · `INPUT` · `CONTRACT` · `TEST` · `UI` · `BUILD`)이고, 센서 지적은 「표준 §12」처럼 절을 인용한다. 이 표준은 규칙이지 게이트가 아니다 — 지키는지는 코드 리뷰가 본다. 언어는 C# 9.0(Unity 6000.3, 근거 1).

---

## 0. 기본 원칙

1. **가독성을 최우선으로 삼는다.** 코드가 그 자체로 문서여야 한다.
2. 합당한 이유가 없는 한 **`.editorconfig` 가 정한 IDE 자동 서식을 따른다.**
3. **일관성을 유지한다.** 기존 코드의 스타일을 존중한다.
4. **C# 일반 관례와 Unity 가 다를 때는 Unity 를 따른다** — 직렬화(§12) · null(§6) · 수명 주기(§7 · §9).
5. **접근점은 적을수록 좋다.** 싱글톤 · 정적 전역은 최소한으로 쓴다 — 무분별한 싱글톤은 의존을 숨기고 초기화 순서와 테스트 격리를 깨뜨려 구조가 망가지기 쉽다. 기본은 부트스트랩이 참조를 넘기는 것(§7).

---

## 1. 명명 [CONTRACT]

| 대상 | 규칙 | 비고 |
|---|---|---|
| 클래스 · 구조체 · 열거형 | PascalCase | 비트 플래그는 `[Flags]` + 비트 시프트, 이름은 복수 |
| 인터페이스 | `I` + PascalCase | `IAdService` |
| private 필드 | `_camelCase` | `readonly` 도 같다. 인스펙터는 `_` 를 벗겨 보여 준다 |
| 상수(`const` · `static readonly`) | UPPER_SNAKE_CASE | Unity 관례는 `k_PascalCase` 이나 이 저장소는 UPPER_SNAKE(D-07) |
| 프로퍼티 | PascalCase | 대응 private 필드는 프로퍼티 바로 위 |
| 지역 변수 · 매개변수 | camelCase | |
| 메서드 | PascalCase, 동사 + 명사 | |
| bool 반환 메서드 · 프로퍼티 | `Is` · `Can` · `Has` · `Should` 접두 | |
| 이벤트 | 동사구 과거형 `WaveStarted` · `EnemyDied`, 발생 메서드 `OnWaveStarted` | C# `event Action<T>` |
| 줄임말 | 단독이면 대문자, 뒤에 단어가 오면 파스칼 · 카멜 | `OrderID` · `HttpCode` |
| 네임스페이스 | 코어 `Devman.Core.<영역>` · 이 게임 `Defense.Game.<영역>` · 테스트 `Defense.Tests.EditMode` | asmdef 이름 = 루트 네임스페이스 |
| 데이터 에셋 클래스 | `<이름>Def` · 곡선 `<이름>Curve` | 기획 데이터 표 K1~K6(§8) |
| 시스템 · 서비스 | `<이름>System` · `I<이름>Service` | `WaveSystem` · `ISaveService` |

- **코어 경계**: 다른 게임에서 수정 없이 쓰는 것(저장 · 광고 자리 · 플랫폼 · 풀 · 로그 래퍼 · 시간 배속 · 범용 유틸)은 `Devman.Core`, 이 게임의 규칙(웨이브 · 무기 · 드래프트 · 강화)은 `Defense.Game`. Core 는 Game 을 참조하지 않는다(asmdef). 애매하면 Game 에 두고, 두 번째 게임이 필요로 할 때 Core 로 올린다.
  — 왜: 코어는 다음 게임이 복사해 간다(G-07). 게임 이름이 들어 있으면 복사할 때마다 고쳐야 한다.
- 반복문 인덱스 말고는 의미 있는 이름. getter · setter 메서드 대신 프로퍼티. `OrNull` 접미는 §6.
- **경계의 이름**: 기획 데이터 표의 열 = 에셋 필드 이름(단위 접미 `Seconds` · `PerSecond` · `Percent` · `Meters`) · 저장 JSON 키 = 필드 이름(§12) · 태그 · 레이어 · 씬 · 애니메이터 파라미터 · 입력 액션 이름은 상수 클래스 하나(`GameIds`)에 — 문자열 리터럴을 흩뿌리지 않는다.

---

## 2. 파일 · 프로젝트 구조 [BUILD]

- **클래스 하나 = 파일 하나**, 파일 이름 = 클래스 이름(대소문자까지).
  — 왜: MonoBehaviour · ScriptableObject 는 파일 이름이 다르면 Unity 가 컴포넌트 · 에셋으로 만들지 못한다.
- partial 은 `클래스명.세부.cs`. 드물게 쓴다.
- `using` 은 IDE 정렬(System → Unity → 프로젝트, 알파벳). 안 쓰는 `using` 은 지운다. 파일 범위 네임스페이스(C# 10)는 쓸 수 없다 — 블록으로.
- 파일 헤더 블록 주석은 없다. 작성자 · 날짜 · 변경 이력은 git 과 작업 보고서에.
- 폴더(저장소 루트 기준): `Assets/_Project/Core/`(asmdef `Devman.Core`) · `Assets/_Project/Defense/`(`Defense.Game`) · `Assets/_Project/Data/`(에셋) · `Assets/_Project/Art/` · `Assets/_Project/Tests/EditMode` · `PlayMode` · `Assets/ThirdParty/`(외부 — `ASSETS.md` 장부). 폴더마다 asmdef. 에디터 전용 코드는 `Editor/` + 에디터 asmdef(§16).
- 설정값은 데이터 에셋(`GameConfigDef`)에. INI · XML · `Resources/` · `StreamingAssets/` 는 만들지 않는다.
- 빌드 산출물은 저장소 밖 `../z.builds/`. `Library/` · `Temp/` · `Logs/` · `obj/` · `UserSettings/` 는 커밋하지 않고 `.meta` 는 반드시 짝으로 넣는다.

---

## 3. 클래스 구조 [LIFE]

멤버 순서: ① 상수 → ② 정적 필드 → ③ `[SerializeField]` 필드 → ④ 런타임 필드 → ⑤ 프로퍼티 → ⑥ 이벤트 → ⑦ **Unity 메시지**(실행 순서대로 `Awake` · `OnEnable` · `Start` · `FixedUpdate` · `Update` · `LateUpdate` · `OnDisable` · `OnDestroy`, 그 밖의 메시지는 그 뒤) → ⑧ public 메서드 → ⑨ private · protected 메서드 → ⑩ 중첩 타입.

- 그룹 사이는 빈 줄 하나. 구분선 주석은 없다.
- 연관 있는 멤버끼리 모은다. `#region` 은 쓰지 않는다 — 길어지면 클래스를 나눈다.
- 상속을 의도하지 않는 클래스는 `sealed`(MonoBehaviour 포함). 밖에 보일 필요 없으면 `internal`(테스트는 §15).
- ISP — 인터페이스는 좁고 분명하게. 실제 자원을 쥔 인터페이스만 `IDisposable`(§9).

---

## 4. 서식

- 띄어쓰기 4칸, 탭 없음, 줄 끝 LF, 한 줄 120자 안팎.
- 중괄호는 **Allman**(새 줄). 한 줄 블록에도 중괄호. 예외: 단일 흐름 제어문(`return` · `continue` · `break`)은 생략 허용.
- 한 줄에 변수 하나. 값의 수직 정렬은 하지 않는다(자동 서식이 깨뜨린다).
- 나머지는 `.editorconfig`(`Defense.Unity/.editorconfig`, 정본 `_템플릿/Unity_.editorconfig`)가 정한다. Unity 컴파일러는 이 파일을 읽지 않는다 — IDE 용이다.

---

## 5. 변수 · C# 기능 [PERF]

- **`var` 금지.** 예외는 우변 `new` 로 타입이 드러날 때와 `IEnumerable` 체인뿐.
- 변수 가리기 금지. 지역 변수는 쓰는 곳 가까이, 반환값 변수 `retval` 은 메서드 시작에.
- 컨테이너는 `System.Collections.Generic`. 예외: 코루틴 반환형 `IEnumerator`(`System.Collections`).
  — 왜: Unity 코루틴은 비제네릭 `IEnumerator` 를 반환하는 메서드다(근거 4).
- 디폴트 매개변수는 비트 패턴 0(`null` · `false` · `0`). 자주 쓰는 호출은 축약형 오버로딩.
- **금지**: `using` 선언(C# 8) · `??` · `??=` · 대상 형식 `new()`(C# 9) · 레코드 · `init` 세터 · `#nullable` 컨텍스트.
  — 왜(레코드 · `init`): Unity 6000.3 은 C# 9 이지만 `init` 세터를 지원하지 않고 레코드는 직렬화되지 않는다(근거 1). — 왜(`#nullable`): UnityEngine API 에 null 주석이 없어 경고만 늘고, Unity 의 가짜 null(§6)을 표현하지 못한다.
- **필수**: `new` 뒤 명시적 타입. `out` 변수는 별도 줄에 선언(단순하면 인라인 허용).
- **핫패스 금지**(매 프레임 · 적 · 투사체 단위로 도는 코드): LINQ · 박싱 · 문자열 결합 · 보간 · 클로저 · `params` · 인터페이스 타입으로 받은 컬렉션의 `foreach`(열거자가 박싱된다) · 새 배열 · `yield` 열거.
  — 왜: 매 프레임 할당은 GC 스파이크가 되어 모바일에서 프레임을 떨어뜨린다.
- 권장: `StringBuilder` 는 캐시해 재사용 · `CallerMemberName` 은 로그 래퍼(§13)에만 · `struct` 는 작고 불변인 값에만, 큰 구조체는 `in` 으로 전달.
- 스레드 안전 컬렉션은 쓸 일이 없다 — 메인 스레드 게임(§14).

---

## 6. null · 예외 · 단언 [LIFE]

- public 메서드의 매개변수 · 반환값은 null 을 허용하지 않는 것을 추구한다. 허용하면 이름 뒤에 **`OrNull`**(`FindTargetOrNull`).
- 순수 C# 타입에는 `?.` 허용, `??` 는 금지(§5).
- **`UnityEngine.Object` 파생**(GameObject · Component · MonoBehaviour · ScriptableObject)은 **`== null` · `!= null` 만.** `?.` · `??` · `is null` · `is not null` · `ReferenceEquals` 금지.
  — 왜: Unity 의 `==` 는 관리 참조뿐 아니라 네이티브 객체 포인터도 검사해 파괴된 객체를 null 로 본다. `?.` · `??` · `is null` 은 C# 규칙상 사용자 정의 연산자를 부르지 않아 파괴된 객체를 산 것으로 다룬다(근거 2).
- 예외는 **경계에서만** 다룬다 — 저장 파일 읽기(§12) · 데이터 에셋 검증(`OnValidate` · EditMode 테스트) · 플랫폼 API(광고 · 파일). 안으로 들어온 데이터는 유효하다고 가정하고 던지지 않는다.
- `catch (Exception)` 일괄 처리 금지 — 구체 타입. catch 하면 반드시 로그(§13). 정리 코드의 빈 catch 만 허용.
- **MonoBehaviour 메시지 안에서는 예외를 던지지 않는다.**
  — 왜: Unity 가 예외를 삼키고 로그만 남기며, 그 호출의 나머지 처리가 끊긴 채 다음 프레임이 돈다.
- `switch` 의 `default:` — 코어 순수 로직은 `NotImplementedException`(테스트가 잡는다), 런타임 컴포넌트는 `Debug.LogError` + 안전값(게임을 멈추지 않는다).
- 코드가 세운 가정마다 `Debug.Assert`(`UnityEngine.Debug`). 단언 안에 부작용 있는 식을 쓰지 않고, 릴리스 동작을 단언에 기대지 않는다.
  — 왜: `[Conditional("UNITY_ASSERTIONS")]` 라 그 심볼이 없는 빌드에서는 호출 자체가 빠진다(근거 3).

---

## 7. MonoBehaviour [LIFE · PERF]

- 인스펙터 노출은 **`[SerializeField] private`** 만. public 필드 금지. `[field: SerializeField]` 는 쓰지 않는다.
  — 왜: 백킹 필드 이름이 프로퍼티 이름에 묶여, 프로퍼티 이름을 바꾸면 직렬화된 값이 사라진다.
- 메시지의 역할: `Awake` = 자기 초기화 · 컴포넌트 캐시 / `Start` = 다른 객체 참조 · 부트스트랩이 넘긴 값 사용 / `OnEnable` · `OnDisable` = 구독 · 해제 **짝** / `OnDestroy` = 마지막 정리.
- **서비스 접근**: 씬의 부트스트랩 하나(`GameBootstrap`)가 시스템을 만들고 생성자 · `Init` 으로 참조를 넘긴다. `Instance` 싱글톤 · `FindObjectOfType` · `FindAnyObjectByType` · `GameObject.Find` · `SendMessage` 로 찾지 않는다. 정적 접근점은 순수 유틸(수학 · 상수)뿐 — 꼭 필요하면 이유를 주석 한 줄로 남기고, 둘을 넘기면 설계를 다시 본다(§0 ⑤).
- **적 · 투사체 · 코인마다 `Update` 를 두지 않는다.** 시스템 하나(`EnemySystem`)가 배열 · 리스트를 돈다.
  — 왜: 개체마다 들어오는 Unity 메시지는 네이티브 → 관리 경계 비용이라 300 개체 목표(기획서 5절)에서 프레임을 먹는다.
- `FixedUpdate` 는 물리만. 게임 로직은 `Update` + `Time.deltaTime`(§10).
- `GetComponent` · `Camera.main` · `transform` 체인은 `Awake` 에서 캐시. 루프 안에서 부르지 않는다.
- `[RequireComponent]` · `[DisallowMultipleComponent]` 로 전제를 선언하고, 필수 참조는 `Awake` 에서 `Debug.Assert`.
- 씬 전환 · 재시작 때 정적 상태(static 필드 · static 이벤트)를 초기화하는 자리를 부트스트랩 한 곳에 둔다.
  — 왜: 플레이 모드 옵션에서 도메인 리로드를 끄면 static 이 플레이 세션 사이에 남는다.

---

## 8. 데이터 에셋 · 계약 [CONTRACT · ECON]

- 밸런스 수치 · 사용자 문구 · 색 · 곡선은 코드가 아니라 **데이터 에셋**(ScriptableObject `*Def` · `*Curve`)에. 코드에 박힌 수치는 지적 대상(ECON).
- 기획 데이터 표(`Defense.Design/데이터/`)의 열 = 에셋 필드(이름 · 단위 · 순서). **표에 없는 수치는 코드에도 없다.** 표와 에셋이 다르면 CONTRACT. 재화 · 영구 강화 · 해금(K5)은 고위험 — 바꾸면 보고에 전후 값.
- 클래스에 `[CreateAssetMenu(menuName = "Defense/<영역>/<이름>")]`, 에셋은 `Assets/_Project/Data/<영역>/`.
- **런타임에 에셋을 바꾸지 않는다** — 읽기 전용. 런 중 변하는 값은 런타임 객체(POCO)로 복사해 쓴다.
  — 왜: 에디터에서는 플레이 모드에 쓴 값도 에셋에 저장돼 다음 플레이에 남고, 플레이어에서는 읽기만 되어 두 환경의 동작이 달라진다(근거 5).
- 필드에 `[Min]` · `[Range]` · `[Tooltip]`. 검증은 `OnValidate` 와 EditMode 테스트(모든 `*Def` 를 로드해 범위 · 표 대조, §15).
- 에셋 참조는 인스펙터로 연결한다. `Resources.Load` · 경로 문자열 금지.

---

## 9. 풀 · 수명 주기 [LIFE]

- 런 중 `Instantiate` · `Destroy` 금지 — 풀(`ObjectPool<T>`, Core)에서 꺼내고 돌려준다. 풀은 런 시작 전에 미리 채운다.
- **꺼낼 때 상태를 전부 초기화**(체력 · 속도 · 타이머 · 구독 · 트레일 · 머티리얼 색). 돌려준 객체의 참조를 들고 있지 않는다 — 다음 프레임에 다른 적이 된다.
- 돌려주기는 `SetActive(false)`. 코루틴은 이때 멈추지만 `enabled = false` 로는 멈추지 않는다(§14).
- 이벤트 구독은 `OnEnable` · `OnDisable` 짝. 람다 구독은 해제할 수 없으니 메서드 그룹으로 구독한다.
- `IDisposable` · 파이널라이저는 `NativeArray` · 파일 스트림처럼 실제 자원을 쥘 때만. MonoBehaviour 의 정리 지점은 `OnDisable` · `OnDestroy` 다.
- 씬 전환 · 재시작의 초기화 순서(정적 상태 → 풀 → 시간 배율 → 시스템)는 부트스트랩 한 곳에.

---

## 10. 시간 [TIME]

- 게임 로직은 **`Time.deltaTime`**(일시정지 · 배속 반영). UI 연출 · 메뉴만 `Time.unscaledDeltaTime`.
- 배속 · 일시정지는 `Time.timeScale` 을 바꾸는 곳 하나(`GameClock`). 흩어 놓지 않는다.
- 프레임 수에 기대는 로직 금지(「10 프레임 뒤」). 시간 · 거리로 쓴다.
- 코루틴 대기 `WaitForSeconds` 는 캐시해 재사용. `WaitForSecondsRealtime` 은 UI 만.
- 누적 타이머를 쓴다. `DateTime.Now` 는 저장 기록(§12)에만, 로직에는 쓰지 않는다.

---

## 11. 성능 [PERF]

- **매 프레임 할당 0** 이 목표 — 프로파일러 GC Alloc 열로 확인한다. 금지 목록은 §5.
- 문자열은 UI 갱신 때만 만들고, 숫자 표시는 값이 바뀔 때만 갱신한다.
- 물리 질의는 `NonAlloc` 계열 + 레이어 마스크. 콜라이더를 껐다 켜기보다 레이어로 거른다.
- `renderer.material` 로 머티리얼을 인스턴스화하지 않는다 — `sharedMaterial` · `MaterialPropertyBlock`.
- 목표는 적 300 · 중급 Android 60 fps(기획서) — 측정 전 목표이고 실측은 `DEF-M04`. 성능은 추측하지 않고 프로파일러 수치로 말한다.

---

## 12. 저장 · 직렬화 [SAVE]

- 저장 DTO 는 **`[Serializable]` 클래스 + 필드**(public 또는 `[SerializeField]`), 매개변수 없는 생성자. 프로퍼티 · `Dictionary` · 다형성 · 다차원 배열 없음.
  — 왜: Unity 직렬화(JsonUtility · 인스펙터)는 필드만 보고 프로퍼티 · `Dictionary` · 다차원 배열을 지원하지 않는다(근거 1). 어기면 컴파일은 되지만 값이 조용히 빠진다.
- 라이브러리는 **`JsonUtility`**(패키지 0). `Dictionary` · 다형성이 필요해지면 보류 항목으로 `com.unity.nuget.newtonsoft-json` 을 재검토(D-06).
- **포맷 버전 필드 `version` 필수.** 필드를 바꾸면 버전을 올리고 이전 버전 변환 함수 + 변환 테스트(§15). 기존 저장 파일을 못 읽게 되는 변경은 고위험.
- JSON 한 파일(`Application.persistentDataPath`). 쓰기는 임시 파일에 쓴 뒤 바꿔치기, 이전 파일은 `.bak`. 읽기 실패(예외 · 미래 버전 · 깨짐)는 `.bak` → 기본값 순서로 복구하고 로그.
- 저장 시점: 정산 · 강화 구매 · 해금 · 설정 변경 · 앱 백그라운드(`OnApplicationPause(true)`). 매 프레임 저장 금지.
- 저장 I/O 는 **`SaveSystem` 하나만** 호출한다. 다른 코드는 DTO 를 주고받을 뿐 파일을 모른다.
- `PlayerPrefs` 는 쓰지 않는다 — 설정값까지 저장 파일에.
  — 왜: 한 파일이면 백업 · 복구 · 버전 관리가 한 곳이다.
- 저장 데이터 변조 방지(암호화)는 범위 밖 — 오프라인 단일 플레이. 비밀값 · 서명 자료는 git 밖(루트 `CLAUDE.md`).

---

## 13. 로깅 [PERF]

- 로그는 **상태 전이에만**: 런 시작 · 웨이브 · 보스 · 정산 · 저장 · 씬 전환 · 광고 자리. 매 프레임 · 적 · 투사체 · 풀 단위 로그 금지.
  — 왜: `Debug.Log` 는 호출마다 문자열 할당과 스택 추적 캡처가 있어 핫패스에서 프레임을 먹는다.
- 메시지 앞에 `[태그]`(`[Wave]` · `[Save]`). 개발 전용 로그는 Core 의 얇은 래퍼 `GameLog.Dev(...)`(`[Conditional("UNITY_EDITOR")]` · `[Conditional("DEVELOPMENT_BUILD")]`)로 — 릴리스에서는 호출과 인자 식이 함께 빠진다. 문자열 보간은 래퍼 인자에서만.
- 레벨은 Unity 의 셋: `Log`(전이) · `LogWarning`(복구한 이상) · `LogError`(버그 — 게임은 계속). 예외는 `LogException(ex)`.
- 메서드 진입 · 종료 로그, 클래스별 로그 상수는 쓰지 않는다.
- 비밀값 · 기기 식별자는 로그에 찍지 않는다.

---

## 14. 비동기 · 코루틴 [TIME · LIFE]

- 프레임에 걸친 연출 · 대기는 **코루틴**. 파일 · 광고 SDK 콜백 같은 완료 대기는 Unity 6 **`Awaitable`**(`UnityEngine.Awaitable`). `System.Threading.Tasks.Task` · UniTask 는 쓰지 않는다(D-07).
  — 왜: `Awaitable` 은 Unity 가 플레이어 루프에 맞춰 제공하는 비동기 타입이고 패키지가 필요 없다(근거 4).
- `async void` 금지 → `async Awaitable`(이벤트 핸들러만 예외). `async` 메서드에 `Async` 접미는 붙이지 않는다.
- 코루틴은 소유 GameObject 가 비활성화되거나 파괴되면 멈추지만 **`enabled = false` 로는 멈추지 않는다** — 풀로 돌려줄 때 `StopAllCoroutines()` 를 명시한다(근거 4).
- `await` 뒤에는 자신이 파괴됐는지(`this == null`) 확인한 뒤 Unity 객체를 만진다. 씬 전환 뒤 돌아오는 결과는 버린다.
- Unity API 는 메인 스레드에서만. 스레드 · 잡 시스템은 이 게임 범위 밖(필요하면 보류 항목으로).
- 코루틴 메서드 이름은 동사 + `Routine`(`SpawnWaveRoutine`). `StartCoroutine("문자열")` 금지.

---

## 15. 테스트 [TEST]

- Core 의 순수 로직(스탯 · 곡선 · 드래프트 추첨 · 저장 변환)은 MonoBehaviour 에 의존하지 않는 POCO 로 두어 EditMode 로 검사한다.
  — 왜: EditMode 는 0.3초, PlayMode 는 씬이 필요하다(`CLAUDE.md` 「결정론 게이트」).
- 테스트 이름은 `메서드_상태_기대`(`Convert_V1Save_ProducesV2Fields`). 한 테스트에 한 가지 뜻.
- 필수 테스트: 데이터 에셋 검증(모든 `*Def` 로드 · 범위 · 표 대조, §8) · 저장 포맷 변환(§12).
- PlayMode 스모크(자동 선택 + 가속 한 판)는 런 흐름을 바꿨을 때.
- 테스트 어셈블리는 `Defense.Tests.EditMode` · `PlayMode`. Core 의 `internal` 은 `[assembly: InternalsVisibleTo("Defense.Tests.EditMode")]` 로 연다 — 테스트 때문에 public 으로 올리지 않는다.
- 새 동작에 맞춰 단언만 바꾼 테스트는 지적 대상. 실제 연결(wiring)도 테스트에 넣는다.

---

## 16. 에디터 코드 · 빌드 · 플랫폼 [BUILD]

- 에디터 전용 코드(커스텀 인스펙터 · 메뉴 · 임포터)는 `Editor/` 폴더 + 에디터 asmdef(`includePlatforms: Editor`). `#if UNITY_EDITOR` 는 런타임 클래스 안의 보조 한두 줄에만.
- 플랫폼 분기(`UNITY_ANDROID` · `UNITY_WEBGL` · `UNITY_IOS`)는 플랫폼 서비스 클래스 한 곳(`IPlatformService` 구현). 게임 로직에 흩뿌리지 않는다.
- 게이트: 컴파일 오류 0 · 새 경고 0 · EditMode 전부 통과 · (런 흐름 변경 시) PlayMode 스모크 · (빌드 설정 변경 시) 대상 빌드. 명령은 `CLAUDE.md` 「결정론 게이트」 한 곳.
- `-warnaserror` 는 쓰지 않는다 — 패키지 경고로 깨진다. 대신 새 경고 0.
- 패키지는 재배포 가능한 라이선스만. `Packages/manifest.json` 변경은 승인 지점이고 `ASSETS.md` 에 적는다. 외부 코드는 `Assets/ThirdParty/` + 장부.
- `ProjectSettings/` · 빌드 프로필 변경은 기능 커밋과 분리한다. 조건부 컴파일 블록에는 이유 주석.

---

## 17. 에셋 이름

접두 없이 PascalCase 하나. 종류는 폴더와 접미가 말한다. 띄어쓰기 · 한글 · 특수문자 없음(명령줄 · WebGL 경로). 변형은 `_접미` 하나만.

| 종류 | 폴더 | 예 |
|---|---|---|
| 데이터 에셋 | `Data/<영역>/` | `LanternDef.asset`(클래스 `WeaponDef`) · `NightCurve.asset` |
| 프리팹 | `Defense/<영역>/` | `EnemyGrunt.prefab` · 변형 `EnemyGrunt_Elite.prefab` |
| 씬 | `Scenes/` | `Boot.unity` · `Island.unity` · `Night.unity` |
| 모델 · 머티리얼 · 텍스처 | `Art/<영역>/` | `TowerBase.fbx` · `TowerBase.mat` · `Palette.png` — 같은 대상은 같은 이름 |
| 애니메이션 | `Art/<영역>/` | `EnemyGrunt_Walk.anim` |
| 오디오 | `Audio/Sfx/` · `Audio/Music/` | `Hit.wav` · `Night.ogg` |

- 외부 에셋은 원본 이름을 유지하고 `ASSETS.md` 에 적는다(출처 추적).

---

## 18. UI · 입력 [UI · INPUT]

- UI 프레임워크(uGUI 대 UI Toolkit)는 `DEF-M01` 전에 정한다 — 그때 이 절을 채운다(패널 상태 · 버튼 조건 · 연출 순서 · 세이프 영역 · 해상도 · 화면 방향).
- 지금 정해진 것: 입력은 Input System 패키지(템플릿 기본) · 세로 · 한 손(기획서 3절). 사용자 문구는 문자열 표(데이터 에셋)에서 — 코드 리터럴 금지.

---

## 19. 주석 · 문서

- public 타입 · 메서드에 `<summary>`(한국어). `<param>` · `<returns>` 는 이름만으로 모를 때만. Unity 메시지 메서드 · 테스트 메서드는 생략.
- 람다 · 코루틴 블록은 역할 한 줄. 「무엇」이 아니라 「왜」를 쓴다.
- 인라인 변경 표식(`@id 날짜`) · 파일 헤더 이력은 없다(§2).
- `// TODO(H-nn 또는 DEF-Mnn): …` — Planning 보류 항목 · 마일스톤 번호와 잇는다. 번호 없는 TODO 는 남기지 않는다.
- 쓰지 말아야 할 메서드는 `[Obsolete("대신 X")]`.

---

## 근거

| # | 사실 | 출처 | 확인 |
|---|---|---|---|
| 1 | Unity 6000.3 은 C# 9.0, `init` 세터 미지원, 레코드는 직렬화 불가. 직렬화는 public 또는 `[SerializeField]` 필드만(static · const · readonly 제외), 프로퍼티 · `Dictionary` · 다차원 배열 미지원. JsonUtility 는 필드만, `Dictionary` 불가 | Unity 매뉴얼 6.3 — [C# compiler and language version reference](https://docs.unity.com/en-us/engine/6000.3/manual/programming-environment/overview-of-dot-net-in-unity/csharp-compiler) · [Serialization rules](https://docs.unity.com/en-us/engine/6000.3/manual/programming-environment/code-reload-serialization/script-serialization/rules) · [JSON serialization](https://docs.unity.com/en-us/engine/6000.3/manual/programming-environment/code-reload-serialization/script-serialization/json-serialization) | △ 2026-10-30 web-fetch |
| 2 | `UnityEngine.Object` 의 `==` 는 관리 참조와 네이티브 포인터를 함께 검사한다. `?.` · `??` · `is null` 은 사용자 정의 연산자를 부르지 않는다 | [Object.operator ==](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/object/op-equality)(6.3) · C# 언어 규칙([null 조건 연산자](https://learn.microsoft.com/dotnet/csharp/language-reference/operators/member-access-operators#null-conditional-operators--and-)) | △ · C# 쪽은 세션 지식 |
| 3 | `Debug.Assert` 는 `[Conditional("UNITY_ASSERTIONS")]` — 심볼이 없으면 호출이 빠진다 | [Debug.Assert](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/debug/assert)(6.3) | △ |
| 4 | 코루틴은 `IEnumerator` 반환. GameObject 비활성화 · 파괴로 멈추고 `enabled = false` 로는 멈추지 않는다. 비동기는 Unity 자체 `Awaitable` | [Coroutines](https://docs.unity.com/en-us/engine/6000.3/manual/scripting/coroutines-section/coroutines) · [Async/await support](https://docs.unity.com/en-us/engine/6000.3/manual/scripting/programming-distribute-work-threads/async-await-support)(6.3) | △ |
| 5 | 에디터에서는 편집 · 플레이 모드 모두 ScriptableObject 에 저장할 수 있고, 플레이어에서는 읽기만 된다 | [ScriptableObject](https://docs.unity.com/en-us/engine/6000.3/manual/scripting/get-started/fundamental-unity-types/class-scriptable-object)(6.3) | △ |

원문(EasyCheck 판)과 절별 처리 · 결정 경위는 Planning `P00_환경_체계_로깅/01_검토/검토서_20261030_코딩표준.md` · `결정기록.md` D-06 · D-07.
