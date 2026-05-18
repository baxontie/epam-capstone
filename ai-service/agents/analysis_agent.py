import ollama

client = ollama.Client(
    host="http://ollama:11434"
)


class AnalysisAgent:

    def analyze(self, question: str, documents: list):

        context = "\n\n".join([
            doc["content"]
            for doc in documents
        ])

        prompt = f"""
You are an enterprise documentation analysis agent.

Your responsibilities:
- analyze retrieved enterprise documents
- identify key findings
- identify risks or validation rules
- summarize important technical details

Answer ONLY using the provided context.

If information is missing, clearly state that.

Context:
{context}

Question:
{question}
"""

        response = client.chat(
            model="qwen2.5:7b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]