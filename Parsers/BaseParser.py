from abc import ABC


import numpy as np
from requests_html import HTMLSession

class BaseParser(ABC):

    def __init__(self, url):
        self.url = url
        self.history_url = url + "/history/double/all"

    def parse(self):
        session = HTMLSession()
        resp = session.get(self.history_url)
        resp.html.render()

        raw_text = resp.html.text

        return raw_text



url = "http://csgofastx.com"
parser = BaseParser(url)
history = parser.parse()
history = history.split("Game #")
history = history [1:]
records = []
for record in history:
    records.append(record.split('\n'))

print(records)