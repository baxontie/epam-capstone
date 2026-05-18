# Intelligent Enterprise Documentation Assistant

AI-powered hybrid multi-agent enterprise documentation platform built with Retrieval-Augmented Generation (RAG), external web augmentation, and intelligent orchestration.

The platform enables enterprise users to retrieve, analyze, and synthesize technical documentation, API references, troubleshooting guides, and release information using a multi-agent AI architecture.

---

# Project Goals

The project demonstrates practical application of Generative AI techniques for enterprise software development scenarios.

Key objectives:
- semantic enterprise knowledge retrieval
- multi-agent orchestration
- hybrid internal/external AI workflows
- hallucination prevention
- explainable AI responses
- automated AI behavior testing

---

# Key Features

## Multi-Agent Architecture

The system includes multiple specialized AI agents:

- QueryRouterAgent
- RetrievalAgent
- WebSearchAgent
- AnalysisAgent
- SynthesisAgent

---

## Retrieval-Augmented Generation (RAG)

Enterprise documentation is:
- embedded using Ollama
- indexed in Qdrant
- retrieved via semantic vector search

---

## Hybrid AI Workflow

The platform supports:
- internal enterprise knowledge retrieval
- external web fallback using Tavily search
- intelligent routing logic

---

## Explainable AI

The system provides:
- workflow traces
- citations
- routing visibility
- document attribution

---

## Automated Testing

Includes:
- positive AI behavior tests
- adversarial prompt validation
- routing tests
- orchestration verification

---

# System Architecture

```text
Angular Frontend
        ↓
FastAPI Multi-Agent Backend
        ↓
QueryRouterAgent
        ↓
Internal RAG OR External Tavily Search
        ↓
AnalysisAgent
        ↓
SynthesisAgent
        ↓
Workflow Trace + Citations
```

---

# Technology Stack

## Frontend
- Angular
- TypeScript
- CSS

---

## Backend
- Python
- FastAPI
- LangChain
- LangGraph

---

## AI & RAG
- Ollama
- Qwen2.5
- Qdrant
- Tavily Search API

---

## Infrastructure
- Docker
- Docker Compose

---

# Project Structure

```text
frontend/                  Angular frontend UI
ai-service/                Multi-agent AI backend
datasets/enterprise-docs/  Enterprise knowledge base
tests/                     Automated AI behavior tests
ARCHITECTURE.md            Architecture blueprint
README.md                  Project documentation
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
cd epam-capstone
```

---

## 2. Configure Environment Variables

Create `.env` file:

```env
TAVILY_API_KEY=your_api_key
```

---

## 3. Start Infrastructure

```bash
docker compose up -d --build
```

---

## 4. Pull Ollama Model

```bash
docker exec -it ollama ollama pull qwen2.5:7b
docker exec -it ollama ollama pull nomic-embed-text
```

---

## 5. Ingest Enterprise Documents

```bash
docker exec -it ai-service python ingest.py
```

---

## 6. Start Angular Frontend

```bash
cd frontend
npm install
npm start
```

Frontend:
```text
http://localhost:4200
```

Backend:
```text
http://localhost:8000
```

---

# Example Queries

## Internal Enterprise Queries

- What causes duplicate registration errors?
- How to fix Access-Control-Allow-Origin errors?
- What security improvements were added in release 1.2?
- What causes expired token errors?

---

## External Web Search Queries

- What is the latest Angular authentication best practice?
- What are current Kubernetes security recommendations?

---

# Automated Tests

Run AI behavior tests:

```bash
python -m pytest tests/test_rag.py
```

Test coverage includes:
- positive retrieval scenarios
- negative/adversarial prompts
- routing validation
- web search fallback
- workflow verification

---

# Security & Safety

Implemented safeguards:
- hallucination prevention
- insufficient context detection
- external routing controls
- CORS protection
- workflow tracing
- source attribution

---

# Observability

The platform provides:
- agent workflow tracing
- routing visibility
- source attribution
- citations
- orchestration transparency

---

# Future Improvements

Potential future enhancements:
- advanced LangGraph orchestration
- streaming responses
- authentication & RBAC
- feedback/rating systems
- semantic reranking
- hybrid search
- monitoring dashboards

---

# Demo Highlights

The project demonstrates:
- enterprise RAG architecture
- multi-agent collaboration
- hybrid AI workflows
- MCP-style external integrations
- AI observability
- automated AI validation

---

# Author

EPAM Generative AI for Software Development Capstone Project