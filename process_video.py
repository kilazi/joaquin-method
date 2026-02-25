#!/usr/bin/env python3
"""Process a Joaquín Vega video: download, transcribe, translate, extract key frames + decision points."""
import sys, os, json, subprocess, openai, time

def process(video_id, title):
    work_dir = f"/Users/kilazi/Work/joaquin-method/{video_id}"
    os.makedirs(work_dir, exist_ok=True)
    os.chdir(work_dir)
    
    print(f"\n{'='*60}")
    print(f"PROCESSING: {title} ({video_id})")
    print(f"{'='*60}")
    
    # 1. Download
    if not os.path.exists("video.mp4"):
        print("\n[1/5] Downloading...")
        subprocess.run([
            "yt-dlp", "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "-o", "video.%(ext)s", f"https://www.youtube.com/watch?v={video_id}"
        ], capture_output=True)
    else:
        print("\n[1/5] Already downloaded")
    
    # 2. Extract audio
    if not os.path.exists("audio.mp3"):
        print("[2/5] Extracting audio...")
        subprocess.run([
            "ffmpeg", "-i", "video.mp4", "-vn", "-acodec", "libmp3lame",
            "-q:a", "2", "audio.mp3", "-y"
        ], capture_output=True)
    else:
        print("[2/5] Audio already extracted")
    
    # 3. Transcribe
    client = openai.OpenAI()
    if not os.path.exists("transcription.json"):
        print("[3/5] Transcribing (Whisper)...")
        with open("audio.mp3", "rb") as f:
            result = client.audio.transcriptions.create(
                model="whisper-1", file=f, language="es",
                response_format="verbose_json",
                timestamp_granularities=["segment"]
            )
        with open("transcription.json", "w") as f:
            json.dump(result.model_dump(), f, ensure_ascii=False, indent=2)
        with open("transcription_es.txt", "w") as f:
            f.write(result.text)
    else:
        print("[3/5] Already transcribed")
    
    # 4. Translate with decision-point extraction
    if not os.path.exists("analysis.json"):
        print("[4/5] Translating + extracting decision points...")
        with open("transcription_es.txt") as f:
            spanish = f.read()
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "system",
                "content": """You are analyzing a Spanish trading education video by Joaquín Vega, who teaches a modified Fibonacci methodology. 

Your job is to produce a JSON object with:

1. "translation": Full faithful English translation. Keep trading terms precise.

2. "decision_points": Array of key decision moments. Each has:
   - "timestamp_approx": rough position in the video (early/mid/late or minute mark if obvious)
   - "condition": What price condition he's looking at (e.g. "price retraces to 61.8%")
   - "if_true": What happens / what to do if this condition is met
   - "if_false": What happens / alternative if not met
   - "action": The trade action (buy/sell/wait/exit/partial)
   - "quote_es": The key Spanish phrase he uses
   - "quote_en": English translation of that phrase

3. "concepts": Array of methodology concepts mentioned, each with:
   - "name": concept name (e.g. "fractality", "point of control", "61.8% retracement")
   - "definition": how he defines/uses it in this video
   - "relationship": how it connects to other concepts

4. "rules": Array of explicit trading rules stated, each with:
   - "rule": the rule in plain English
   - "context": when it applies

5. "summary": 3-5 sentence summary of what this video teaches

Output ONLY valid JSON, no markdown fences."""
            }, {
                "role": "user",
                "content": spanish
            }],
            max_tokens=8000,
            response_format={"type": "json_object"}
        )
        
        analysis = json.loads(response.choices[0].message.content)
        with open("analysis.json", "w") as f:
            json.dump(analysis, f, ensure_ascii=False, indent=2)
        
        # Also save plain translation
        with open("translation.txt", "w") as f:
            f.write(analysis.get("translation", ""))
    else:
        print("[4/5] Already analyzed")
    
    # 5. Extract key frames
    with open("transcription.json") as f:
        data = json.load(f)
    
    segments = data["segments"]
    duration = segments[-1]["end"] if segments else 600
    
    # Extract frames every 30 seconds + at beginning and end
    frame_times = list(range(0, int(duration), 30))
    if duration not in frame_times:
        frame_times.append(int(duration) - 1)
    
    existing_frames = [f for f in os.listdir(".") if f.startswith("frame_") and f.endswith(".jpg")]
    if len(existing_frames) < len(frame_times) // 2:
        print(f"[5/5] Extracting {len(frame_times)} frames...")
        for ts in frame_times:
            out = f"frame_{ts:04d}s.jpg"
            if not os.path.exists(out):
                subprocess.run([
                    "ffmpeg", "-ss", str(ts), "-i", "video.mp4",
                    "-vframes", "1", "-q:v", "2", out, "-y"
                ], capture_output=True)
    else:
        print("[5/5] Frames already extracted")
    
    # Load analysis for summary
    with open("analysis.json") as f:
        analysis = json.load(f)
    
    n_decisions = len(analysis.get("decision_points", []))
    n_concepts = len(analysis.get("concepts", []))
    n_rules = len(analysis.get("rules", []))
    
    print(f"\n✓ DONE: {title}")
    print(f"  Decision points: {n_decisions}")
    print(f"  Concepts: {n_concepts}")
    print(f"  Rules: {n_rules}")
    print(f"  Summary: {analysis.get('summary', 'N/A')[:200]}")
    
    return analysis

if __name__ == "__main__":
    video_id = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else video_id
    process(video_id, title)
