import uvicorn
from bs4 import BeautifulSoup

import requests
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from utils.create_database import dump_db
from generate_output.preprocess import find_paragraphs
from generate_output.responder import respond

app = FastAPI()


class PageUrl(BaseModel):
    url: str


class UserQuery(BaseModel):
    query: str


@app.get("/")
async def index():
    return 'Server spin up successful!'


@app.post("/createdb")
async def create_database(page_url: PageUrl):
    page = requests.get(page_url.url)
    soup = BeautifulSoup(page.content, 'html.parser')
    paragraphs = find_paragraphs(raw_data=soup)
    input_string = ''
    for paragraph in paragraphs:
        input_string += paragraph.text
    response = dump_db(data=input_string)
    return response


@app.post("/ask")
async def ask_question(user_query: UserQuery):
    user_query = user_query.query
    response = respond(user_query)
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
