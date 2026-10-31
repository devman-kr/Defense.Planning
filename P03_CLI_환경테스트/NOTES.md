---
id: 20261031-p03-notes
title: NOTES — P03 작업 메모
summary: P03 세션 인계 메모 — 실행 대기 상태(K1 763866b · 지시서 S1·S2 · S3), 사용자 손 절차 (a)~(d) 순서, 미실측 5(창 없는 에디터 카메라 렌더 · 클론 Library · Blender MP4 · bake_space_transform · clipAnimations), 격리 조건, 발견 로그.
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

_갱신: 2026-10-31 — 세션 a3a90bb0(Fable 5.1): 등재 · 검토 · 의논 3라운드 → D-01~D-10 · 계획서 · S0 준비(Defense.Unity `7f88bef` · `1f87826` · `763866b`) · 지시서 S1·S2 · S3. 실행은 다른 세션 둘(Sonnet 5.5 → Opus 5.5)_

1. **지금 어느 단계**: 계획 — 실행 대기. 결정 D-01~D-10 끝, 미결 없음. 시작 커밋 K1 = `Defense.Unity` `763866b`(`main`). 지시서 둘은 `02_계획/지시서/`.
2. **다음 할 일 순서(사용자 손 절차 — [계획서](02_계획/계획서_20261031.md) 7절)**: (a) worktree `z.tmp/wt/p03-sonnet` + `Library/` 클론 + `z.captures/<날짜>/sonnet/` → 작업 공간 루트에서 새 세션 `/model sonnet` · `/effort high`, [지시서 S1·S2](02_계획/지시서/20261031_S1S2_Unity_P03_실행.md) 「프롬프트 본문」 붙여 넣기, 시작 시각 기록 → 끝나면 `/cost` · 끝 시각 · 멈춤 · 개입 횟수 기록 → (b) 격리(번들 · worktree 제거 · 브랜치 삭제 · 캡처 이동) → (a) 를 `opus` 로 → (c) 격리 → (d) 복원 → `/model fable` 세션에 [지시서 S3](02_계획/지시서/20261031_S3_판정.md).
3. **착수 전 확인**: 에디터 · Blender 가 떠 있지 않은지(`pgrep -x Blender` · `pgrep -f 'Unity.app/Contents/MacOS/Unity'`). `git -C Defense.Unity branch` 에 `p03/exec-*` 가 남아 있지 않은지(S2 전). 실행 세션은 Planning 을 읽지 않는다(지시서만) — 이 NOTES 는 S3 와 사용자용.
4. **미실측(실행 세션이 닫는다 — 지시서 「알려진 함정」)**: ① 창 없는 에디터의 `capture game_view --source camera` ② 클론 `Library/` 로 다른 경로에서 열리는지 ③ Blender ffmpeg MP4 ④ `bake_space_transform` 켠 FBX 의 Unity 루트 회전 ⑤ `clipAnimations` 로 접두 벗기기.
5. **S3 가 받을 것**: 두 세션의 시간 · `/cost` · 멈춤 · 개입 기록(사용자) · 번들 둘(`z.tmp/p03_results/<모델>/`) · 캡처 폴더 둘.

## 현재 상태 (덮어쓰기)

_갱신: 2026-10-31_

| 항목 | 상태 |
|---|---|
| 검토 | 검토서 2026-10-31 ✔(확인 사항 8 전부 답) |
| 결정 | D-01~D-10 ✔ · 미결 없음 |
| 계획 | 계획서 2026-10-31 ✔ · 지시서 S1·S2(두 모델 공통) · S3 ✔ |
| S0 | ✔ `Defense.Unity` `7f88bef`(이동) · `1f87826`(문서 · `Tools/Blender`) · `763866b`(보고) — 게이트 2/2 · 경고 0 · 센서 생략(사용자) |
| 저장소 변경 | `Defense.Unity` `main` `763866b`(미푸시 3) · `Defense.Planning` `main`(등재 `5d822fc` + 이 세션 커밋 — 작업색인) |
| 환경 | Unity 6000.3.27f1 · Unity CLI 1.0.0-beta.13 · pipeline 0.9.1 · Blender 5.2.3(내장 ffmpeg) · 에디터 꺼짐 · 활성 플랫폼 WebGL [추정] · 인코더 ffmpeg · ImageMagick · PIL 없음 |

## 사용자 대기 (덮어쓰기)

