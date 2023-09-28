# 
# 91.239.148.59
# 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def deafult():
    return "Hello!"



@app.get('/path/{item}')
def itemGet(item):
    return 'Item is ' + item


@app.get('/query')
def params(a: int, b: int):
    return f'a is {a}, b is {b}'


class postAnswer(BaseModel):
    title: str
    description: str


class postRequest(BaseModel):
    title: str


@app.post('/post', response_model=postAnswer)
def request(input: postRequest):
    return postAnswer(title=input.title, description=f'description for {input.title}')

