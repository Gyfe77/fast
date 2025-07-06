from fastapi import FastAPI
import uvicorn
import requests
import json

from model import UserInput, CatsInput


app = FastAPI()


@app.get("/", tags=['Привет'])
def root():
    return 'Hello world!!'


@app.get("/square/{number}", tags=['Квадрат числа'])
def square(number: int):
    return {"number": number, "square": number ** 2}


@app.post("/process", tags=['Человек'])
def process_user(input_data: UserInput):
    return {
        "message": f"Привет, {input_data.name}!",
        "age_in_5_years": input_data.age + 5,
        "status": "success"}


@app.get("/cats", tags=['Кошки'])
def process_user():
    response = requests.get(f"https://catfact.ninja/fact")
    res = json.loads(response.content)
    return {"Факт": res.get('fact'), "Длинна": res.get('length')}


if __name__ == '__main__':
    uvicorn.run("main:app")
