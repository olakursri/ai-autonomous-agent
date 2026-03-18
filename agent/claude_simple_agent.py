import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def run_agent(query: str):
    print(f"[Claude Simple Agent] Received: {query}")

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=500,
        messages=[
            {"role": "user", "content": query}
        ]
    )

    return response.content[0].text