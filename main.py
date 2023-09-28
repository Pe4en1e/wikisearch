# 
# 91.239.148.59
# 

from fastapi import FastAPI
from pydantic import BaseModel

import wikiworker

app = FastAPI()


@app.get('/')
def deafult():
    return "БВТ2304 Дубровин Александр"



@app.get('/path/{page}', description='Возвращает резюме статьи')
def path(page: str):
    return wikiworker.getSummary(page, None)


@app.get('/query', description='Возвращает резюме статьи, можно указать кол-во предложений ')
def query(page: str, sent: int):
    return wikiworker.getSummary(page, sent)


class WikiAnswer(BaseModel):
    title: str
    content: str
    link: str


class WikiInput(BaseModel):
    title: str


@app.post('/post', response_model=WikiAnswer, description='Возвращает название, полное содержание и ссылку на статью')
def request(input: WikiInput):
    wikipage = wikiworker.getPage(input.title)
    return WikiAnswer(
        title=wikiworker.getTitle(wikipage),
        content=wikiworker.getContent(wikipage),
        link=wikiworker.getUrl(wikipage)
    )

