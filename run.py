from load import load_articles
from search.index import Index


index = Index()
searchings = [
    "Uwłaszczenie",
    "Książek",
    "TralaLala",
]

if __name__ == "__main__":
    if index.is_saved():
        index.load()
    else:
        index.index_articles(load_articles())
        index.save()

    for search in searchings:
        print(
            f"\nThe result of searching the text '{search}' is:\n"
            f"{index.search(search)}",
        )
