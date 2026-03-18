from duckduckgo_search import DDGS

def search(query):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)
        return results