## 기본 원칙

1. **가독성을 최우선으로 삼는다.** 코드는 그 자체가 문서의 역할을 해야 한다.
2. 합당한 이유가 없는 한, **IDE 자동 서식을 따른다.** (VS `Ctrl + K + D`)
3. **일관성을 유지한다.** 기존 프로젝트의 코딩 스타일을 존중한다.

---

## I. 명명 규칙

| 대상 | 규칙 | 비고 |
|------|------|------|
| 클래스 / 구조체 | PascalCase | |
| 인터페이스 | `I` + PascalCase | |
| 열거형(Enum) | PascalCase | 비트 플래그는 `[Flags]` + 16진수/비트 시프트 |
| private 필드 | `_camelCase` | `readonly`도 동일 |
| 상수 (`const`, `static readonly`) | UPPER_SNAKE_CASE | |
| 프로퍼티 | PascalCase | 대응 private 필드는 프로퍼티 바로 위에 선언 |
| 지역 변수 / 매개변수 | camelCase | |
| 메서드 | PascalCase | 동사 + 명사 형태 |
| bool 반환 메서드/프로퍼티 | `Is`, `Can`, `Has`, `Should` 접두사 사용 | |
| 줄임말(축약어) | 단독 사용 시 대문자, 뒤에 단어 올 때 파스칼/카멜 | 예: `OrderID`, `HttpCode` |
| 네임스페이스 | PascalCase | 루트: `MinervaSoft` |

- 반복문 이외의 변수에는 의미 있는 이름을 사용한다.
- getter/setter 메서드 대신 **프로퍼티**를 사용한다.

### 외부/내부 경계 네이밍

| 구분 | 네이밍 | 적용 수단 |
|------|--------|----------|
| JSON Body | snake_case | `JsonNamingPolicy.SnakeCaseLower` 전역 설정 |
| Query Parameter | snake_case | `[FromQuery(Name = "...")]` 명시 (단일 단어는 생략 가능) |
| DB 컬럼 | snake_case | Dapper 매핑 또는 `[Column("...")]` |
| Route Parameter | kebab-case / lowercase | ASP.NET Core 기본 |
| C# 프로퍼티 / 변수 | PascalCase / camelCase | C# 표준 |

- JSON Body는 전역 설정으로 자동 변환되므로 개별 `[JsonPropertyName]`은 불필요하다.
- 기존 API 쿼리 파라미터는 하위 호환성을 고려하여 점진적으로 정규화한다.

---

## II. 파일 구조

- 모든 소스 파일 상단에 **블록 주석 헤더**(작성자, 작성일, 목적, 변경 이력)를 작성한다.
- **클래스는 독립된 소스 파일**에 배치하며, 파일 이름은 클래스 이름과 대소문자까지 일치시킨다.
- Partial 클래스 파일명: `클래스명.세부항목.cs` (예: `ScanFacade.GunInfo.cs`)
- `using` 문 순서: ① 프로젝트 내부 네임스페이스 → ② `System` 네임스페이스

---

## III. 클래스 구조

### 멤버 등장 순서

① 상수 → ② 이벤트 → ③ 정적 멤버 → ④ 프로퍼티(+대응 필드) → ⑤ 기타 멤버 변수 → ⑥ 생성자 → ⑦ public 메서드 → ⑧ private/protected 메서드 → ⑨ Dispose

- 각 그룹은 **80자 구분선 주석**으로 구분하고, 그룹 간 **2행의 빈 줄**을 둔다.
- 개별 멤버에는 `<summary>` XML 주석을 작성한다.
- `#region`은 되도록 사용하지 않는다. 예외: 메서드 내부 대형 로직 블록.
- 연관 있는 메서드/변수끼리 그룹을 짓는다.

---

## IV. 서식

- 탭: VS 기본값 또는 **띄어쓰기 4칸**
- 중괄호: **Allman 스타일** (새 줄에 열기), 한 줄이라도 중괄호 사용
  - 예외: 단일 흐름 제어문(`return`, `continue`, `goto`)은 중괄호 생략 허용
