<!-- 정본: z.docs/Defense.Planning/_템플릿/Unity_CLAUDE.md — P00 스트림 D 에서 Defense.Unity/CLAUDE.md 로 복사한다. 게이트 명령 · Unity 버전은 설치 뒤 실측으로 채운다(「(설치 뒤)」 표시). 복사한 뒤 이 줄을 지운다. -->

# Defense.Unity

Unity 6 · URP 모바일 게임 「Lantern Rush!」(랜턴 러시!)의 공개 포트폴리오 저장소(저장소 이름은 게임 순서 가칭 `Defense`, G-09). 작업 공간 규칙은 `../CLAUDE.md`(루트), 세 게임 공통은 `../../CLAUDE.md`, 과제 · 결정은 `../z.docs/Defense.Planning/`, 기획은 `../z.docs/Defense.Design/`. 이 문서는 저장소 안 작업(코드 · 문서 · 커밋)의 규칙이고, 루트와 충돌하면 이 문서가 우선한다.

## 작업 시작 전
- 작업 계획을 다음 형식으로 제시한 뒤 승인을 기다린다:
  - 목표:
  - 영향 파일:
  - 작업 단계(TodoWrite):
- Planning 지시서(`../z.docs/Defense.Planning/…/02_계획/지시서/`)로 시작한 세션은 지시서의 「성공 기준 · 위험 · 되돌리는 법」 · 「승인 지점」을 따른다 — 위험 등급이 저(문서 · 테스트 · 주석 · UI 문자열 · 데이터 에셋 수치 아님)면 「지시서와 다른 점」 한 줄로 알리고 바로 착수, 중 · 고는 위 형식대로 승인. 등급은 `../z.docs/Defense.Planning/코드리뷰_가이드.md` 5절.
- 설계와 다른 구현이 필요하면 먼저 `../z.docs/Defense.Design/기획서.md` 를 고치자고 제안한다. 코드가 기획서보다 앞서가지 않는다.

### 사용자와 논의가 필요한 사항 발견 시
- 권장안(프로젝트 도메인 · 일관성 · 안정성 기준)과 제언안(세션의 인사이트)을 같이 제안한다.

## 작업 중
- 명시적으로 지시된 내용 외에는 하지 않는다. 추가 작업이 필요하면 이유와 계획을 승인받는다.
- 읽기 전용 명령은 바로 실행한다. 파일 · 상태 · 외부 자원을 바꾸거나 네트워크로 보내는 명령은 확인을 받는다.
- 에디터 조작(씬 · 프리팹 · 컴포넌트 · 플레이 모드 · 빌드)은 `unity-cli` 로 주 세션만 한다. 에디터 재시작 · 패키지 추가 · `ProjectSettings/` 변경 · 플랫폼 전환은 승인 지점.

## 작업 후
- 작업 내용을 요약해 전달한다. 바꾸는 곳 밖의 원본 내용은 보존한다.
- `z.docs/work_reports/{yyyyMMdd}/{그날 순번}_{verb}_{제목}.md` 작업 보고서를 쓴다. 프론트매터 `work_unit` 은 과제 ID(`P01`).
- 모든 작업 후 커밋한다.

