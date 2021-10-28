import numpy as np
from requests_html import HTMLSession

class CSGOFastParser():

    def __init__(self, url="http://csgofastx.com"):
        self.url = url
        self.history_url = url + "/history/double/all"
        self.current_game_url = url + "/game/double"
        self.current_game_session = HTMLSession()

    def _get_rendered_page(self):
        pass

    def parse_history(self):
        resp = None
        while (resp is None):
            try:
                history_session = HTMLSession()
                resp = history_session.get(self.history_url)
                resp.html.render()
            except BaseException:
                pass

        resp = resp.html.find('.history-wrap', first=True)
        history = resp.text
        history = history.split("Game #")
        rounds = []
        for record in history:
            rounds.append(record.split('\n')[:6])
        return rounds[1:]

    def parse_current_game(self):
        resp = None
        while (resp is None):
            try:
                resp = self.current_game_session.get(self.current_game_url)
                resp.html.render()
            except BaseException:
                pass

        results = resp.html.find('.game-bets-header')
        red_bet = results[0].text
        green_bet = results[1].text
        black_bet = results[2].text
        time_till_raffle = resp.html.find('.bonus-game-timer')[0].text
        game_id = resp.html.find('.game-num')[0].text



        return (time_till_raffle, game_id, red_bet, green_bet, black_bet)

