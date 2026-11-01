---
id: 20261031-p03-s1-a3ff2b61-prompt
title: 코드리뷰 S1 — 에이전트 a3ff2b61 지시 원문
summary: 「2라운드 센서 — 수정 커밋 리뷰어 A(opus)」 에이전트(claude-opus-5-5 · 도구 호출 44)에 작성 세션이 보낸 첫 지시 원문.
doc_type: review
status: final
lifecycle: static
created: 2026-10-31
updated: 2026-10-31
work_unit: P03
---
이 지시는 Opus 5.5 기준으로 썼다(가이드 확인일 2026-09-29). 세션 모델이 다르면 보고 첫 줄에 적는다.

역할 — 코드 리뷰어다(2라운드 — 1라운드 센서 지적을 고친 수정 커밋만 본다). 읽기만 한다. 파일을 고치지 않고, 커밋하지 않고, 테스트를 돌리지 않고, Unity 에디터 · Blender 를 실행하지 않는다. 작업 트리의 상태도 바꾸지 않는다 — `git checkout` · `git switch` · `git stash` · `git reset` 을 쓰지 않고, 다른 시점의 파일은 `git show <해시>:<경로>` 로 읽는다. 찾은 것을 전부 보고하고 선별은 내가 한다. 이 리뷰의 목적은 결함 후보와 이해 안 되는 곳을 찍어 사람의 주의 위치를 알려 주는 것이다 — 판결이 아니다.

격리 — 이 작업은 두 모델이 같은 조건으로 따로 하는 비교 실험의 한쪽이다. 다음은 열거나 읽거나 실행하지 않는다: `git branch` · `git log --all` · `git worktree list` · 다른 브랜치를 가리키는 `git show` · `z.captures/` 안의 모든 것 · `z.tmp/p03_results/` · `z.docs/Defense.Logs/` · Planning 의 P03 폴더 안 문서(아래 지시서 하나만 예외) · 아래 저장소 폴더 밖의 다른 worktree.

저장소 — `/Users/devman/_Projects/_Personal/Games/Defense/z.tmp/wt/p03-sonnet` (git worktree, 브랜치 `p03/exec-sonnet`). 모든 git 명령은 `git -C <이 경로>` 로 쓴다.

대상 — 위 저장소에서 `git diff 546f586..94591e2 -- . ':(exclude)z.docs' ':(exclude)*.md' ':(exclude)*.unity' ':(exclude)*.prefab' ':(exclude)*.meta' ':(exclude)*.fbx' ':(exclude)*.png'` (코드 4파일 +52/−17: `Assets/10_Scripts/Editor/P03/` 의 `P03Capture.cs` · `P03Measure.cs` · `P03ModelImporter.cs` · `P03Runner.cs`). 커밋은 하나다 — `git -C <저장소> log -1 --format='%h %s%n%b' 94591e2` 로 설명을 읽는다. 이 커밋은 1라운드 센서가 짚은 세 곳(① `ImportModels` 의 「벗기기 전」 클립 이름이 가져오기 설정이 바꾼 이름에서 읽혀 설정된 프로젝트에서 다시 돌리면 달라짐 ② `DumpFrames` 가 `BuildScene` 과 따로 변형 인자를 받아 어긋날 수 있음 ③ `new[]` 표기)을 고친 것이다. 수정이 의도한 것을 실제로 하는지, 새 결함을 만들지 않았는지를 본다. 주변 코드와 호출 관계는 `94591e2` 시점 파일로 읽는다(작업 트리가 같을 수 있으나 `git show 94591e2:<경로>` 가 기준이다). 큰 diff 는 파일별로 전부 읽는다 — 훑지 않는다. 호출처 확인을 위해 `546f586` 시점의 같은 파일도 읽어도 된다.

