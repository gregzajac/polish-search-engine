import json
import os.path

from load import load_articles
from search.index import Index


def index_articles(articles, index):
    for i, article in enumerate(articles):
        index.index_article(article)
    return index


def save_index():
    """Build and save the index for all articles"""
    index = index_articles(load_articles(), Index())
    print(index, type(index))
    # with open("data/search.json", "w") as f:
    #     f.write(index)


def load_index():
    """Load the index of all articles"""
    with open("data/search.json", "r") as f:
        result = f.read()
        return json.loads(result)


if __name__ == "__main__":
    if not os.path.exists("data/search.json"):
        save_index()
        print("Zapis pliku")
    else:
        print("Plik istnieje")
    # index = load_articles()
    # index.search("Uwłaszczenie")
