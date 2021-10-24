import os

from search.analysis import analyze


class Index:
    """Index of articles representation"""
    def __init__(self):
        self.index = {}
        self.articles = {}
        self.path_to_file = "data/search.json"

    def index_article(self, article):
        if article.id not in self.articles:
            self.articles[article.id] = article
            article.analyze()

        for token in analyze(article.fulltext):
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(article.id)

    def search(self, query):
        """
        Boolean search; this will return documents that contain all words from the
        query, but not rank them (sets are fast, but unordered).
        """
        analyzed_query = analyze(query)
        hits = [self.index.get(token, set()) for token in analyzed_query]
        articles = [self.articles[article_id] for article_id in set.intersection(*hits)]
        print(articles)
        return articles

    def save(self):
        pass

    def load(self):
        pass

    def is_built(self):
        return os.path.exists(self.path_to_file)