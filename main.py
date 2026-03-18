from tools.web_search import search

if __name__ == "__main__":
    query = input("Enter task: ")
    result = search(query)
    print(result)