from load import load_articles
from search.index import Index


index = Index()

if __name__ == "__main__":
    if index.is_saved():
        index.load()
    else:
        index.index_articles(load_articles())
        index.save()

    print("\nUwłaszczenie --> ", index.search("Uwłaszczenie"))
    print("\nksiążek --> ", index.search("książek"))
