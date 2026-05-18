import ollama

client = ollama.Client(
    host="http://ollama:11434"
)


class SynthesisAgent:

    def synthesize(self, question: str, analysis: str):

        prompt = f"""
You are a synthesis agent for an enterprise AI assistant.

Your responsibilities:
- generate a clean final answer
- keep responses concise and professional
- avoid hallucinations
- use only the provided analysis
- clearly state when information is uncertain

Analysis:
{analysis}

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