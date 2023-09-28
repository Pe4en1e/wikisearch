from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def deafult():
    return "Hello!"



@app.get('/path/{item}')
def itemGet(item):
    return 'Item is ' + item


