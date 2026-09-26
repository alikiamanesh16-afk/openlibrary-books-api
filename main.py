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


books = data["docs"]

filtered_book = []

for book in books:

    year = book["first_publish_year"]
    if year > 2000:
        filtered_book.append(book)



print(filtered_book)
