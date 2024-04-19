import uvicorn
from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from utils.create_database import dump_db
from generate_output.preprocess import find_paragraphs
from generate_output.responder import respond
from custom_logger import get_logger

logger = get_logger('main')
app = FastAPI()


class PageUrl(BaseModel):
    """Model representing the input URL for creating a database."""
    url: str


class UserQuery(BaseModel):
    """Model representing the user's query."""
    query: str


@app.get("/")
async def index():
    """Endpoint to check if the server is up."""
    return 'Server spin up successful!'


@app.post("/createdb")
async def create_database(page_url: PageUrl):
    """
    Endpoint to create a database from the provided URL.

    Args:
        page_url (PageUrl): The URL of the page from which to create the database.

    Returns:
        str: Success message or error message.
    """
    page = requests.get(page_url.url)
    soup = BeautifulSoup(page.content, 'html.parser')
    paragraphs = find_paragraphs(raw_data=soup)
    input_string = ''
    for paragraph in paragraphs:
        input_string += paragraph.text
    try:
        response = dump_db(data=input_string)
        return response
    except Exception as e:
        logger.info(e)
        return 'I am unable to do that right now...'


@app.post("/ask")
async def ask_question(user_query: UserQuery):
    """
    Endpoint to ask a question based on the user's query.

    Args:
        user_query (UserQuery): The user's query.

    Returns:
        str: Response to the user's query or error message.
    """
    user_query = user_query.query
    try:
        response = respond(user_query)
        return response
    except Exception as e:
        logger.info(e)
        return 'I am unable to do that right now...'


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
