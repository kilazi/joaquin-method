# Data Gaps Analysis — Joaquín Vega Method Decision Trees

Generated: 2026-02-25
Source: 15 video analyses from `all_analyses.json`

---

## Critical Gaps (Missing data prevents building complete decision paths)

### 1. Pattern 1 and Pattern 2 — Definitions Missing
**Trees affected:** T4 (Context Reading), T9 (161-200 Zone Trading)

The videos reference "Pattern 1" and "Pattern 2" (Pauta 1 / Pauta 2) as **objective measurements** used to evaluate zones and set expectations for 161.8 and 200 targets. However, the analyses do not contain:
- What exactly Pattern 1 measures
- What exactly Pattern 2 measures
- How they are drawn/calculated on the chart
- The relationship between Pattern 1 and Pattern 2
- When to use one vs. the other

**Quote from data:** *"Ha tocado la extensión que abajo de la medida de la pauta 2, las hipótesis cambian..."* — This shows patterns drive hypothesis changes, but we don't know how to construct them.

**Impact:** Cannot build the full context-reading decision path without knowing these measurements.

---

### 2. Entry Patterns (1 and 2) — Not Described
**Trees affected:** T5 (Entry Strategy)

Joaquín mentions teaching "entry patterns" on YouTube but explicitly says there are many ways to attack and the specific patterns are not the only way. The analyses reference patterns for entries but never describe:
- What Pattern 1 entry looks like
- What Pattern 2 entry looks like
- The specific candle/price structure that constitutes each
- How they differ from liquidity grabs

**Quote from data:** *"Mira, yo te enseño algunas, pero hay mil formas de atacar el precio."*

**Impact:** The entry strategy tree (T5) relies heavily on zone confluences and liquidity grabs because those are well-described. The specific named entry patterns are a gap.

---

### 3. Point of Control Identification — Criteria Unclear
**Trees affected:** T1 (Cycle Identification), T2 (Fractality/Evolution)

Points of Control are referenced constantly as the starting reference for cycles, but the data lacks:
- Exact criteria for what qualifies as a Point of Control
- How to distinguish a Point of Control from a random swing high/low
- Whether Points of Control have hierarchy (major vs. minor)
- How internal Points of Control relate to external ones
- The specific method for "unraveling" price through control points

**Quote from data:** *"Lógicamente, también vamos desentrañando la subida a través de puntos de control."*

**Impact:** The very first node of T1 (Cycle Identification) asks "Do you have a Point of Control?" but we cannot fully define what constitutes one from the available data.

---

### 4. Break Level Exact Calculation
**Trees affected:** T1, T2

Every cycle has a "break level" that determines when the cycle is dead. The data confirms break levels exist and are marked, but:
- The exact Fibonacci level or formula for calculating the break level is not specified
- Whether it's the same for uptrend and downtrend cycles
- Whether it relates to the impulse measurement or the zone boundaries

**Impact:** The break/evolve decision in T2 references "break level hit" but we can't specify where exactly that level sits.

---

### 5. 25% Movement Origin Rule — Incomplete
**Trees affected:** T4 (Context Reading)

