from bs4 import BeautifulSoup
import requests

from generate_output.create_database import dump_db


def create_database(url='https://en.wikipedia.org/wiki/Python_(programming_language)'):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    final_string = ''
    response = dump_db(data=soup, input_string=final_string)
    print(response)


if __name__ == '__main__':
    create_database()
