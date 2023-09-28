from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def deafult():
    return "Hello!"



@app.get('/path/{item}')
def itemGet(item):
    return 'Item is ' + item


@app.get('/querry')
def params(a: int, b: int):
    return f'a is {a}\nb is {b}'


