# OpenLibrary Books API

A simple Python script that retrieves 50 books from the OpenLibrary API, filters books published after 2000, and saves the results in a CSV file.

## Features

* Fetches 50 books from the OpenLibrary API
* Filters books with a publication year after 2000
* Saves the filtered results in `books.csv`
* Stores the book title, author, and first publication year

## Requirements

* Python 3
* `requests`

Install the required package with:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command:

```bash
python main.py
```

After running the script, the filtered books will be saved in:

```text
books.csv
```

## Output

The CSV file contains the following columns:

* `title`
* `author`
* `first_publish_year`

Only books with a `first_publish_year` greater than 2000 are included.
