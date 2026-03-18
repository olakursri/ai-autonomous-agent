# from fastapi import FastAPI
# from pydantic import BaseModel
# from agent.claude_simple_agent import run_agent

# app = FastAPI()

# class AgentRequest(BaseModel):
#     query: str

# @app.post("/agent")
# def agent_api(request: AgentRequest):
#     response = run_agent(request.query)
#     return {"response": response}

# @app.get("/")
# def root():
#     return {"message": "AI Agent is running 🚀"}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.openai_agent import run_agent

app = FastAPI()

class AgentRequest(BaseModel):
    query: str

@app.post("/agent")
def agent_api(request: AgentRequest):
    try:
        response = run_agent(request.query)
        return {"response": response}
    except Exception as e:
        print(f"ERROR: {e}")   # <--- This will show the real error
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "AI Agent running"}