from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime


def get_noun(years):
    if 11 <= years % 100 <= 19:
        return 'лет'
    elif years % 10 == 1:
        return "год"
    elif 2 <= years % 10 <= 4:
        return "года"
    else:
        return "лет"


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


then = datetime(year=1920, month=1, day=1)
years = (datetime.now() - then).days // 365
rendered_page = template.render(
    winery_age=years, 
    noun=get_noun(years)
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 5000), SimpleHTTPRequestHandler)
server.serve_forever()