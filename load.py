from search.article import Article


def load_articles():
    yield Article(
        1, "title1",
        "książek książkowy książkowa ujmująca niezwłocznie",
        "url1", 10, "Category1",
    )
    yield Article(
        2, "title2",
        "książkowo, książeczkowo w ujmującym uwłaszczeniu",
        "url2", 20, "Category1",
    )
    yield Article(
        3, "title3",
        "ujmująco w uwłaszczonym stylu",
        "url3", 30, "Category2",
    )
