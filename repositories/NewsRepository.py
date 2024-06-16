from repositories.INewsRepository import INewsRepository
from entity_manager.entity_manager import entity_manager
import os, datetime
from dotenv import load_dotenv
from DTOs.News import News, SavedArticle
from typing import List
from pymongo import DESCENDING
from DTOs.CustomResponseMessage import CustomResponseMessage
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=dotenv_path)

# Convert MongoDB document to JSON serializable format
def convert_to_json_serializable(doc):
    if '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc

class NewsRepository(INewsRepository):
    def __init__(self):
        self.em = entity_manager.get_collection(os.environ.get("SAVED_ARTICLES_COLLECTION"))

    def save_article(self, news : News, user : str):
        document = self.em.find_one({"article.url": news.url})
        if document is not None:
            current_users = document["savedBy"]
            if user not in current_users:
                current_users.append(user)

            self.em.update_one({"_id": document["_id"]}, {
                "$set": {
                    "article": news.model_dump(),
                    "savedBy": current_users
                }
            })
        else:
            document = SavedArticle(article=news, savedBy=[user])
            self.em.insert_one(document.model_dump())
        
        return CustomResponseMessage(status_code=200, message = "The article has been saved.")

    def get_all_articles_by_user(self, user): 
        query = {"savedBy": {"$in": [user]}}
        matching_documents = self.em.find(query)
        # return list(document) if document is not None else None
        articles = [convert_to_json_serializable(doc) for doc in matching_documents]
        return JSONResponse(content=jsonable_encoder(articles))

    def remove_article(self, news, user): 
        document = self.em.find_one({"article.url": news.url})
        if document is not None:
            current_users = document["savedBy"]
            if user in current_users:
                current_users.remove(user)
            
            print("current", current_users)
            if current_users == []:
                self.em.delete_one({"_id": document["_id"]})
            else:
                self.em.update_one({"_id": document["_id"]}, {
                    "$set": {
                        "article": news.model_dump(),
                        "savedBy": current_users
                    }
                })
        return self.get_all_articles_by_user(user); 