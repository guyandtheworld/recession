import json
import requests
import sys


class FetchBonds:

    URL = "https://api.stlouisfed.org/fred/series?series_id={}&api_key={}&file_type=json"

    OBSERVATION_URL = "https://api.stlouisfed.org/fred/series/observations?series_id={}&api_key={}&\
        file_type=json&observation_start={}"

    API_KEY = "40eb8f5691964bb12d7401930acc00d5"
    BONDS = {
        '3_year_yield': 'DGS3',
        '5_year_yield': 'DGS5',
    }

    def __init__(self):
        pass

    def set_bond(self, bond_type):
        self.bond_type = bond_type
        self.URL = self.URL.format(self.BONDS[self.bond_type], self.API_KEY)

    def get_bond_details(self):
        try:
            response = requests.get(self.URL)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        content = response._content.decode('utf8').replace("'", '"')
        content = json.loads(content)
        self.date = content['seriess'][0]['observation_end']
        return self.date

    def get_observation(self, last_date):
        self.OBSERVATION_URL = self.OBSERVATION_URL.format(
            self.BONDS[self.bond_type], self.API_KEY, last_date)

        try:
            response = requests.get(self.OBSERVATION_URL)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        content = response._content.decode('utf8').replace("'", '"')
        data = json.loads(content)

        return data['observations']
