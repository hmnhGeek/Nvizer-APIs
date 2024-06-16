from repositories.UserRepository import UserRepository
from DTOs.User import User
from DTOs.News import News
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from repositories.NewsRepository import NewsRepository

class NewsService:
    def __init__(self) -> None:
        self.newsRepository = NewsRepository()

    def save_article(self, news: News, user: str):
        self.newsRepository.save_article(news, user)

    def get_saved_articles(self, user):
        return self.newsRepository.get_all_articles_by_user(user)

    def remove_article(self, news, user):
        return self.newsRepository.remove_article(news, user)