- 푸시 허락(세션 끝 질문) — `Defense.Unity` 3 커밋 · Planning 2 커밋.
- 실행 세션 열기(위 2번) — 세션이 아니라 사용자가 한다.

---

## 함정 · 주의 (누적)

- 한 기기(G-01) — Blender(약 0.4 GB) 와 에디터를 같이 띄우지 않는다. 동영상 인코딩(Blender)은 에디터를 끈 뒤.
- `bpy` 스크립트를 공개 저장소에 두면 그 폴더가 GPL-3.0-or-later(G-17) — P03 동안 git 밖(`z.tmp` · `z.captures`).
- 사본 프로젝트에서 에디터를 띄울 때 `--project-path` 를 사본 경로로 준다. `Defense.Unity` 를 연 에디터와 사본을 연 에디터를 같이 띄우지 않는다(메모리 · 혼동).
- 기획서 9절은 적 모델을 Quaternius 1순위로 적었다 — P03 은 기획서를 고치지 않는다(시험). 본편에 쓰면 `DEF-M03` D-nn → 기획서.
- **격리 조건(D-04)**: 실행 세션은 Planning · Design · Logs 를 읽거나 쓰지 않고, 다른 브랜치 · 다른 모델 캡처 폴더를 열지 않는다. S1 이 끝나면 사용자가 번들로 빼고 브랜치를 지운 뒤 S2 를 연다 — 순서를 어기면 비교가 성립하지 않는다.
- 사용자가 Finder 로 만든 폴더 이름(「00. Scenes」)은 S0 에서 `00_Scenes` 로 바꿨다(D-09). 에디터는 `.meta` 로 빈 폴더를 다시 만든다 — 번호 폴더 `.meta` 넷이 `7f88bef` 에 있다.

## 발견 로그 (누적, 최신 위)

- 2026-10-31 — Blender 5.2.3 창 없이 `make_enemies.py` 한 번에 5.35초 · 최대 RSS 417 MB — 모델 3 · 동작 6 · FBX 6 · EEVEE 렌더 7장(4.28초) · 재임포트 클립 4. P00 D-09 스모크 방식(`keyframe_insert` 로 동작 자동 생성 · 슬롯 지정 · NLA 트랙 뮤트 · `bake_anim_use_all_actions`)이 그대로 산다. ✔
- 2026-10-31 — 렌더 결함 둘(파이프라인 아님 · 스크립트 수치): 박쥐 날개가 팔레트 셀 6(보라)이 아니라 초록 — `from_pydata` 메시에 `set_cell` 한 UV 가 join 뒤 0 으로 간 듯 [추정]. 날갯짓 회전축이 어색(한쪽 날개가 접힘) — 월드 Y 축을 뼈 공간으로 옮긴 `rot_about_world` 의 부호 · 축 확인 필요. 슬라임(스쿼시 · 점프 · 피격 · 납작) · 탑은 의도대로. ✔
- 2026-10-31 — Blender 가 자기 FBX 를 다시 읽으면 클립 이름이 `SlimeRig|SlimeRig|Idle`(뼈대 이름 두 번). Unity 는 P00 실측 `Rig|Idle`(한 번). 뼈 이름을 모델마다 다르게(`SlimeRoot` · `BatRoot`) 두어 `bake_anim_use_all_actions` 가 다른 모델의 동작을 섞어 내보내지 않게 했다. ✔
- 2026-10-31 — `com.unity.pipeline` 0.9.1 명령 목록(`Runtime/Common/CommandNames.cs`): `capture game_view`(source camera · screen, `save_path`, 1280×720 기본 · 4096 상한) · `capture scene_view` · `script run --file`(프로젝트 밖 `.cs` 도 메모리 컴파일) · `scene` · `gameobject` · `asset` · `material` · `prefab` · `animation.animator` · `animation.clip` · `editor.playmode` · `wait_for --capture` · `job batch`. ✔
- 2026-10-31 — `Defense.Unity` → `z.tmp/p03/unity/` APFS 클론 `cp -c -R` 7.5초(8.9 GB, 실제 공간 거의 0). 인코더: ffmpeg · ImageMagick · gifsicle · PIL 없음, Blender `bpy.app.ffmpeg.supported` 참(codec H264 · AV1 · WEBM …, format MPEG4 · MKV · WEBM …). ✔

## 미해결 (누적)

- 창 없는 에디터의 카메라 렌더 · 플레이 모드 `source=screen` 캡처 가능 여부 — 실행 세션 실측.
- 샘플 에셋을 들일지 — 결정 3 · `DEF-M03`.
