from fastapi import HTTPException, Depends, Header
from fastapi.security import OAuth2PasswordRequestForm
from services.NewsService import NewsService
from services.UserService import UserService
from DTOs.News import News
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from DTOs.CustomResponseMessage import CustomResponseMessage
from fastapi.security import OAuth2PasswordBearer

news_controller_router = InferringRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

@cbv(news_controller_router)
class NewsController:
    def __init__(self):
        self.newsService = NewsService()
        self.userService = UserService()

    @news_controller_router.post("/save_article")
    def save_article(self, news: News, user: str, token: str = Depends(oauth2_scheme)):
        self.userService.authenticate(token)
        self.newsService.save_article(news, user)
    
    @news_controller_router.get("/get_saved_articles")
    def get_saved_articles(self, user: str, token: str = Depends(oauth2_scheme)):
        self.userService.authenticate(token)
        return self.newsService.get_saved_articles(user)
    
    @news_controller_router.post("/remove_article")
    def remove_article(self, news: News, user: str, token: str = Depends(oauth2_scheme)):
        self.userService.authenticate(token)
        return self.newsService.remove_article(news, user)
