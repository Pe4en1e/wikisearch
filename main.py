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



@app.get('/path/{page}')
def path(page):
    return wikiworker.getSummary(page)


@app.get('/query')
def query(page: str):
    return f'Looking for {page}'


class postAnswer(BaseModel):
    title: str
    description: str


class postRequest(BaseModel):
    title: str


@app.post('/post', response_model=postAnswer)
def request(input: postRequest):
    return postAnswer(title=input.title, description=f'description for {input.title}')

