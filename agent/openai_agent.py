# import os
# import openai

# # Make sure your OpenAI API key is set in environment variables
# # e.g., in PowerShell: $env:OPENAI_API_KEY="sk-xxxxxx"
# openai.api_key = os.getenv("OPENAI_API_KEY")


# def run_agent(query: str):
#     """
#     This agent uses OpenAI GPT-4 to respond to queries.
#     Works as a temporary replacement for Claude agent.
#     """
#     print(f"Agent received: {query}")

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are an intelligent AI assistant."},
#                 {"role": "user", "content": query}
#             ],
#             max_tokens=500,
#             temperature=0.7
#         )

#         answer = response.choices[0].message.content
#         return answer

#     except Exception as e:
#         print(f"OpenAI Agent ERROR: {e}")
#         return f"Error: {str(e)}"

# agents/openai_agent.py
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def run_agent(query: str):
    """
    GPT-4 agent using the new openai>=1.0 SDK
    """
    print(f"Agent received: {query}")

    try:
        # response = openai.chat.completions.create(
        #     model="gpt-4",
        #     messages=[
        #         {"role": "system", "content": "You are an intelligent AI assistant."},
        #         {"role": "user", "content": query}
        #     ],
        #     max_tokens=500,
        #     temperature=0.7
        # )
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Works for almost all accounts
            messages=[
                {"role": "system", "content": "You are an intelligent AI assistant."},
                {"role": "user", "content": query}
            ],
            max_tokens=500,
            temperature=0.7
        )
        answer = response.choices[0].message["content"]
        return answer

    except Exception as e:
        print(f"OpenAI Agent ERROR: {e}")
        return f"Error: {str(e)}"