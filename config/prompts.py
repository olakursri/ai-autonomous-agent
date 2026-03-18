# config/prompts.py

SYSTEM_PROMPT = """
You are an intelligent AI assistant capable of solving complex tasks.

You can:
- Search the web
- Perform calculations
- Analyze results

Always:
1. Break down the problem
2. Choose the right tool
3. Provide a clear final answer
"""

TASK_PROMPT_TEMPLATE = """
User Task:
{task}

Think step by step and decide the best action.
"""