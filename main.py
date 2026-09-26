import requests
import csv

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

filtered_books = []

for book in books:

    year = book["first_publish_year"]
    if year > 2000:
        filtered_books.append(book)



print(filtered_books)


with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["title", "author", "first_publish_year"])

    for book in filtered_books:
        writer.writerow([
            book["title"],
            ", ".join(book["author_name"]),
            book["first_publish_year"]
        ])