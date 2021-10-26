from collections import Counter
from dataclasses import dataclass

from search.analysis import analyze


@dataclass
class Article:
    """Article representation"""
    id: int
    title: str
    content: str
    url: str
    order: int
    category: str

    @property
    def fulltext(self):
        return ' '.join([self.title, self.content])

    def analyze(self):
        self.term_frequencies = Counter(analyze(self.fulltext))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "url": self.url,
            "order": self.order,
            "category": self.category,
        }

    def from_dict(self, article_dict):
        pass
