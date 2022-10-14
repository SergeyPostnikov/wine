from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
from storage import get_records


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



years = datetime.now().year - 1920
rendered_page = template.render(
    winery_age=years, 
    noun=get_noun(years),
    records=get_records() 
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 5000), SimpleHTTPRequestHandler)
server.serve_forever()