import os
from tavily import TavilyClient


class WebSearchAgent:

    def __init__(self):

        api_key = os.getenv("TAVILY_API_KEY")

        self.client = TavilyClient(api_key=api_key)

    def search(self, query: str):

        response = self.client.search(
            query=query,
            search_depth="basic",
            max_results=3
        )

        results = []

        for item in response["results"]:

            results.append({
                "title": item["title"],
                "content": item["content"],
                "url": item["url"]
            })

        return results