# from langchain.agents import initialize_agent
# from langchain.llms import OpenAI

# def create_agent(tools):
#     llm = OpenAI()
#     return initialize_agent(tools, llm, agent="zero-shot-react-description")
from config.prompts import AGENT_PROMPT
from tools.search_tool import search_tool

def run_agent(query: str):
    print(f"Agent received: {query}")

    # Step 1: Think (simple logic for now)
    if "search" in query.lower():
        tool_result = search_tool(query)

        return f"""
        Thought: I should search for this
        Action: search_tool
        Observation: {tool_result}
        Final Answer: Based on search, here is the answer.
        """

    # Default response
    return f"Final Answer: {query}"