- 관련 상수/변수의 할당 값은 **수직 정렬**한다.

---

## V. 변수 사용

- `var` 키워드는 **사용하지 않는다.** 단, `new`로 타입이 명확하거나 `IEnumerable` 등은 허용.
- **Variable Shadowing 금지.**
- `System.Collections` 대신 **`System.Collections.Generic`** 사용.
- 지역 변수는 사용하는 코드와 **최대한 가까운 곳**에 선언한다. 반환값 변수(`retval`)는 메서드 시작부.

---

## VI. 함수 오버로딩 / 디폴트 매개변수

- 디폴트 매개변수는 비트 패턴이 0인 값(`null`, `false`, `0`)을 사용한다.
- 축약형 오버로딩을 제공하여 자주 사용되는 호출을 편리하게 한다.

---

## VII. 어트리뷰트

- 모든 클래스·인터페이스·주요 메서드에 **`[Developer("@id", "날짜")]`** 어트리뷰트를 적용한다.
- 커스텀 어트리뷰트는 `sealed`로 선언하고 `AttributeUsage`를 명시한다.

---

## VIII. XML 문서 주석

- 모든 `public`, `protected` 멤버에 XML 문서 주석(`///`)을 작성한다.
- `<summary>`, `<param>`, `<returns>` 태그를 일관되게 사용하며, 한국어로 작성한다.

---

## IX. 예외 처리 및 데이터 유효성

- **외부/내부 경계에서 유효성을 검증**하고, 내부로 들어온 데이터는 유효하다고 가정한다.
- 내부 함수에서 예외를 던지지 않으려 노력한다.
- `catch (Exception ex)` 일괄 처리 대신 **구체적인 예외 타입을 각각 처리**한다.
- 예외 catch 시 **반드시 로그**를 남긴다. 리소스 정리 코드에서는 빈 catch 허용.
- `enum` + `switch`의 `default:`에서 `NotImplementedException` 던지기는 허용.

---

## X. 로깅 패턴

- 모든 public 메서드에 **시작(`>>`) / 종료(`<<`) 로그**를 기록한다.
- 클래스별 `LOG_DOC`(로그 타입), `PAD_DOC`(패딩) 상수를 정의한다.
- 예외 로그는 `Exception` 객체를 포함하며, 레벨 1(심각)~9(경미)를 사용한다.

---

## XI. 리소스 관리 / Dispose 패턴

