# Metodo Joaquin Vega — Complete Project Documentation

## What This Is

A fully interactive web application that digitalizes the **Joaquin Vega Modified Fibonacci Trading Method** — a complete trading system taught through 40+ YouTube videos by Spanish trader Joaquin Vega. The webapp turns hours of video content into navigable decision trees, searchable knowledge, audio clips of Joaquin's voice, chart screenshots, and YouTube timestamp links — all bilingual (English/Spanish).

**Live:** https://kilazi.github.io/joaquin-method/

---

## Project Stats

| Metric | Count |
|--------|-------|
| YouTube videos analyzed | 40 |
| Decision trees | 19 + 1 master "Should I Enter?" tree |
| Total decision nodes | ~200+ |
| Audio clips (Joaquin's voice) | 16 clips, 864KB total |
| Chart screenshots | 115 unique frames, 130 references |
| YouTube timestamp links | 61 |
| Languages | 2 (English + Spanish) |
| Webapp size | ~19MB (mostly frames) |
| index.html | 959 lines, single-file SPA |

---

## Architecture

### The Method's Three Layers
Joaquin's method is NOT just chart patterns. It's a 3-layer architecture:

1. **Reading Model** (T1-T4, T18) — Cycles, fractality, retracement, context. This is what the YouTube course teaches.
2. **Attack Model** (T5, T9, T15) — Entry strategy, zone trading, deception patterns. How to actually enter trades.
3. **Management** (T6-T8, T12, T14, T17, T19) — Post-entry management, partials, hedging, drawdown, null operations.

The YouTube course only covers the Reading Model. The webapp covers ALL three layers.

### Tech Stack
- **Frontend:** Single HTML file with vanilla JS, CSS custom properties (dark theme)
- **Data:** JSON files (trees.json, media_manifest.json, clips/manifest.json)
- **Hosting:** GitHub Pages (kilazi/joaquin-method, main branch, root-level files)
- **Processing pipeline:** yt-dlp → ffmpeg (audio extraction) → OpenAI Whisper (transcription) → GPT-4o (analysis) → ffmpeg (frame extraction every 30s)
- **No frameworks, no build step, no dependencies**

---

## File Structure

```
joaquin-method/
├── index.html                    # Root copy for GitHub Pages
├── trees.json                    # Root copy for GitHub Pages
├── media_manifest.json           # Root copy for GitHub Pages
├── frames/                       # 115 chart screenshots (root copy for GH Pages)
│   ├── 3ilsV4UU5Y0_0360s.jpg
│   ├── gold_si_o_si_entry.jpg
│   └── ...
├── clips/                        # 16 Joaquin voice clips (root copy)
│   ├── si_o_si.mp3
│   ├── fractalidad.mp3
│   └── ...
├── webapp/                       # Source directory
│   ├── index.html                # 959-line single-file SPA
│   ├── trees.json                # 19 decision trees v3.0
│   ├── media_manifest.json       # Frame/YouTube/clip mappings per tree
│   ├── clips/
│   │   ├── manifest.json         # 16 audio clip metadata
│   │   ├── si_o_si.mp3
│   │   └── ...
│   └── frames/                   # 115 chart screenshots
├── all_analyses.json             # Merged analysis of all 40 videos
├── decision_trees.json           # Master decision trees file
├── JOAQUIN_METHOD_REFERENCE.md   # 719-line comprehensive reference doc
├── PROJECT.md                    # This file
├── .gitignore                    # Excludes video files, allows clips/frames
└── [40 video directories]/       # Raw video data (not in git)
    ├── video.mp4
    ├── audio.mp3
    ├── transcription.json
    ├── analysis.json
    └── frame_XXXXs.jpg
```

---

## The 20 Decision Trees

### Master Entry Tree
| ID | Name | Purpose |
|----|------|---------|
| entry | **Should I Enter This Trade?** | Primary entry checklist — walks through every condition before entering. 13 decision nodes covering business plan, PoC identification, cycle activation, context, zones, confluence, liquidity, failure. Fully bilingual with Joaquin's voice clips at key nodes. |

### Reading Model (T1-T4, T18)
| ID | Name | Sources | Purpose |
|----|------|---------|---------|
| T1 | Cycle Identification | 3 videos | How to identify, activate, and mark a trading cycle (PoC + impulse + 38.2% retracement) |
| T2 | Fractality & Evolution | 3 videos | How cycles evolve or break — every cycle WILL do one or the other |
| T3 | Retracement Completion | 1 video | 130% rule — retracement is NOT finished until 130% touched |
| T4 | Context Reading | 3 videos | How to read the left side of the chart (failures, liquidity, PoCs, origins) |
| T18 | Context Assessment | 3 videos | Good/Regular/Weak context classification → lot sizing |

### Attack Model (T5, T9, T15)
| ID | Name | Sources | Purpose |
|----|------|---------|---------|
| T5 | Liquidity & Entry Strategy | 5 videos | Entry triggers: zone confluence, liquidity grabs, 61.8 post-failure, Fib+bias |
| T9 | 161-200 Zone Trading | 4 videos | Special handling for the 161.8-200% zone (currencies vs indices) |
| T15 | Deception Pattern | 1 video | False breakouts, 161.8% reversal zone, stop-then-turn validation |

### Management (T6-T8, T12, T14, T17, T19)
| ID | Name | Sources | Purpose |
|----|------|---------|---------|
| T6 | Trade Classification | 1 video | 5 outcomes: complete loser, null, positive, winner, very winner |
| T7 | Post-Entry Management | 6 videos | Fixed ratio (1:4), stop adjustments, partials, divided positions |
| T8 | Partial Profit Strategy | 3 videos | When/how to take partials without destroying statistics |
| T12 | Super-Winner Psychology | 4 videos | Holding through erratic moves, 10-20 per year |
| T14 | Hedging & Coberturas | 8 videos | Constant hedging, CFDs, zone indifference, dual-direction |
| T17 | Drawdown Management | 1 video | 15% stop, 22.5% reflect, 30% critical, segment trading |
| T19 | Null Operations | 2 videos | Exit at breakeven when price shows weakness |

### Foundation (T10-T11, T13, T16)
| ID | Name | Sources | Purpose |
|----|------|---------|---------|
| T10 | Risk & Business Plan | 5 videos | Max loss, 5 profitability factors, risk framework |
| T11 | Method Architecture | 1 video | Reading + Attack + Management = Complete Method |
| T13 | Chart Analysis Methodology | 1 video | 3 study methods: past complete, past reviewed, moving chart |
| T16 | Business Plan Compliance | 4 videos | Restaurant analogy, positive numerical expectancy, consistent menu |

---

## The 40 Analyzed Videos

### Batch 1 — Original 20 (Core Method)
| # | Video ID | Title |
|---|----------|-------|
| 1 | 3ilsV4UU5Y0 | Understanding Fractality |
| 2 | 4b2ZAImaATk | Fractality Practice Example |
| 3 | 6U91ZG1e80g | Many Ways to Win and Lose |
| 4 | ExKdYnCebqY | Must Keep This In Mind |
| 5 | GrH-mtabADo | Setbacks - Enemy of Novice Traders |
| 6 | M70f76duW2s | Good/Bad Use of Partials |
| 7 | QNRJX4b7Qq4 | Students Preferred Ratios |
| 8 | Tiy6bO9hXJ4 | Trading Gold & Silver |
| 9 | aUHXlpn-iRc | Value Left Side of Charts |
| 10 | fk3luzBRmHA | Work on Context in Chart |
| 11 | ijMX71M37Uw | Gold Trading with the Kids |
| 12 | koKCbtrB_eI | Better Explained Live |
| 13 | p9aw5DkgFX8 | Evolution of Cycles |
| 14 | u6K3H8d-4J0 | Super Winning Trades |
| 15 | wmqmqzn_Ito | Analysis vs Strategy vs Method |
| 16 | SbIr86IVdvA | Practice Finding Points of Control |
| 17 | OMNRlfZzZmU | Fractality and Level Breaks |
| 18 | JgTMWX3hjY0 | Failure Management in Trading |
| 19 | YmdLBEThXvQ | Entry Timing for Good Ratios |
| 20 | uYgJBc6TehE | Trend Breaks Without Lines |

### Batch 2 — Hedging & Position Sizing (10 videos)
| # | Video ID | Title |
|---|----------|-------|
| 21 | UagTOjoC4us | Proper Use of Hedging Simplifies Management |
| 22 | LtSfnLbTPMI | Coberturas, Essential Part of My Trading |
| 23 | Fr4lEDnT2SM | Account Size Is Ridiculous |
| 24 | jdb0RQrQcbE | All Positions Stopped But I Win |
| 25 | UKv_l1zUPr8 | Hedging Can Yield Very Good Results |
| 26 | I9ZbsIRYxAg | Why I Like CFDs — Hedging Options |
| 27 | g44ncKXTQYY | Only Add Positions If Price Agrees |
| 28 | -1ynDl64noU | Constant Hedging |
| 29 | bzJTdS2tw5M | SP500 Hedging Example |
| 30 | ncC4_enuX-8 | Minimum Stop Sizes Required |

### Batch 3 — Psychology, Business Plan, Context (10 videos)
| # | Video ID | Title |
|---|----------|-------|
| 31 | 1vfxDbav44U | My Deception Pattern in Trading |
| 32 | J-sqjzmntCE | Create a Correct Business Plan (3/3) |
| 33 | aY_rYYg3GZ0 | If Your Results Curve Falls, It's Your Fault |
| 34 | G_22Hli7Hls | A Trading Method Is Not What They Told You |
| 35 | 1YCSx7gXPF0 | Drawdown Debate: Joaquin, Pablo, Victor |
| 36 | zcP866VYuI8 | I Don't Want High Accuracy, I Want Money |
| 37 | HLVeiM-z1S0 | Context Always Commands |
| 38 | 5jrIu_WmAsY | Intraday SP500 Trading Day |
| 39 | S7pK5Oj6kyo | Include Null Operations in Your Trading |
| 40 | CInOSEOYEIg | Profit Ratio Per Trade |

---

## 16 Audio Clips — Joaquin's Voice

These are the most iconic phrases, extracted directly from the videos via ffmpeg:

| Clip ID | Duration | Spanish Phrase | English Translation |
|---------|----------|----------------|---------------------|
| si_o_si | 3.0s | "Eso era venta si o si" | That was a sell, no question |
| hay_que_darle_si_o_si | 6.0s | "Ya sabeis que estas son las tipicas operaciones donde yo le tengo que dar si o si" | You already know these are the typical trades where I must take them |
| punto_de_control | 7.5s | "Imaginaos que esto es un punto de control de una caida" | Imagine this is a point of control of a drop |
| retroceso_imprescindible | 6.0s | "El retroceso es la condicion imprescindible" | The retracement is the essential condition |
| no_sigo_tendencias | 8.5s | "Yo no funciono asi, no sigo tendencias, lo unico que sigo es fractalidad" | I don't follow trends, I only follow fractality |
| fractalidad | 15.0s | "La fractalidad. Esto es uno de los conceptos mas importantes. Y si no se domina, estamos jodidos de cojones" | Fractality. If you don't master it, we're completely screwed |
| plan_de_negocio | 10.0s | "Un dinero que yo tengo establecido como maxima perdida en mi plan de negocio" | A fixed amount I've established as maximum loss in my business plan |
| doble_direccion | 5.0s | "Tu pensamiento es siempre doble direccion" | Your thinking is always dual-direction |
| cobertura | 6.5s | "Que entendais que yo siempre trabajo con doble direccion" | Understand that I always work with dual-direction |
| sin_ubicacion_del_mapa | 15.5s | "Lo que yo no puedo tener es una estrategia de atacar el precio si no tengo una ubicacion del mapa" | I can never attack price without knowing my location on the map |
| tomas_de_liquidez | 9.5s | "Que venga aqui y tire, que venga aqui y tire. Solo por pura liquidez" | Price comes here and bounces. Pure liquidity |
| imprescindible | 11.0s | "Diferenciar los contextos para diferenciar los lotajes de entrada. Esto es imprescindible" | Differentiate contexts to differentiate entry lot sizes. Essential |
| colchon | 7.0s | "Mi obsesion es tener un colchon que sepa que lo que haga es gratis" | My obsession is having a cushion so whatever I do is free |
| parcial_si_o_si | 3.0s | "Aqui se sacaria un parcial si o si" | Here you'd take a partial, no question |
| zona_de_compra | 3.0s | "Sin duda esto es zona de compra" | Without a doubt, this is a buy zone |
| break_even_si_o_si | 8.5s | "Cojo las tres posiciones y las pongo en break-even. Que me las va a sacar si o si" | I put all three positions at break-even. It's going to hit them all |

---

## Media System Per Tree

Each tree has a media bar in the header with clickable chips:

| Tree | Frames | YouTube Links | Audio Clips |
|------|--------|---------------|-------------|
| entry (Should I Enter?) | 4 | 2 | 4 |
| T1 Cycle Identification | 6 | 3 | 4 |
| T2 Fractality & Evolution | 6 | 3 | 2 |
| T3 Retracement Completion | 3 | 1 | 1 |
| T4 Context Reading | 6 | 3 | 2 |
| T5 Entry Strategy | 10 | 5 | 4 |
| T6 Trade Classification | 3 | 1 | 0 |
| T7 Post-Entry Mgmt | 12 | 6 | 2 |
| T8 Partial Strategy | 6 | 3 | 1 |
| T9 161-200 Zone | 8 | 4 | 0 |
| T10 Risk & Business Plan | 10 | 5 | 2 |
| T11 Method Architecture | 3 | 1 | 1 |
| T12 Super-Winner | 8 | 4 | 0 |
| T13 Chart Analysis | 3 | 1 | 1 |
| T14 Hedging | 16 | 8 | 3 |
| T15 Deception Pattern | 3 | 1 | 0 |
| T16 Business Plan Check | 8 | 4 | 1 |
| T17 Drawdown Mgmt | 3 | 1 | 1 |
| T18 Context Assessment | 6 | 3 | 1 |
| T19 Null Operations | 6 | 2 | 1 |
| **TOTAL** | **130** | **61** | **31** |

---

## Webapp Features

### 1. "Should I Enter?" — Master Decision Tree
The primary entry point. A 13-node bilingual decision tree that walks through:
1. Business plan defined?
2. Points of Control identified?
3. Active cycle (38.2% retracement)?
4. Context checked (left side)?
5. Cycle still valid (no evolution/break)?
6. Price in tradeable zone with bias?
7. Confluence present?
8. Entry trigger type (zone/liquidity/61.8/Fib)

Each node has Joaquin's Spanish quotes and playable audio clips.

### 2. AI Search
Fuzzy keyword search across all 20 trees (~200+ nodes). Matches on questions, actions, explanations, notes, quotes — in both languages. Weighted scoring: exact phrase matches score highest, then key term matches (38.2, 61.8, fractal, liquidez, etc.), then individual word matches.

Example queries: "price retraced to 38.2%", "should I hedge?", "I'm in 15% drawdown", "pattern de engano"

### 3. Step-by-Step Mode
Interactive walkthrough — answer Yes/No questions, follow the path, see explanations and Joaquin quotes at each step. Breadcrumb trail to go back. Frame thumbnails at root level.

### 4. Full Tree Mode
Visual tree rendering showing all branches at once. Nodes color-coded: blue (question), green (action/enter), yellow (wait), red (stop/don't enter).

### 5. Session Workflow
The 16-step execution flow from T10 → T17 → T11 → T13 → T1 → T4/T18 → T2 → T3 → T9 → T15 → T5 → T7/T8 → T14 → T19 → T12 → T6. Click any step to jump to that tree.

### 6. EN/ES Language Toggle
Complete bilingual support. Spanish mode uses Joaquin's actual phrasing — not translations, but how he would say it. Toggle in sidebar and mobile header.

### 7. Media Bar
Below each tree title: purple audio chips, cyan screenshot chips (with count), red YouTube chips linking to source videos at exact timestamps. Click screenshots to open fullscreen lightbox.

### 8. Lightbox Viewer
Fullscreen frame viewing with:
- Arrow key navigation (left/right)
- Bilingual captions from the analysis
- Direct YouTube link per frame (jumps to that exact moment)
- Escape to close, click outside to close

---

## Core Method Numbers (Quick Reference)

| Number | Meaning |
|--------|---------|
| **38.2%** | Cycle activation — impulse + retracement to 38.2 = activated cycle |
| **61.8%** | Primary working zone — does NOT trigger evolution |
| **130%** | Retracement completion — not finished until 130% touched |
| **161.8%** | First failure projection target (better in currencies) |
| **200%** | Extended failure target (better in indices/commodities) |
| **1/3 Rule** | PoC validation and break confirmation |
| **25% Rule** | Movement origin quality — less than 25% = failure = defective origin |
| **10% Rule** | When floating profit > 10% of balance, take some off |
| **1:4** | Minimum risk-reward ratio (restaurant: charge 4x cost) |
| **12 pips** | Minimum stop in Forex (never less) |
| **15%** | Drawdown threshold: STOP trading |
| **22.5%** | Drawdown: consider 6-month break |
| **30%** | Drawdown: CRITICAL, return to demo |

---

## Processing Pipeline

```
YouTube Video
    ↓ yt-dlp (download)
Video File (.mp4)
    ↓ ffmpeg -vn -acodec libmp3lame
Audio File (.mp3)
    ↓ OpenAI Whisper API
Transcription (.json with timestamps)
    ↓ GPT-4o analysis prompt
Analysis (.json with key_concepts, decision_tree, rules)
    ↓ ffmpeg (every 30s)
Frame Screenshots (.jpg)
    ↓ Claude Code aggregation
Decision Trees (trees.json v3.0)
    ↓ ffmpeg (precise timestamp cuts)
Audio Clips (clips/*.mp3)
    ↓ Python media mapping
Media Manifest (media_manifest.json)
    ↓ git push
GitHub Pages (live webapp)
```

---

## Git History

```
8334a89 add media system: 115 chart screenshots, lightbox viewer, youtube links per tree
473b3ff add 16 joaquin audio clips (864KB total)
16f1358 add en/es language toggle, joaquin audio clips on quotes
f6f0dc5 remove cname redirect to surge
90c23a1 v3.0: 19 trees from 40 videos, hedging/context/deception/drawdown/null ops
26f7cdc v2: should i enter tree, ai search, interactive flow
3177592 joaquin vega decision tree webapp
```

---

## Known Gaps in the Method

These concepts are referenced but not fully defined in the analyzed videos:

| Gap | Description |
|-----|-------------|
| Pattern 1/2 exact definitions | Referenced as entry triggers but not detailed |
| 25% rule base measurement | Which candle/level is the 25% measured from? |
| Break level placement | Confirmed by 1/3 rule, but where is the base level exactly? |
| Lot sizing formula | Comes from business plan, no formula documented |
| Multi-timeframe priority | Joaquin says same concept applies on all TFs, no priority specified |
| Stop placement formula | Per business plan, no zone-distance formula given |
| Super-winner exit criteria | "Decide at entry" but specific criteria not detailed |

---

## Deployment

### GitHub Pages
- Repository: `kilazi/joaquin-method`
- Branch: `main`
- Files must be at **root level** (not in `webapp/` subdirectory)
- All files are duplicated: `webapp/` (source) and root (deployment)
- `.gitignore` has exceptions for `!clips/*.mp3`, `!frames/*.jpg`, `!webapp/frames/*.jpg`

### Important Notes
- Video directories (`*/video.mp4`, `*/audio.mp3`, `*/*.jpg`) are gitignored (too large)
- Frame files are explicitly un-ignored with `!frames/*.jpg`
- No CNAME file (was causing redirect to surge.sh — removed)

---

## Brainstorm Follow-Up Plans

*Pulled from Kortex brainstorms on 2026-02-25:*

### 1. Interactive Cloud Code Session for Trading
**Status:** Brainstorm idea
**Description:** Instead of just a static cheat sheet, create an interface where Claude Code can be initiated as a live session with full knowledge of the Joaquin method. The user describes their chart situation, and Claude walks them through the decision tree in real-time with chart analysis capabilities.
**Next steps:**
- Design an API or webhook that takes a chart screenshot + user context
- Claude processes it against the full method knowledge base (JOAQUIN_METHOD_REFERENCE.md + trees.json)
- Returns specific tree node recommendation with zone identification
- Could be a Telegram bot, web interface with image upload, or Claude Code slash command

### 2. Kortex + Cloud Code Voice Integration
**Status:** Brainstorm idea
**Description:** Enable voice-based communication between the user and Cloud Code via phone calls or messaging apps (WhatsApp/Telegram). Cloud Code runs in a persistent session, waiting for calls to initiate actions. When a trading session ends, Cloud Code calls the user to debrief.
**Relevance to Joaquin Method:** Could be used for:
- Voice-activated trade journal entries
- Real-time trading coaching ("I'm looking at gold, price just entered high zone, what should I do?")
- Post-session analysis calls
**Next steps:**
- Explore WAPI (WhatsApp API) or Telegram Bot API
- Reference MoldBot project (Steve's similar implementation)
- Design the "sleep mode" session that watches for incoming events

### 3. Live Chart Analysis Integration
**Status:** Not started
**Description:** Connect the webapp to live chart data (via TradingView API, broker API, or screenshot analysis) to automatically identify:
- Current cycles and their activation status
- Active zones (high/low/61.8)
- Confluence points
- Context quality (good/regular/weak)
**Next steps:**
- Explore TradingView Pine Script integration
- Consider browser extension that reads chart data
- Or: screenshot upload → GPT-4V analysis → map to tree nodes

### 4. Trade Journal with Method Compliance Scoring
**Status:** Not started
**Description:** Track every trade against the decision trees. Did you follow T1-T19? Score each trade for method compliance. Track your results curve per Joaquin's framework.
**Fields per trade:**
- Entry tree path taken (which nodes were Yes/No)
- Context quality assessment (Good/Regular/Weak from T18)
- Position sizing compliance (per T16 business plan)
- Management compliance (T7 rules followed?)
- Outcome (T6 classification: loser/null/positive/winner/very winner)
- Drawdown tracking (T17 segment)
**Next steps:**
- Add a "Log Trade" feature to the webapp
- Store in localStorage or simple backend
- Generate compliance reports and results curves

### 5. More Video Analysis
**Status:** Ongoing
**Description:** Joaquin has more videos beyond the 40 analyzed. The channel may also have newer content. Continue expanding the knowledge base.
**What to look for:**
- Newer videos with updated concepts
- Live trading sessions (practical application)
- Q&A sessions (clarify known gaps)
- Guest videos with other traders

### 6. Mobile UI for Remote Claude Code Control
**Status:** Not started (ties into brainstorm #2 — voice/messaging integration)
**Description:** A mobile-first interface (web app or Telegram bot) that connects to Claude Code running persistently on the home machine. Send commands from your phone, get results back, trigger actions remotely — without needing to sit at the computer.
**Use cases:**
- "Analyze this chart" — send a screenshot from phone, Claude Code processes it against the Joaquin method knowledge base
- "What's the status of X?" — query running sessions
- "Deploy the latest changes" — trigger git push / deploy from phone
- "Start processing these 5 new Joaquin videos" — kick off batch jobs
- "Log this trade" — voice note or text → Claude Code logs it with method compliance
**Architecture ideas:**
- Home machine runs Claude Code in persistent/sleep mode, watching for incoming requests
- Telegram Bot API or simple webhook endpoint on the home machine
- Messages go in → Claude Code picks them up → executes → sends result back
- Could piggyback on Kortex API as the message bus
- Reference: MoldBot project (Steve's similar implementation)
