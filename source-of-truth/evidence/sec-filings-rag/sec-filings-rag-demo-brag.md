# SEC Filings RAG — live end-to-end demo

**Recorded November 3, 2026 · Local run (FastAPI backend + Next.js frontend) · Video walkthrough of the personal SEC-filings RAG application**

## Brag document summary

I recorded a live, end-to-end walkthrough of my personal SEC-filings RAG application. The demo shows a filing-grounded answer streaming into the UI in real time (~22 s generation), the Multi-Stream Analysis agent producing parallel fundamental, momentum, and sentiment sections with a grade and recommendation for AAPL, and the underlying Qdrant Cloud hybrid collection (`financial`, ~170 points) with a real indexed chunk — including its payload metadata and its sparse, dense (384-dim), and ColBERT (216×128) vectors.

The recording was made by driving a headless Chrome session over the Chrome DevTools Protocol; the Qdrant dashboard API key was pre-seeded programmatically and never appeared on screen.

## What the recording shows

All items below are **[FATO]**, directly observable in `sec-filings-rag-demo.mp4` and the screenshots.

| Time | Scene | What is demonstrated |
|---|---|---|
| 0:00–0:10 | Landing page | Product shell: RAG/Agent mode toggle, grounded-answer positioning |
| 0:10–0:25 | RAG query typed and sent | "What is Apple's investment thesis?" submitted to the live local backend |
| 0:25–0:55 | Answer rendering | Grounded multi-pillar answer drawn from indexed filings/news, streaming into the UI |
| 0:55–1:40 | Agent mode on AAPL | 3-stream analysis (Fundamental grade + recommendation, Momentum, Sentiment) plus Key Risks / Key Opportunities panels |
| 1:40–2:06 | Qdrant Cloud dashboard | `financial` collection: status GREEN, ~170 points, vector config `dense 384 / sparse / colbert`; opened a real point with AAPL news payload (`source: yahoo_finance`, dated November 2, 2026) and its three vector lengths |

**Architecture shown in practice:** FastAPI backend with hybrid dense (`all-MiniLM-L6-v2`) + sparse (BM25) retrieval, RRF fusion and ColBERT reranking against Qdrant Cloud, LLM answers via Groq (`openai/gpt-oss-120b`); Next.js frontend adapted from `finlab-front`.

## Honest limits

- **[LIMIT]** Personal/course project running locally. Do not present as professional deployment, production operations, or measured answer quality.
- **[LIMIT]** Generation waits (~22 s RAG, ~22 s agent) were partially trimmed from the video; the unedited run also recorded slower first calls. Timings here are single observed samples, not benchmarks.
- **[LIMIT]** Agent output quality depends on indexed coverage: a MSFT test query returned a refusal because its filings were not indexed, and the sentiment stream occasionally reports "insufficient data" for tickers without news chunks. Not shown in the final cut.
- **[LIMIT]** The recording proves the pipeline runs end to end; it does not establish retrieval precision, recall, or latency metrics.
- **[FACT-CONTEXT]** Frontend behavior was improved the same day: switching RAG/Agent mode now clears the input and previous response (implemented during recording prep; verified live in the final cut).

## Sources

- [Video — sec-filings-rag-demo.mp4](./sec-filings-rag-demo.mp4) (126 s, 1280×640)
- [Screenshots](./screenshots/) — hero, RAG answer, agent result, risks/opportunities, Qdrant collections, point payload
- [Code — sec-filings-rag-app](https://github.com/santosdanilo/ai-specialization/tree/HEAD/sec-filings-rag-app) (backend) and `sec-filings-web` (frontend, same repository family)
- Canonical claim: `source-of-truth/evidence-ledger.md` E-020 and E-025
- Recording method documented in `guidelines/browser-demo-recording-workflow.md` (scripts in `guidelines/scripts/browser-demo-recording/`)

Recording method: Chrome DevTools Protocol screencast (headless Chrome, cloned local profile for the Qdrant Cloud session); frames timed from CDP timestamps; idle LLM wait windows cut with ffmpeg. No credentials were captured on screen.
