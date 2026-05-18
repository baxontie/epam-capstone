from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from qdrant_client import QdrantClient
from agents.retrieval_agent import RetrievalAgent
from agents.analysis_agent import AnalysisAgent
from agents.synthesis_agent import SynthesisAgent
from agents.web_search_agent import WebSearchAgent
from agents.query_router_agent import QueryRouterAgent

import ollama

client = ollama.Client(
    host='http://ollama:11434'
)

qdrant = QdrantClient(
    host="qdrant",
    port=6333
)

COLLECTION_NAME = "enterprise_docs"

retrieval_agent = RetrievalAgent()
analysis_agent = AnalysisAgent()
synthesis_agent = SynthesisAgent()
web_search_agent = WebSearchAgent()
query_router_agent = QueryRouterAgent()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "AI Service Running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@app.get("/ask")
async def ask(question: str):

    response = client.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return {
        "question": question,
        "answer": response["message"]["content"]
    }

@app.get("/search")
async def search(query: str):

    embedding_response = client.embeddings(
        model="nomic-embed-text",
        prompt=query
    )

    query_vector = embedding_response["embedding"]

    results = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=3
    ).points

    response = []

    for result in results:
        response.append({
            "score": result.score,
            "filename": result.payload["filename"],
            "content": result.payload["content"]
        })

    return {
        "query": query,
        "results": response
    }

@app.get("/rag-ask")
async def rag_ask(question: str):

    workflow = []

    route = query_router_agent.route(question)

    workflow.append({
        "agent": "QueryRouterAgent",
        "status": "completed",
        "route": route
    })

    results = []

    if route == "internal":
        results = retrieval_agent.search(question)

    if route == "external" or not results or results[0]["score"] < 0.55:

        workflow.append({
            "agent": "RetrievalAgent",
            "status": "insufficient_context"
        })

        web_results = web_search_agent.search(question)

        combined_content = " ".join([
            result["content"]
            for result in web_results
        ])

        validation_prompt = f"""
        Question:
        {question}

        Retrieved Context:
        {combined_content}

        Determine whether the retrieved context is truly relevant
        and sufficient to answer the question reliably.

        If the context is weak, absurd, unrelated,
        or insufficient, answer ONLY:

        INSUFFICIENT_CONTEXT

        Otherwise answer ONLY:

        SUFFICIENT_CONTEXT
        """

        validation_response = client.chat(
            model="qwen2.5:7b",
            messages=[
                {
                    "role": "user",
                    "content": validation_prompt
                }
            ]
        )

        validation_result = validation_response["message"]["content"].strip()

        if "INSUFFICIENT_CONTEXT" in validation_result:

            workflow.append({
                "agent": "ValidationAgent",
                "status": "rejected_low_confidence"
            })

            return {
                "question": question,
                "answer": "I could not find reliable information to answer this request confidently.",
                "citations": [],
                "workflow": workflow
            }

        workflow.append({
            "agent": "WebSearchAgent",
            "status": "completed",
            "sources_found": len(web_results)
        })

        web_context = "\n\n".join([
            item["content"]
            for item in web_results
        ])

        analysis = analysis_agent.analyze(
            question=question,
            documents=[
                {
                    "content": web_context
                }
            ]
        )

        workflow.append({
            "agent": "AnalysisAgent",
            "status": "completed"
        })

        final_answer = synthesis_agent.synthesize(
            question=question,
            analysis=analysis
        )

        workflow.append({
            "agent": "SynthesisAgent",
            "status": "completed"
        })

        return {
            "question": question,
            "answer": final_answer,
            "citations": [
                item["url"]
                for item in web_results
            ],
            "workflow": workflow,
            "source": "external_web_search"
        }

    workflow.append({
        "agent": "RetrievalAgent",
        "status": "completed",
        "documents_found": len(results)
    })

    analysis = analysis_agent.analyze(
        question=question,
        documents=results
    )


    workflow.append({
        "agent": "AnalysisAgent",
        "status": "completed"
    })

    final_answer = synthesis_agent.synthesize(
        question=question,
        analysis=analysis
    )

    workflow.append({
        "agent": "SynthesisAgent",
        "status": "completed"
    })

    citations = [
        result["filename"]
        for result in results
    ]

    return {
        "question": question,
        "answer": final_answer,
        "citations": citations,
        "workflow": workflow
    }