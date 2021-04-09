from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from app import ml

app = FastAPI()


# defines and validates the
# request body format
class Article(BaseModel):
    content: str
    comments: List[str] = []


@app.get('/')
def simple_get():
    return {'message': 'Hello World!'}


@app.get('/article_id/{article_id}')
def read_main(article_id: int, q: str = None):
    return {'atricle_id': article_id, 'query_param': q}


@app.post('/article/')
def analyse_article(articles: List[Article]):
    ents = []
    for article in articles:
        doc = ml.nlp(article.content)
        for ent in doc.ents:
            ents.append({'text': ent.text, 'label': ent.label_})
    return {'ents': ents}