- 관리/비관리 리소스 사용 클래스는 **표준 Dispose 패턴**(`Dispose(bool)` + 파이널라이저)을 구현한다.
- **`using` 선언(C# 8.0) 금지** → `using` 블록 문을 사용한다.

---

## XII. 디자인 패턴 가이드

- **Facade 패턴**: 비즈니스 로직은 `internal sealed partial` Facade 클래스로, 관심사별 partial 파일 분리.
- **Template Method 패턴**: 공통 알고리즘 골격은 추상 기본 클래스에, 구현은 하위 클래스에.
- **Wrapper/Adapter 패턴**: 네이티브 DLL은 `sealed` 래퍼 + 공통 인터페이스. P/Invoke는 `private static extern`.
- **싱글톤 패턴**: 인프라 클래스에서 정적 프로퍼티를 통해 접근.

---

## XIII. 인터페이스 / 클래스 한정자

- ISP에 따라 인터페이스는 **좁고 명확**하게 설계한다.
- 리소스 관리가 필요한 인터페이스는 `IDisposable`을 상속받는다.
- 상속을 의도하지 않는 클래스는 **`sealed`** 로 선언한다.
- 외부 노출이 불필요한 클래스는 **`internal`** 로 선언한다.

---

## XIV. 데이터 매핑

- DB 컬럼 매핑에 `[FieldMapping]` 어트리뷰트를 사용한다.
- 데이터 클래스는 `MappedFieldBase`를 상속받아 리플렉션 기반 매핑을 활용한다.

### 응답 DTO 참조 표시 이름 규약

- 목록/상세 응답 DTO에서 사람이 읽는 이름을 가진 엔티티(User, Site, ShiftType, LeaveType, Role, Flow 등)를 참조하는 모든 `*_guid`(C# `*Guid`)는 짝이 되는 표시 이름 `*_name`(C# `*Name`)을 함께 직렬화한다.
  - 예: `UserGuid` → `UserName`, `SiteGuid` → `SiteName`, `CreatedByUserGuid` → `CreatedByUserName`.
- 표시 이름은 EF 네비게이션 속성을 조회 쿼리에서 `.Include` 한 뒤 매퍼에서 `엔티티?.Name`으로 채운다. 미배정/미로드 시 `null`을 허용한다.
- 순수 레코드 참조(`attendance_guid`, `approval_request_guid`, `ledger_entry_guid` 등 사람이 읽는 이름이 없는 식별자)는 본 규약 대상이 아니다.
- Schedule 도메인 DTO(`site_name`/`building_name`/`team_name`/`created_by_name`)를 표준 레퍼런스로 한다.

---

## XV. Null 처리

- public 함수의 매개변수와 반환값에서 **`null`을 허용하지 않는 것을 추구**한다.
- `null`을 허용/반환하는 경우 이름 뒤에 **`OrNull`** 을 붙인다.
- null 조건부 연산자(`?.`)는 사용 가능. **null 병합 연산자(`??`)는 금지.**

---

## XVI. 보안

- SQL은 **파라미터화된 쿼리**를 우선 사용. 문자열 결합 시 싱글 쿼트 이스케이프 필수.
- P/Invoke 메서드는 `private`으로 선언하고 공개 래퍼를 통해 접근한다.

---

## XVII. C# 기능 사용 지침

**금지**: `using` 선언(C# 8.0), `??` 연산자, target-typed `new()` (C# 9.0)
**필수**: `new` 키워드 뒤에 명시적 자료형 표기, `out` 매개변수는 별도 라인 선언 (단순한 경우 인라인 허용)
**권장**: `CallerMemberName`/`CallerFilePath`/`CallerLineNumber`, `ConcurrentQueue<T>`, `StringBuilder`, `params`

---

## XVIII. 빌드

- Release 빌드에서 **경고를 오류로 처리** 설정.
- 조건부 컴파일(`#if`)은 최소화하고 주석을 남긴다.

---

## XIX. 주석 규칙

- 코드 변경 시 **`@devman 날짜`** 인라인 주석, 범위는 `>>` / `<<`로 표시.
- 향후 개선: **`TODO: @개발자ID 날짜`** 형식.
- 사용 비권장 메서드: **`[Obsolete("사유")]`** 어트리뷰트 적용.

---

## XX. 직렬화

- 직렬화용 클래스에 특정 라이브러리 전용 어트리뷰트를 넣지 않는다.
- **public 자동 프로퍼티**만 사용. 읽기 전용이 필요하면 public 메서드로 대체.
- public 생성자는 **매개변수 없는 것 하나만** 둔다.
- 직렬화 함수는 직접 호출하지 않고 **wrapper 함수**를 통해 자료형을 통제한다.

---

## XXI. 프로젝트 구조

- **레이어**: Application → Common → Core, DbHelper → Core (상위→하위 의존)
- SQL 쿼리는 XML 파일에 외부화하여 `QueryManager`로 관리.
- 외부 설정은 INI 파일로 관리하고, 설정값 없을 시 기본값 사용.
- 빌드 출력: `z.release/<ProjectName>/Current/`에 자동 복사.

---

## XXII. 기타

- 조건 가정 코드에 **`Debug.Assert()`** 사용.
- **`async void` 금지** → `async Task` 사용. (이벤트 핸들러만 예외)
- 컨트롤 이름(`x:name`)은 필요한 경우에만 지정.
