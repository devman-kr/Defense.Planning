---
id: 20261030-p00-codereview-s1b-sensor-a-round2
title: 코드 리뷰 P00 S1b 2라운드 — 센서 A 원본 (수정 커밋 점검)
summary: 표준 수정 커밋을 다시 읽은 2라운드 센서 A 의 지적 17건 — D-06 추기 확인 대기 표시 누락, §7.10 과 §9.6 어긋남 등 — 과 처리표 고침 표본 12건 검산(부분 고침 · 다르게 고침 포함) 결과.
doc_type: review
status: final
lifecycle: static
created: 2026-10-30
updated: 2026-10-30
work_unit: P00
---
리뷰어 모델: Sonnet 5.5 (지시의 원본 기준 Opus 5.5 와 다르다). 읽기만 했고 저장소 파일은 건드리지 않았다. 검증용 임시 프로젝트는 scratchpad 에서 돌렸다.

표기: 표준 = `_템플릿/Unity_csharp_coding_standards.md`, 템플릿 = `_템플릿/Unity_CLAUDE.md`, ec = `_템플릿/Unity_.editorconfig`, 가이드 = `코드리뷰_가이드.md`, 검토서 = `P00_환경_체계_로깅/01_검토/검토서_20261030_코딩표준.md`, 결정기록 = `P00_환경_체계_로깅/결정기록.md`.