The "defective origin" concept (movement didn't reach 25%) is mentioned as critical for identifying activated failures, but:
- 25% of what? The zone? The previous move? A pattern measurement?
- Is 25% a Fibonacci level or a proportional calculation?
- What constitutes a "correct" movement origin beyond reaching 25%?
- How is the 25% level calculated on the chart?

**Quote from data:** *"¿Esto es un origen de movimiento correcto? No. ¿Por qué no? Porque no ha llegado al 25%."*

**Impact:** The failure activation branch of T4 depends on identifying defective origins, which requires understanding the 25% rule precisely.

---

## Moderate Gaps (Data is partial — trees can be built but with assumptions)

### 6. Lot Sizing and Business Plan Numbers
**Trees affected:** T10 (Risk/Business Plan)

The data establishes that lot sizing comes from the "business plan" and a "line of work" (línea de trabajo) but never specifies:
- How the line of work is calculated
- What percentage of account constitutes max risk per trade
- How lot size scales with account size
- Whether there's a maximum number of simultaneous positions

The 10% floating profit rule is mentioned as a hard boundary, but is presented as a guideline rather than a formula.

---

### 7. Timeframe Selection
**Trees affected:** All trees

Joaquín states fractality works on all timeframes ("no importa en cuál estés, el concepto es el mismo"), but the data doesn't clarify:
- Which timeframes are recommended for which assets
- How to handle conflicting signals across timeframes
- Whether the cycle on a 15-minute chart takes precedence over a daily chart or vice versa
- The relationship between timeframe and the type of trade (scalp vs. swing vs. position)

---

### 8. Failure Mechanics — Detailed Progression
**Trees affected:** T9 (161-200 Zone), T4 (Context)

"Failure" (fracaso) is a core concept with two meanings:
1. A price movement that fails to sustain direction
2. A structural failure where highs/lows are broken

The data shows failures are critical for projections to 200 and for sell signals ("any 61.8 after failure of highs is a reason to sell"), but:
- The exact definition of when a "failure" is confirmed vs. just a retracement
- How many failures typically occur before the 200 level
- Whether there's a maximum number of failures before the thesis is invalidated

---

### 9. Coverage/Hedging Strategy
**Trees affected:** T7 (Post-Entry Management)

Brief mention of "coverage" (cobertura) when price reverses during a trade:
- *"Intentaré que cuando se me dé la vuelta intentaré cogerlo con alguna cobertura"*
- No details on how hedges are structured
- No information on when to place a hedge vs. simply exiting
- No guidance on hedge sizing

---

### 10. Multiple Position Entry — Beyond 2
**Trees affected:** T5, T7

Joaquín mentions entering with "2, 3, 4, 5, 6, 7 positions" in a trade, but the detailed mechanics are only described for:
- Single entry
- 2-part fractional entry ("from 3 it becomes confusing")

How entries of 3+ positions are structured, spaced, and managed is not covered in the available data.

---

## Minor Gaps (Context is available but specifics are missing)

### 11. Gold-Specific Adjustments
Gold is used as the primary example asset in multiple videos, with notes that it was "random" and "lacking fractality" for an extended period. But the data doesn't provide clear rules for:
- When to declare an asset is behaving too randomly for the method
- How long to wait before re-engaging
- Quantitative thresholds for "sufficient fractality"

### 12. Session/Time-of-Day Rules
No information on:
- Whether certain market sessions are better for the method
- Time-based filters for entries
- Whether sessions affect zone validity

### 13. Specific Stop Loss Placement
Stops are referenced as defined by the business plan, but:
- No specific guidance on initial stop placement relative to zones
- Whether stops are placed at the break level or elsewhere
- How to calculate stop distance for different timeframes

### 14. Losing Streak Management
Beyond the general "setbacks" discussion, there's no:
- Maximum consecutive losses rule
- When to reduce position size during drawdowns
- Recovery protocol after a significant drawdown

### 15. Cycle Concurrency
When multiple cycles from different Points of Control are active simultaneously:
- Which cycle takes priority?
- How to handle conflicting signals from concurrent cycles
- Whether to trade both or only the dominant one

---

## Recommendations for Filling Gaps

| Priority | Gap | Suggested Source |
|----------|-----|-----------------|
| **P0** | Pattern 1 / Pattern 2 definitions | Likely in the free YouTube course — search for "pauta 1 pauta 2 joaquín vega" |
| **P0** | Point of Control identification criteria | May be in introductory methodology videos |
| **P0** | Entry patterns (specific structures) | YouTube course likely covers these |
| **P1** | Break level calculation | May need a dedicated video on zone marking |
| **P1** | 25% origin rule details | Look for videos on "orígenes de movimiento" |
| **P1** | Failure mechanics (structural) | Search for "fracaso" or "failure" dedicated content |
| **P2** | Lot sizing / business plan template | May be in paid course content only |
| **P2** | Multi-timeframe rules | Likely discussed in live sessions |
| **P3** | All minor gaps | Will naturally be filled as more videos are analyzed |

---

## Coverage Assessment

| Method Area | Coverage | Notes |
|-------------|----------|-------|
| Cycle Identification | **70%** | Core flow is clear. Point of Control identification and break level calculation are gaps. |
| Fractality/Evolution | **85%** | Well covered across 3+ videos. The evolution mechanics are clearly described. |
| Context Reading | **60%** | Failure projections and liquidity are well covered. Pattern 1/2 and 25% origin rule are significant gaps. |
| Trade Entry | **65%** | Zone confluences and liquidity grabs are well described. Specific named patterns are missing. |
| Trade Management | **80%** | Partials, stop adjustments, and the five trade types are well documented. Coverage/hedging is a gap. |
| Risk Management | **55%** | Philosophy is clear but quantitative rules (lot sizing, drawdown protocols) are mostly missing. |
| Psychology | **90%** | Super-winner psychology, fear management, and discipline are thoroughly covered. |
| Method Architecture | **95%** | The reading/attack/management distinction is explicitly and clearly taught. |

**Overall Method Extraction:** ~72% complete from available data.
The remaining 28% is concentrated in the technical specifics (exact calculations, pattern definitions) that are likely covered in the foundational YouTube course or paid course material.
