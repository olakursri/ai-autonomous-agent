import os
from anthropic import Anthropic
from tools.search_tool import search_tool

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """
You are an intelligent AI agent.

You can:
- Answer questions
- Use tools when needed

Available tools:
1. search_tool(query)

When needed:
- Decide the tool
- Use it
- Then give final answer

Respond in this format:
Thought:
Action:
Observation:
Final Answer:
"""

def run_agent(query: str):
    print(f"Agent received: {query}")

    # Step 1: Ask Claude what to do
    response = client.messages.create(
        model="claude-3-haiku-20240307",  # fast + cheap
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": query}]
    )

    output = response.content[0].text

    # Step 2: Simple tool trigger (basic parsing)
    if "search_tool" in output.lower():
        tool_result = search_tool(query)

        final_response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": query},
                {"role": "assistant", "content": output},
                {"role": "user", "content": f"Tool result: {tool_result}"}
            ]
        )

        return final_response.content[0].text

    return output