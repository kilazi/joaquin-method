# Joaquín Vega Method — Video Breakdown Pack

15 videos from Joaquín Vega's trading channel, fully processed: downloaded, transcribed from Spanish, translated to English, analyzed for decision points, concepts, and rules.

## Quick Start

Open `joaquin-method-breakdown.html` in any browser — it's self-contained with embedded screenshots.

## What's Inside

### Master Files
- `joaquin-method-breakdown.html` — full interactive breakdown (15 videos, 34 decision points, 47 concepts, 40 rules, embedded screenshots)
- `all_analyses.json` — structured JSON of all extracted data across all videos
- `video_queue.json` — processing queue with video IDs, titles, priorities
- `process_video.py` — pipeline script to process additional videos

### Per-Video Folders (one per video ID)
Each folder (e.g. `Tiy6bO9hXJ4/`) contains:
- `video.mp4` — original downloaded video
- `audio.mp3` — extracted audio track
- `transcription_es.txt` — Spanish transcript (Whisper)
- `transcription.json` — timestamped segments (for syncing with frames)
- `translation.txt` — English translation
- `analysis.json` — structured extraction: decision points, concepts, rules, summary
- `frame_XXXXs.jpg` — screenshots every ~30 seconds

### First Video Bonus (in `/Users/kilazi/Work/video-translate/`)
- `dubbed_video.mp4` — English voiceover (Orpheus TTS "dan" voice) over original video
- `voiceover_full.mp3` — standalone English audio
- `presentation.html` — slide-by-slide presentation of gold/silver video

## Videos Processed

| # | ID | Title | Priority |
|---|-----|-------|----------|
| 1 | Tiy6bO9hXJ4 | Trading Gold & Silver | method-application |
| 2 | QNRJX4b7Qq4 | Students Preferred Ratios | core-method |
| 3 | p9aw5DkgFX8 | Evolution of Cycles | core-method |
| 4 | wmqmqzn_Ito | Analysis vs Strategy vs Method | core-method |
| 5 | aUHXlpn-iRc | Value Left Side of Charts | core-method |
| 6 | fk3luzBRmHA | Work on Context in Chart | core-method |
| 7 | 4b2ZAImaATk | Fractality Practice Example | core-method |
| 8 | 3ilsV4UU5Y0 | Understanding Fractality | core-method |
| 9 | u6K3H8d-4J0 | Super Winning Trades | method-application |
| 10 | M70f76duW2s | Good/Bad Use of Partials | risk-mgmt |
| 11 | ExKdYnCebqY | Must Keep This In Mind | core-method |
| 12 | koKCbtrB_eI | Better Explained Live | method-application |
| 13 | 6U91ZG1e80g | Many Ways to Win and Lose | risk-mgmt |
| 14 | ijMX71M37Uw | Gold Trading with the Kids | method-application |
| 15 | GrH-mtabADo | Setbacks - Enemy of Novice Traders | risk-mgmt |

## Stats
- 34 decision points (with IF/ELSE branching)
- 47 concepts identified
- 40 explicit trading rules
- ~350 chart screenshots total

## Next Steps
- Build binary decision trees from the 34 decision points + 40 rules
- Process more videos with `python3 process_video.py <VIDEO_ID> "<TITLE>"`
- Cross-reference concepts into a unified methodology document

## Tools Used
- yt-dlp (download), ffmpeg (audio/frames), OpenAI Whisper (transcribe), GPT-4o (translate + analyze), Together AI Orpheus TTS (voiceover)
