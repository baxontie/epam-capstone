from qdrant_client import QdrantClient
import ollama

COLLECTION_NAME = "enterprise_docs"

qdrant = QdrantClient(
    host="qdrant",
    port=6333
)

client = ollama.Client(
    host="http://ollama:11434"
)


class RetrievalAgent:

    def search(self, query: str, limit: int = 3):

        embedding_response = client.embeddings(
            model="nomic-embed-text",
            prompt=query
        )

        query_vector = embedding_response["embedding"]

        results = qdrant.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=limit
        ).points

        documents = []

        for result in results:

            documents.append({
                "score": result.score,
                "filename": result.payload["filename"],
                "content": result.payload["content"]
            })

        return documents