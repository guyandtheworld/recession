import requests
import sys


class FetchBonds:

    URL = "https://api.stlouisfed.org/fred/series?series_id={}&api_key={}&file_type=json"
    API_KEY = "40eb8f5691964bb12d7401930acc00d5"
    BONDS = {
        '3_year_yield': 'DGS3',
        '5_year_yield': 'DGS5',
    }

    def __init__(self, bond_type):
        self.bond_type = bond_type
        self.URL = self.URL.format(self.BONDS[self.bond_type], self.API_KEY)

    def get_bond(self):
        try:
            response = requests.get(self.URL)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        print(response._content)


f = FetchBonds('5_year_yield')
f.get_bond()
