from langchain.agents import initialize_agent
from langchain.llms import OpenAI

def create_agent(tools):
    llm = OpenAI()
    return initialize_agent(tools, llm, agent="zero-shot-react-description")