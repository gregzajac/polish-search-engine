import json
import os

from search.analysis import analyze
from search.article import Article


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

    def index_articles(self, articles):
        for i, article in enumerate(articles):
            self.index_article(article)

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
        indexes_to_save = {}
        for key, value in self.index.items():
            indexes_to_save[key] = list(value)
        articles_to_save = {}
        for key, value in self.articles.items():
            articles_to_save[key] = value.to_dict()

        data = json.dumps({"index": indexes_to_save, "articles": articles_to_save})
        with open(self.path_to_file, "w") as f:
            f.write(data)

    def load(self):
        try:
            with open(self.path_to_file, "r") as f:
                data = json.loads(f.read())
        except os.error:
            print(f"File '{self.path_to_file}' not found")
        for key, value in data["index"].items():
            self.index[key] = set(value)
        for key, value in data["articles"].items():
            self.articles[key] = Article(**value)

        print("index:", self.index)
        print("articles:", self.articles)

    def is_saved(self):
        return os.path.exists(self.path_to_file)
