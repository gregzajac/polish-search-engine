from load import load_articles
from search.index import Index


if __name__ == "__main__":
    index = Index()
    # index.index_articles(load_articles())
    # index.save()
    index.load()
    index.search("Uwłaszczenie")

    # result = json.dumps([(a.to_dict()) for a in load_articles()])
    # print(result)
    # print()
    # print(json.loads(result))
    # for a in load_articles():
    #     print(json.dumps(a.to_dict()))