## git 워크플로우
- 커밋 메시지는 한글, `verb: [Pnn] 제목` — verb 는 `create` · `modify` · `fix` · `refactor` · `docs` · `delete` · `test`.
- 커밋 전에 `git diff` 와 `git status` 를 확인한다. `.meta` 가 짝으로 들어갔는지, `Library/` · `Temp/` · `Logs/` · `obj/` · `Builds/` · `UserSettings/` 가 안 들어갔는지 본다.
- 트레일러는 `_공통` Q-01 결정대로. 결정 전: `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
- 푸시는 루트 `CLAUDE.md` 「푸시」대로(허락 뒤 주 세션만).

## Agent Teams 병렬 구현
- 파일을 고치는 병렬 작업은 worktree 격리. 에이전트마다 폴더 영역을 겹치지 않게 나누고, **씬 · 프리팹 · `.asset` 은 한 에이전트만** 만진다.
- `main` 은 작업 중 바꾸지 않는다. 머지 방식은 사용자가 정한다(PR 검토 머지 권장 · 순차 머지 · 브랜치 삭제로 롤백).
- 서브에이전트는 코드 · 컴파일 · EditMode 테스트까지. 에디터 · 빌드는 주 세션.

## 코딩 (C# · Unity)
- 폴더: `Assets/_Project/Core/`(게임 무관 — 다른 게임이 복사해 간다, G-07) · `Assets/_Project/Defense/`(이 게임) · `Assets/_Project/Data/`(ScriptableObject 에셋) · `Assets/_Project/Art/` · `Assets/ThirdParty/`(외부 에셋 — `ASSETS.md` 장부 필수). 테스트는 `Assets/_Project/Tests/EditMode` · `PlayMode`.
- 어셈블리: 폴더마다 asmdef. **Core 는 Defense 를 참조하지 않는다.**
- 이름: 네임스페이스 `Defense.Core.*` · `Defense.Game.*`, 타입 · 메서드 · 속성 PascalCase, 비공개 필드 `_camelCase`, 인스펙터 노출은 `[SerializeField] private`. 공개 필드 금지.
- 하드코딩 금지 — 밸런스 수치는 ScriptableObject(`*Def` · `WaveCurve`), 문자열은 문자열 표, 레이어 · 태그는 상수 클래스 하나.
- 성능: 적 · 투사체마다 `Update` 를 두지 않고 시스템 하나가 배열로 처리한다. 런 중 `Instantiate` · `Destroy` 대신 풀. 매 프레임 할당(LINQ · 박싱 · 문자열 결합 · 클로저) 금지. `FindObjectOfType` · `GetComponent` 를 루프에서 부르지 않는다. `Camera.main` 은 캐시.
- 주석: 공개 타입 · 메서드에 `///` 요약. 람다는 그 블록의 역할 한 줄. 수정 이력은 파일 헤더가 아니라 작업 보고서 · 커밋에.
- 외부 패키지는 MIT · Apache · CC0 등 재배포 가능한 것만, `Packages/manifest.json` 변경은 승인 지점이고 `ASSETS.md` 에 적는다. Asset Store 에셋은 커밋하지 않는다.

## 결정론 게이트 (커밋 전)
- 에디터 콘솔 컴파일 오류 0 · 새 경고 0(설치 뒤 `unity-cli` 명령 기록).
- EditMode 테스트 전부 통과. 런 흐름을 바꿨으면 PlayMode 스모크(자동 선택 + 가속 한 판).
- 빌드 설정 · 플랫폼을 바꿨으면 대상 빌드 한 번(Android · WebGL).

## 검토 기준
코드 리뷰 센서가 diff 에 대조하는 이 저장소의 실패 유형. 반복 지적은 테스트 · 분석기로 내리고 여기서 지운다. 10줄을 넘기면 `z.docs/dev/review_criteria.md` 로.
- 저장 데이터: 포맷 버전 필드를 올리지 않고 필드를 바꾸지 않는다. 이전 버전 변환 테스트가 있다.
- 재화 · 업그레이드 수치: 코드 상수가 아니라 데이터 에셋. 바뀌면 작업 보고에 전후 값.
- 시간: 게임 로직은 `Time.deltaTime`(일시정지 · 가속 반영), UI 연출만 `unscaledDeltaTime`.
- 풀: 꺼낸 객체는 상태를 초기화하고, 돌려준 객체를 계속 참조하지 않는다.

## 참조 경로
- 기획서: `../z.docs/Defense.Design/기획서.md`(기획 저장소 — Planning X-02)
- 마일스톤: `z.docs/dev/milestone/NN_slug/milestone.md`(`DEF-Mnn`)
- 작업 보고서: `z.docs/work_reports/{yyyyMMdd}/*`
- 에셋 장부: `ASSETS.md`
- Unity 버전: `ProjectSettings/ProjectVersion.txt`(설치 뒤)
