from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
from storage import get_products
import os
from dotenv import load_dotenv
import argparse


def get_noun(years):
    if 11 <= years % 100 <= 19:
        return 'лет'
    elif years % 10 == 1:
        return "год"
    elif 2 <= years % 10 <= 4:
        return "года"
    else:
        return "лет"


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--storage', 
        help='storage location')
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    foundation_year = 1920
    winery_age = datetime.now().year - foundation_year
    filepath = args.storage if args.storage else os.getenv("PATH_TO_STORAGE", default='wine.xlsx')
    rendered_page = template.render(
        winery_age=winery_age, 
        noun=get_noun(winery_age),
        records=get_products(filepath) 
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 5000), SimpleHTTPRequestHandler)
    server.serve_forever()