| # | 종류 | 심각도 | 기원 | 유형 | 파일:줄 | 실패 시나리오(입력 → 잘못된 결과) | 확신 |
|---|---|---|---|---|---|---|---|
| 1 | issue | important | new | 결정기록 정확성 — 사용자 승인 행에 승인 안 된 변경이 「확인 대기」 표시 없이 들어감 | 결정기록:14 (D-06 추기) ↔ 결정기록:15 (D-07 추기) · 검토서:95 | D-06 은 「사용자(권장안 전체 승인)」 행인데 추기로 「⑤ `PlayerPrefs` 는 설정값도 쓰지 않는다」를 넣었다. D-06 ⑤ 원문에는 `PlayerPrefs` 범위가 없고(반론 D 도 인정), 이 변경은 승인 지점 2 에서 사용자가 다시 본다고 처리.md TOOL.08 이 적었다. D-07 추기에는 「사용자 확인 대기」가 있고 D-06 추기에는 없다 → 결정기록만 읽은 다음 세션은 `PlayerPrefs` 금지를 사용자 승인 결정으로 읽는다. | confirmed |
| 2 | issue | important | new | 「사용자 확인 대기」 목록 누락 — 센서 수정으로 생긴 새 규칙 5건이 검토서 4.5 · D-07 비고에 없음 | 검토서:99-101 · 결정기록:15 ↔ 표준:169 (§11.4), :202 (§14.1), :206 (§14.4), :126 (§7.10), :117 (§7.2) | 확인 대기 목록은 8개뿐이다. 목록에 없는 규칙: ① §11.4 `MaterialPropertyBlock` 금지(수정 전 본문은 MPB 를 권장했다 — 방향 반전) ② §14.1 「SDK 가 `Task` 를 주면 `await` 허용(D-07)」 ③ §14.4 `destroyCancellationToken` 을 넘긴다 ④ §7.10 정적 초기화 수단을 `SubsystemRegistration` 어트리뷰트로 지정 ⑤ §7.2 첫 구독을 `Start` 로. 사용자가 승인 지점 2 에서 보는 목록이 불완전하다. | confirmed (grep: 검토서 · 결정기록에 `MaterialPropertyBlock` · `destroyCancellationToken` · `RuntimeInitialize` 0건, `Task`·`Awaitable` 은 검토서:136 미결 항목뿐) |
| 3 | issue | important | new | §7.10 수정이 §9.6 과 어긋남 — 런 재시작 때 정적 상태 초기화 자리가 사라짐 | 표준:126-127 ↔ :150 | 센서 #25 수정으로 §7.10 은 「static 은 씬 로드로 초기화되지 않는다. 초기화는 `[RuntimeInitializeOnLoadMethod(SubsystemRegistration)]` 한 곳에」가 됐다. 이 콜백은 앱 · 플레이 모드 시작 때 한 번만 돈다. 그런데 §9.6 은 「씬 전환 · 재시작의 초기화 순서(정적 상태 → 풀 → …)는 부트스트랩 한 곳에」다. 수정 전 §7.10 은 「씬 전환 · 재시작 때 … 부트스트랩 한 곳」이라 §9.6 과 맞았다. 규칙 머리글(씬 로드)과 「왜」·근거 9(도메인 리로드를 끈 플레이 모드 세션 사이)는 여전히 다른 사건이다. 재시작 뒤 static 이벤트 구독자가 남아 이벤트가 두 번 불려도 두 절 어느 쪽도 그걸 잡는 곳을 가리키지 않는다. | confirmed (본문 대조 · 근거 9 페이지는 플레이 모드 세션만 말함) |
| 4 | question | important | new | §7.2 「첫 구독은 `Start` 에서」가 풀 재사용(재활성화)을 못 덮음 | 표준:117 ↔ :147-148 | 규칙은 「`OnEnable`·`OnDisable` 짝」인데 수정으로 「주입 참조가 필요하면 첫 구독은 `Start`(또는 `Init`), 해제는 그래도 `OnDisable`」이 됐다. 풀(§9.1 · §9.3)에서 `SetActive(false)` → `OnDisable` 에서 해제 → 다시 `SetActive(true)` 하면 `Start` 는 다시 돌지 않고 `OnEnable` 은 「첫 구독은 `Start`」라 구독하지 않는다 → 재사용된 적이 이벤트를 영영 못 받는다. 초기화 여부 플래그로 `OnEnable` 이 구독하라는 문장이 없다. | plausible (Unity 메시지 순서 일반 지식 · 파일 문장으로 확인, 코드 실행은 안 함) |
| 5 | issue | nit | new | `.editorconfig` 주석의 인과 설명이 틀림 — `applicable_accessibilities = *` 추가가 `const` 우선을 만든 것이 아님 | ec:43-44, :48-49, :55-56 | 주석은 「접근성을 적은 규칙이 우선하고 그다음 한정자 … 모든 심볼 그룹에 접근성을 적어 const · static readonly 가 private 필드 규칙에 밀리지 않게 한다」다. .NET SDK 10.0.403 Roslyn 으로 수정 전(6aefbe1) 파일과 수정 후 파일에 `private const int privBad`, `private static readonly int _badSr`, `private int badField` 를 넣고 `dotnet_diagnostic.IDE1006.severity = warning` 으로 빌드했다. 결과가 동일하다(const 는 UPPER_SNAKE 위반으로, static readonly 는 「`_` 접두 불가」로, 일반 private 는 「`_` 누락」으로). 즉 수정 전에도 const 가 이겼고, 관찰된 순서는 「`*` + `const` 규칙이 `private` 규칙을 이김」이라 주석의 「접근성 먼저」와 반대다. `*` 추가 자체는 MS 문서상 유효하고(Required: Yes) 무해하다. 틀린 것은 주석의 「왜」 · 순서 설명이다. Rider 의 구현은 확인 못 함. | confirmed (Roslyn 실측) |
| 6 | issue | nit | new | `csharp_prefer_braces = when_multiline` 이 §4.2 의 주 규칙(한 줄 블록에도 중괄호)을 IDE 에서 제안하지 않음 | ec:27, :32 ↔ 표준:73 | §4.2 는 「한 줄 블록에도 중괄호. 예외는 return·continue·break」, 「.editorconfig 는 제안 수준으로 둔다」다. SDK 10.0.403 에서 `if (a) Foo(1);` 와 `for (...) Foo(i);` 를 넣고 `true:warning` 과 `when_multiline:warning` 을 비교했다. `true` 는 한 줄 `if`·`for` 와 한 줄 `return` 을 전부 지적하고, `when_multiline` 은 여러 줄 `if` 하나만 지적한다. MS 문서의 예시도 `when_multiline` 에서 `if (test) this.Display();` 를 허용한다. 「제안 수준」이면 `true:suggestion` 이 §4.2 에 더 가깝다. | confirmed (실측 + IDE0011 문서) |
| 7 | issue | nit | new | Unity YAML 섹션의 `insert_final_newline = false` 는 「손대지 않음」이 아니라 「끝 개행 없음」 선언 | ec:12-15 | 실제 `Defense.Unity` 의 `SampleScene.unity` · `Readme.asset` · `*.meta` · `ProjectSettings/ProjectVersion.txt` 는 모두 마지막 바이트가 `0a`(개행)다. EditorConfig 명세는 `false` 를 「끝 개행이 없도록 보장」으로 정의하고, 이를 엄격하게 구현한 편집기(예: dotnet-format 계열 · vim 플러그인)는 개행을 제거할 수 있다. 주석의 의도(재직렬화 diff 방지)와 반대다. 첫 섹션이 이제 이 확장자를 안 잡으므로 이 섹션 자체가 없어도 같다 — 두려면 `unset` 이 안전하다. 편집기별 실제 동작은 실행해 보지 않았다. | plausible (파일 끝 바이트는 확인, 편집기 동작은 미실행) |
| 8 | issue | nit | new | §6.4 가 제네릭 `T` 를 일괄로 「Unity 의 `==` 가 아니다」라 함 | 표준:102 | C# 샌드박스에서 `==` 를 오버로드한 클래스 `Obj` 로 확인했다. `where T : Obj` 인 제네릭의 `t == null` 은 사용자 정의 `==` 를 호출했고(출력 `USER==`), 제약 없는 `T` 와 인터페이스 · `object` 는 참조 비교였다. `where T : Component`/`UnityEngine.Object` 제약 제네릭(흔함)은 Unity 의 `==` 가 맞게 동작하는데 규칙은 그것도 우회 대상으로 쓴다. 「제약 없는 `T`」로 좁혀야 한다. | confirmed (C# 실측 · Unity 에서는 같은 메커니즘으로 추정) |
| 9 | question | nit | new | §14.4 `destroyCancellationToken` 을 넘기면 취소 시 예외가 나는데 처리 규칙이 없음 | 표준:206 ↔ :103-104, :104 | 수정 전에는 「`await` 뒤 `this == null` 확인」뿐이었고, 수정으로 「`await` 에는 `destroyCancellationToken` 을 넘기고, 돌아온 뒤 파괴됐는지 본다」가 됐다. 토큰이 취소되면 await 는 돌아오지 않고 `OperationCanceledException` 을 던진다. §6.6 은 「catch 하면 반드시 로그」라 취소를 로그에 남기는지 삼키는지 불명이다. 「돌아온 뒤 `this == null`」 확인도 토큰을 쓰면 도달하지 않는 경로가 된다. | plausible (Unity 의 `Awaitable` 취소 예외 처리 세부는 못 열어봄) |
| 10 | issue | nit | new | 표준 §14.1 의 「(D-07)」 인용이 D-07 에 없는 허용을 가리킴 | 표준:202 ↔ 결정기록:15 (④) | D-07 ④ 는 「`Task` · UniTask 안 씀, `async void` 금지 유지」뿐이다. 「SDK 가 `Task` 를 주면 `await` 는 허용」은 D-07 에 없는 예외인데 출처가 D-07 로 적혀 있다 → 사용자 결정으로 오독된다(#2 와 같은 뿌리). | confirmed |
| 11 | issue | nit | new | 센서 #24 처리 「나머지는 본문에 ‘작성 세션이 더한 규칙’ 표시」가 일부만 됨 | 표준:29, :38, :86, :100 (표시 없음) ↔ :54, :160, :208 (표시 있음) | 검토서:99 가 나열한 8개 중 본문 표시는 `Resources/`·`StreamingAssets/`(§2.6), `DateTime.Now`(§10.5), 문자열 `StartCoroutine`(§14.6) 3개뿐이다. `??=`(§5.5), `ReferenceEquals`(§6.3), 코루틴 `Routine` 접미(§1 표), 「애매하면 Game」(§1.1) 은 표시가 없다. | confirmed |
| 12 | issue | nit | new | 표준 읽는 법의 「폴더 · 어셈블리 … `CLAUDE.md` 에만 있고」가 §15.5 · §17 · 템플릿과 중복되는 새 문장을 만듦 | 표준:5, :219, :236-246 ↔ 템플릿:39-40 | 센서 #9(중복 0)의 수정 결과로 표준에 「폴더 · 어셈블리는 저장소 `CLAUDE.md` 에만」이라 적었다. 그런데 §15.5 가 테스트 asmdef 이름 3개(`Devman.Core.Tests.EditMode` · `Defense.Tests.EditMode` · `PlayMode`)와 위치(Core 폴더 안)를 적고, 템플릿:39 도 같은 이름 3개를 적는다(이번 커밋에서 새로 생긴 중복). §1.1 「Core 는 Game 을 참조하지 않는다」도 템플릿:40 과 같은 문장으로 남아 있다. asmdef 이름이 바뀌면(S1c) 두 곳을 고쳐야 한다. | confirmed |
| 13 | issue | nit | pre-existing(센서 #34 수정이 반쪽) | 표준은 「코드 폴더마다 asmdef」로 고쳤는데 템플릿은 「폴더마다 asmdef」 그대로 | 템플릿:40 ↔ 표준:53 | 템플릿:39 의 폴더 목록에 `Data/` · `Art/` · `Scenes/` · `Audio/` · `ThirdParty/` 가 있어 「폴더마다 asmdef」는 코드 없는 폴더에도 asmdef 를 요구하는 것으로 읽힌다. S1c 가 이 문장을 Defense.Unity/CLAUDE.md 로 복사한다. | confirmed |
| 14 | question | nit | new | 읽는 법 문장(「대괄호가 없는 절(이름·서식·주석)은 리뷰 영역이 아니라 IDE·리뷰어 취향 밖의 약속」)이 의미 불명 + 괄호 열거가 실제와 다름 | 표준:5 ↔ :19-41, :58-66 | 「리뷰 영역이 아니라」면서 「지키는지는 코드 리뷰가 본다」(같은 문단)와 충돌하는 것처럼 읽힌다. 열거(이름 · 서식 · 주석)에 §0 · §3(클래스 구조) 이 없다. 또 대괄호를 뗀 §1 안에 가이드 부록 A 의 `BUILD`(asmdef 참조 Core → Game 금지 — §1.1)와 `CONTRACT`(기획서 표 ≠ 에셋 필드 — §1.3)에 정확히 해당하는 규칙이 있고, §15.5 는 §1.1 을 인용한다. 영역 열은 작성 세션이 따로 매기므로(가이드:148) 집계는 안 깨지지만 독자가 §1.1 위반을 어느 영역으로 적을지 모른다. | confirmed (본문) · 영향은 plausible |
| 15 | question | nit | new | 가이드 7절 새 문장 「루프 ② 의 목적지는 둘이다」인데 루프 ② 원문은 목적지 하나 | 가이드:118 ↔ :119 | :118 은 ②를 「표준에 없는 유형 → 표준에 한 줄 / 있는 유형 → 결정론 층」 둘로 쓰지만, 바로 아래 루프 본문 ②는 「결정론 층으로 내린다」만 적고 ③ 「내린 것은 기준에서 지운다」로 이어진다. 루프를 따라 읽는 계획 세션은 표준 승격 경로를 ②에서 만나지 못한다. | confirmed |
| 16 | nitpick | nit | new | §9.3 의 「(§14.3)」 인용이 인용 내용(‘띄운 쪽이 `StopCoroutine`’)을 담고 있지 않음 | 표준:147 ↔ :205 | §14.3 은 「컴포넌트만 끄는 경우는 `OnDisable` 에서 `StopAllCoroutines()`」만 말한다. 다른 객체가 띄운 코루틴을 띄운 쪽이 `StopCoroutine` 한다는 문장은 어느 절에도 없다. 번호는 존재하지만 내용이 안 맞는 참조다. | plausible |
| 17 | nitpick | nit | new | §15.1 「EditMode 는 약 0.3초」가 템플릿의 기본 경로(batchmode ≈ 20초)가 아닌 열린 에디터 수치 | 표준:214-215 ↔ 템플릿:53, :64 | 템플릿 게이트에서 batchmode(기본)는 「약 20초」, 0.3초는 `unity command`(에디터 열림) 기준이다. 표준의 「CLAUDE.md 「결정론 게이트」 실측」 인용은 모드 구분 없이 0.3초만 쓴다. PlayMode 는 템플릿에서도 미실측이다. | confirmed |

## 확인하지 않은 것 · 추정한 것

- 근거 표 7~11행은 링크를 열어 대조했다.
  - 7 (naming-scripts): 일치. 다만 해당 문장은 `MonoBehaviour` · `ScriptableObject` 파생에 한정되고, 표준 §2.1 「왜」는 이 한정을 빼고 썼다.
  - 8 (SRP Batcher incompatible): 「`MaterialPropertyBlock` 을 붙이면 비호환」, `Graphics.RenderMeshInstanced` 언급, 「동일 메시 다수는 GPU 인스턴싱이 더 효율적일 수 있다」까지 일치.
  - 9 (domain reloading): static 값 · 이벤트 구독자가 플레이 모드 세션 사이에 남는다는 점과 `SubsystemRegistration` 예시가 일치. 이 페이지는 씬 로드를 말하지 않는다(#3).
  - 10 (stack trace): 「resource-intensive」, 「배포 시 켜지 마라」, None/ScriptOnly/Full 이 일치.
  - 11 (10000 Update): Unity 5.2.2f1 · iOS 9 이므로 「2015년 5.2」가 맞고, 네이티브→관리 호출 비용과 「수천 개 Update 호출은 눈에 띈다」가 일치.
- 근거 1~6 은 이번 커밋이 바꾼 「왜」가 아니어서 다시 열지 않았다. 근거 3 의 MS Learn 링크 3개 본문은 열지 않았다.
- `.editorconfig` 를 확인한 방식.
  - 글롭: Python editorconfig-core 로 `[*.{cs,md,json,asmdef,yml,yaml,editorconfig,gitignore,gitattributes}]` 가 `.gitignore` · `.gitattributes` · `.editorconfig` 를 잡고, Unity YAML 섹션이 `.meta` · `.cs.meta` 까지 잡는 것을 확인했다.
  - `applicable_accessibilities = *`: MS 문서에서 유효한 값임을 확인했다.
  - `when_multiline`: MS 문서(IDE0011)에서 유효한 값임을 확인했다.
  - 명명 규칙과 중괄호 규칙은 .NET SDK 10.0.403 Roslyn 으로만 실측했다. Rider · VS Code C# Dev Kit 에서의 동작은 못 봤다.
  - `new()` · `using var` · `??` 는 이 설정에서 지적되지 않는 것을 확인했다. 머리 주석(「금지는 리뷰가 본다」)은 맞다. `var e = 5` 는 IDE0008 로 지적된다.
- #4 는 파일 문장과 Unity 메시지 순서 일반 지식으로 추정했고 실행하지 않았다.
- #9 의 `Awaitable` 취소 예외가 로그로 남는지는 Unity 문서를 열지 않았다.
- 표준 §16.3 의 `-warnaserror` 주장 · `Physics.*NonAlloc` · `UNITY_ASSERTIONS` 릴리스 정의 여부는 열지 않았다(이번 커밋 변경 밖).
- 새 「왜」중 §7.1 백킹 필드 이름(표에 「세션 지식」으로 명시) · §6.7 예외 「왜」(관찰 문장) · §12.6 「왜」는 URL 근거가 없고 열지도 않았다. 표준이 근거 없음을 표시해 두었다.
- 1라운드에서 닫힌 항목(#8 PlayerPrefs 의도, #19 분량 의도, #39 범위 밖)은 다시 내지 않았다. #1 은 그 의도 결정을 기록하는 방식만 다룬다.

## 처리 검산 표본 12건 (처리.md 「고침」 행)

- TOOL.01 (blocking) — 맞게 고침. §3.5 Template Method, §7.4 인터페이스 + 모의 구현(기획서 8절 모의 광고), §7.5 `event Action`/`UnityEvent`, §7.9 `sealed` + `[AttributeUsage]` 가 모두 존재하고 내용이 일치한다.
- TOOL.02 (blocking) — 맞게 고침. §13.2 「메시지는 한국어, 앞에 `[태그]`」(표준:193).
- TOOL.03 — 맞게 고침. §2.1 · §2.2 가 매뉴얼 문장(여러 클래스 · partial)과 일치한다(근거 7 직접 대조). 「클래스가 하나면」이 MonoBehaviour · ScriptableObject 한정임을 빼고 썼다는 정도만 다르다.
- TOOL.09 — 부분만 고침. §2.5 · §16.3-4 · §17 머리가 `CLAUDE.md` 를 가리키는 것은 맞다. 그러나 표준 §1.1 「Core 는 Game 을 참조하지 않는다」↔ 템플릿:40 같은 문장이 남아 있고, §15.5 테스트 asmdef 이름은 이번에 새로 중복됐다(#12).
- TOOL.13 — 동작은 맞지만 이유가 틀림. `*` 추가로 새로 고쳐진 것은 없고 수정 전 파일도 같은 결과를 낸다. 주석의 우선순위 설명은 관찰과 반대다(#5).
- TOOL.16 — 고쳤으나 새 구멍을 만듦. 주입 전 null 은 해결했지만 풀 재활성화 경로의 구독이 빠질 수 있다(#4).
- TOOL.18 — 고침. §12.4 동기 저장, §14.1 `AwaitableCompletionSource` 는 일치한다. 다만 「SDK `Task` 의 `await` 허용(D-07)」은 D-07 에 없는 예외다(#10).
- TOOL.20 — 고침. 가이드 7절의 두 목적지 명시와 템플릿 「검토 기준」 4줄 → 표준 참조 1줄 + 고유 2줄이 확인된다. 루프 ② 원문은 갱신되지 않았다(#15).
- TOOL.24 (nit) — 부분만 고침. `Async` 접미 규칙 삭제는 확인된다(`Async` 는 근거 표 외 0건). 본문 표시는 3/7이다(#11).
- TOOL.25 (nit) — 다르게 고침. §7.10 이 `SubsystemRegistration` 으로 바뀌며 §9.6 과 어긋난다(#3).
- TOOL.27 (nit) — 맞게 고침. §9.3 · §14.3 · 검토서:96 이 일치한다. §9.3 → §14.3 인용 내용만 약하다(#16).
- TOOL.34 (nit) — 부분만 고침. 예 파일명 · 기준 폴더 · 템플릿의 `Scenes/` · `Audio/` · §2.5 「코드 폴더마다」는 확인된다. 템플릿:40 「폴더마다 asmdef」는 그대로다(#13).
- TOOL.38 (nit) — 고침. 다만 취소 예외 처리 규칙이 없다(#9).