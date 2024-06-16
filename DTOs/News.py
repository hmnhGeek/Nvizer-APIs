from pydantic import BaseModel
from typing import List

# {
#     "title": "Kate attends Trooping the Colour, pictured in carriage with her children: LIVE",
#     "description": "Kate Middleton will be attending King’s Birthday Parade at Trooping the Colour ceremony today.",
#     "content": "June 15, 2024 12:16 PM IST\nI have been blown away by all the kind messages of support and encouragement over the last couple of months. It really has made the world of difference to William and me and has helped us both through some of the harder tim... [1033 chars]",
#     "url": "https://www.hindustantimes.com/world-news/kate-middletons-first-public-appearance-post-cancer-diagnosis-at-kings-birthday-parade-live-updates-101718429809909.html",
#     "image": "https://www.hindustantimes.com/ht-img/img/2024/06/15/550x309/BRITAIN-ROYALS-KING-BIRTHDAY-20_1718446180900_1718446193555.JPG",
#     "publishedAt": "2024-06-15T10:14:26Z",
#     "source": {
#         "name": "Hindustan Times",
#         "url": "https://www.hindustantimes.com"
#     }
# }

class NewsSource(BaseModel):
    name: str
    url: str

class News(BaseModel):
    title: str
    description: str
    content: str
    url: str
    image: str
    publishedAt: str
    source: NewsSource

class SavedArticle(BaseModel):
    article: News
    savedBy: List[str]