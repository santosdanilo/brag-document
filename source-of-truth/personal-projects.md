# Personal Projects

<!-- List your side projects and open-source contributions. -->

## [Project Name] ([Tech Stack])
[Brief description of what the project does and why you built it]
- **Stack:** [Technologies used]
- **Features:** [Key features]
- **Goal:** [What you wanted to learn or achieve]
- **Link:** [github.com/your-username/project-name]

## [Another Project] (Open Source)
[Brief description]
- **Stack:** [Technologies used]
- **Contribution:** [What you built or contributed]
- **Link:** [github.com/your-username/project-name]

## AWS-Deployed Web Application (Personal Project)
Built and deployed a personal web application using AWS services.
- **Stack:** EC2, CodeBuild, CodePipeline, S3, CloudFront
- **Contribution:** Configured the EC2 instance, build/deployment pipeline, and S3/CloudFront delivery.
- **Project purpose and link:** Not yet documented.

## Django Web Application (Personal Project)
Implemented a web application using Django.
- **Stack:** Python, Django
- **Duration:** About two months; dates and application purpose not provided.

## RAG Pipeline (Personal Project)
Implemented a retrieval-augmented generation pipeline.
- **Stack:** Python, scikit-learn, NumPy
- **Duration:** About two months; dates and further implementation details not provided.

## SEC Filings RAG Application (AI Specialization Course)
Built a personal RAG application during the AI specialization course, integrating an LLM API with document retrieval to answer questions about SEC filings.
- **Stack:** Python, Groq API, Qdrant, FastEmbed, dense and sparse embeddings, BM25, Reciprocal Rank Fusion (RRF), ColBERT
- **Contribution:** Integrated Groq Chat Completions with retrieved document context; implemented hybrid retrieval combining dense and sparse embeddings through RRF, followed by ColBERT reranking. Returned generated answers with retrieval metadata and scores.
- **Configured default LLM:** `openai/gpt-oss-120b`, served through Groq; configurable in application settings.
- **Link:** https://github.com/santosdanilo/ai-specialization/tree/HEAD/sec-filings-rag-app
- **Evidence:** User confirmed personal implementation during the Velozient registration conversation on 2026-10-30. Repository implementation reviewed in `api/services/rag.py`, `api/services/search.py`, `api/services/embeddings.py`, and `api/config/settings.py`.
- **Limits:** Personal/course project, not professional production AI ownership. Dates, duration, usage, and evaluation metrics are not documented. Its relationship to the separately documented RAG Pipeline above has not been established.
