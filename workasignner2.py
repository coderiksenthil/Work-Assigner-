import requests
from bs4 import BeautifulSoup

def search_tasks(prompt):
    # Replace spaces with plus signs for the search query
    query = prompt.replace(" ", "+")
    
    # Perform a search on DuckDuckGo
    url = f"https://duckduckgo.com/html?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract and print search results
        results = soup.select('.result__a')
        for i, result in enumerate(results, 1):
            print(f"{i}. {result.text}")
    else:
        print(f"Error {response.status_code}: Unable to fetch search results")

# Example usage
prompt = input("Enter your task prompt: ")
search_tasks(prompt)
