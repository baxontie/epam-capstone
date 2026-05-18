class QueryRouterAgent:

    INTERNAL_KEYWORDS = [
        "registration",
        "organization",
        "approval",
        "authentication",
        "workflow",
        "validation",
        "enterprise",
        "account",
        "user"
    ]

    EXTERNAL_KEYWORDS = [
        "angular",
        "react",
        "kubernetes",
        "docker",
        "terraform",
        "aws",
        "azure",
        "devops",
        "frontend"
    ]

    def route(self, question: str):

        normalized = question.lower()

        for keyword in self.EXTERNAL_KEYWORDS:

            if keyword in normalized:

                return "external"

        for keyword in self.INTERNAL_KEYWORDS:

            if keyword in normalized:

                return "internal"

        return "internal"