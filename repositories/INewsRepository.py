from abc import abstractmethod

class INewsRepository:
    @abstractmethod
    def save_article(self, news, user): pass

    @abstractmethod
    def get_all_articles_by_user(self, user): pass

    @abstractmethod
    def remove_article(self, news, user): pass
