# Импортируем модули

import wikipedia
from fastapi import FastAPI
from pydantic import BaseModel

# Создаем приложение

app = FastAPI()

# path
@app.get('/path/{page}')
def path(page: str):
    return wikipedia.summary(page)

# query
@app.get('/query')
def query(page: str):
    return wikipedia.summary(page)

# Формирование тела ответа
class WikiAnswer(BaseModel):
    title: str
    content: str
    link: str

# Формирование тела запроса
class WikiInput(BaseModel):
    title: str


# Post запрос
@app.post('/post', response_model=WikiAnswer, description='Возвращает название, полное содержание и ссылку на статью')
def request(input: WikiInput):
    wikipage = wikipedia.page(input.title)
    return WikiAnswer(
        title=wikipage.title,
        content=wikipage.content,
        link=wikipage.url
    )