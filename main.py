import requests

url = "https://openlibrary.org/search.json"

response = requests.get(
    url=url,
    params={
        "q": "python",
        "fields": "title,author_name,first_publish_year",
        "limit": 50
    }
)

data = response.json()

print(data)