먼저 읽을 것 —
① 지시서 `/Users/devman/_Projects/_Personal/Games/Defense/z.docs/Defense.Planning/P03_CLI_환경테스트/02_계획/지시서/20261031_S1S2_Unity_P03_실행.md` 의 「프롬프트 본문」 가운데 「맡는 일」 · 「성공 기준 · 위험 · 되돌리는 법」 · 「작업 위치」(수정 허용 영역 · 읽기 전용) · 「계약」 · 「금지」. 이 파일 말고 Planning 의 다른 문서는 읽지 않는다.
② 저장소 `CLAUDE.md` 의 「코딩」 · 「검토 기준」 절.
③ 코딩 표준 `z.docs/dev/csharp_coding_standards.md`(에디터 스크립트에도 §6 null · §7 · §5 var 금지 · §1 이름 · §3 구조 · §16 에디터 코드가 대조 기준이다).
④ 고위험 경로 — 저장 데이터 · 재화 · 업그레이드 수치 · `ProjectSettings/` · 빌드 프로필 · `Packages/` · 서명 · 배포(`.github/workflows/`). 이 범위에 해당 경로가 있는지도 확인해 알려라.
이 코드는 에디터 전용 시험 도구다(런타임 제품 코드가 아니다). 이 범위는 1라운드에서 이미 검토한 코드의 수정이므로, 수정으로 바뀐 줄과 그 줄이 닿는 호출처에 집중하고 1라운드 범위(`546f586` 이전 전체)를 다시 훑지 않는다.

각도(순서대로, 각도마다 diff 전체) —
1. 정확성: 줄 단위 논리 · 경계값 · null · 예외 경로(`ModelImporter` 캐스트가 null 일 때 · `PrefabUtility.GetPrefabAssetPathOfNearestInstanceRoot` 가 돌려주는 값 · 정렬 비교자 · 클립 배열 크기 등).
2. 파일 사이: 바뀐 메서드의 호출처 전부. 시그니처 · 반환 의미 · 예외가 바뀌었는데 호출처가 그대로인 곳(`DumpFrames` 의 인자가 줄었다 — 이 저장소 안의 호출처와 문서 · 주석 · 요약에 옛 시그니처가 남았는지).
3. 누락: 지시서 성공 기준 가운데 이 수정이 영향을 주는 것(3 함정 둘 실측값 · 6 녹화)이 여전히 충족되는지. 수정으로 빠진 처리 · 검증.
4. 검토 기준 대조: 「검토 기준」 절과 코딩 표준 항목 가운데 이 diff 에 해당하는 곳(지적은 표준 절 번호로).
5. 범위: 수정 허용 영역 밖 변경, 요청에 없는 기능 · 리팩터링.
6. 이해: 읽고도 왜 이렇게 했는지 모르는 곳.

쓰지 않는 것 — 스타일 · 포맷 · 주석 문구 · 이름 취향(결정론 층의 일이다). 단 코딩 표준 규칙 위반(var · `??` · Unity 객체의 `?.` · 파일당 클래스 하나 등)은 표준 절 번호와 함께 쓴다.

보고 형식 — 표 한 개, 지적 하나가 한 행. 빈 칸 없이.

| # | 종류 | 심각도 | 기원 | 유형 | 파일:줄 | 실패 시나리오(입력 → 잘못된 결과) | 확신 |
|---|---|---|---|---|---|---|---|

- 종류: issue · suggestion · question · nitpick · thought. 이해 안 되는 곳은 question.
- 심각도: blocking(저장 데이터 손상 · 재화 유실 · 비밀값 · 계약 위반 · 성공 기준 미달) · important(고치거나 사유가 필요) · nit(작성자 재량).
- 기원: new(이 diff 가 만든 것) · pre-existing(diff 전부터 있던 것 — `git blame` 으로 확인) · out-of-scope(수정 허용 영역 밖 · 다른 저장소).
- 유형: 한 줄의 결함 유형. 같은 유형이 여러 곳이면 한 행에 파일:줄을 나열한다.
- 확신: confirmed(파일 · 호출 관계를 열어 확인함) · plausible(가능성은 있으나 끝까지 확인 못 함).
- 증거 없는 지적은 적지 않는다. 심각도 순으로 정렬한다. 지적이 없으면 표를 비우고 그 사실을 한 줄로 적는다. 표 뒤에 「확인하지 않은 것 · 추정한 것」을 따로 적는다.

보고는 표와 그 뒤 한 절만. 요약 · 칭찬 · 과정 서술은 넣지 않는다. 다른 절(구현 계획 · 핵심 파일 목록 따위)을 붙이지 않는다.

Write your final report (and any SubagentHandback message) entirely in Korean. Keep code, commands, file paths, identifiers, URLs and quoted source text as-is.