from pathlib import Path
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import ollama
import uuid

COLLECTION_NAME = "enterprise_docs"

qdrant = QdrantClient(
    host="qdrant",
    port=6333
)

ollama_client = ollama.Client(
    host="http://ollama:11434"
)

docs_path = Path("/data")


def create_collection():
    collections = qdrant.get_collections().collections
    exists = any(c.name == COLLECTION_NAME for c in collections)

    if not exists:
        qdrant.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=768,
                distance=Distance.COSINE
            )
        )

        print(f"Collection '{COLLECTION_NAME}' created.")
    else:
        print(f"Collection '{COLLECTION_NAME}' already exists.")


def get_embedding(text: str):

    response = ollama_client.embeddings(
        model="nomic-embed-text",
        prompt=text
    )

    return response["embedding"]


def ingest_documents():

    markdown_files = docs_path.glob("*.md")

    for file in markdown_files:

        content = file.read_text(encoding="utf-8")

        embedding = get_embedding(content)

        point = PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding,
            payload={
                "filename": file.name,
                "content": content
            }
        )

        qdrant.upsert(
            collection_name=COLLECTION_NAME,
            points=[point]
        )

        print(f"Ingested: {file.name}")


if __name__ == "__main__":
    create_collection()
    ingest_documents()