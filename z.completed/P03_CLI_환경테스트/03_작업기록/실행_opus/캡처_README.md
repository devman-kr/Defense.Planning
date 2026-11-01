---
id: 20261031-p03-captures-opus
title: 2026-10-31 캡처 — P03 S2(Opus 5.5) 샘플 씬
summary: P03 S2 의 산출 대응표 — CLI capture game_view 세로 · 가로 2장, 48프레임 PNG 와 Blender 내장 ffmpeg MP4(다시 읽어 48프레임), 고친 make_enemies.py 렌더 7장 · P03_RESULT JSON 이며 git 사본은 없다.
doc_type: register
status: final
lifecycle: living
created: 2026-10-31
updated: 2026-10-31
work_unit: P03
---
# 2026-10-31 캡처 — P03 S2(Opus 5.5) 샘플 씬

Defense.Unity worktree `p03-opus` · 브랜치 `p03/exec-opus` 의 결과물이다. 씬은 `Assets/00_Scenes/P03_CLI_Sample.unity`(커밋 `3a1dd18` — 섬도 `palette.mat` 을 쓰는 판. 캡처 · 프레임 · MP4 는 이 판으로 다시 만들었다), Blender 스크립트는 `Tools/Blender/make_enemies.py`(커밋 `a5a2a5c`). 측정 기기는 Mac M5 16 GB · Unity 6000.3.27f1(창 없는 에디터) · Blender 5.2.3 LTS. 이 폴더의 파일은 git 에 사본이 없다.

| 원본 | 내용 | 만든 명령 | 크기 · SHA-256 앞 12자 | git 사본 |
|---|---|---|---|---|
| `capture_portrait_1080x1920.png` | 샘플 씬 세로 9:16 — 섬 · 등불 탑 · 슬라임 8 · 박쥐 4(바인드 자세) | `capture game_view --source camera --camera PortraitCamera --width 1080 --height 1920 --save_path Temp/P03/…` → `Assets/Temp/P03/` 에 떨어진 것을 옮김 | 573,436 B · `37d99b1a5040` | 없음 |
| `capture_landscape_1920x1080.png` | 같은 카메라의 가로 16:9 | 같은 명령 `--width 1920 --height 1080` | 245,706 B · `90ce39eaeabd` | 없음 |
| `frames/frame_000.png` ~ `frame_047.png` | 48프레임(24 fps · 2초 · 720×1280) — 슬라임 Idle · Hop 번갈아 · 개체마다 위상, 박쥐 Flap | 에디터 스크립트 `P03FrameRecorder.Record`(클립 샘플링 → 카메라 → RenderTexture → PNG) | 합계 13 MB | 없음 |
| `sample_48f_24fps.mp4` | 위 48프레임의 H.264 MP4 — Blender 로 다시 읽어 `frame_duration` 48 · 24 fps · 720×1280 | `Blender -b … --python encode_mp4.py -- frames sample_48f_24fps.mp4 24`(VSE 이미지 스트립 → `FFMPEG` · `MPEG4` · `H264`) | 179,917 B · `c1940934d7ad` | 없음 |
| `encode_mp4.py` | 위 인코딩 · 다시 읽기 스크립트(세션 스크래치패드 원본의 사본 — 저장소 밖) | — | 2,435 B · `0dd36d2f377f` | 없음 |
| `renders/render_lineup.png` | 고친 스크립트의 라인업 — 박쥐 날개가 팔레트 셀 6(어두운 보라). 이전 렌더(`../render_lineup.png`)와 다른 픽셀 2,496개는 전부 날개 영역(x 331~559 · y 195~248) | `Blender -b --factory-startup -noaudio --python-exit-code 1 --python Tools/Blender/make_enemies.py -- z.tmp/p03_out_opus` | 523,279 B · `6dc6b9d1bed9` | 없음 |
| `renders/render_bat_Flap_f01.png` · `_f06.png` | 박쥐 날갯짓 정면 — f01 두 날개 위 · f06 두 날개 아래 | 같음 | 231,525 B · `ba00a265e882` / 228,749 B · `748835095c56` | 없음 |
| `renders/render_slime_*.png`(4장) | 슬라임 Idle f12 · Hop f08 · Hit f03 · Die f18 — 이전 렌더와 픽셀 차이 0 | 같음 | 각 약 225~229 KB | 없음 |
| `renders/p03_result.json.txt` | 위 실행의 표준 출력 `P03_RESULT` 줄 | 같음 | 1,666 B · `7e2839b728e5` | 없음 |
