import numpy as np
from requests_html import HTMLSession

class CSGOFastParser():

    def __init__(self, url="http://csgofastx.com"):
        self.url = url
        self.history_url = url + "/history/double/all"

    def _get_rendered_page(self):
        pass

    def parse(self):
        session = HTMLSession()
        resp = session.get(self.history_url)
        resp.html.render()
        raw_text = resp.html.text
        history = raw_text
        history = history.split("Game #")
        history = history[1:51]
        rounds = []
        for record in history:
            rounds.append(record.split('\n')[:6])

        return rounds
parser = CSGOFastParser()
rounds = parser.parse()


print(rounds[0])
print(rounds[-1])