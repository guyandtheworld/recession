import pandas as pd
from model.fetch_bonds import FetchBonds


def load_df(last_observation_date, three_year_yield, five_year_yield):
    df = pd.read_csv("data/diff_df.csv")

    if df.iloc[-1]['DATE'] != last_observation_date:
        """
        We currently aren't supporting missing more than last date
        Also, I'm not doing premature optimization.
        """
        # Add a new row to the end of the dataframe with the difference
        # in interest rates.
        interest = float(five_year_yield[0]['value']) - \
            float(three_year_yield[0]['value'])
        df = df.append({'DATE': last_observation_date,
                        'DIFF': interest}, ignore_index=True)
    df.to_csv("data/diff_df.csv")


def update_bond_data():
    fb = FetchBonds()

    fb.set_bond('3_year_yield')
    date_3 = fb.get_bond_details()
    three_year_yield = fb.get_observation()

    fb = FetchBonds()

    fb.set_bond('5_year_yield')
    date_5 = fb.get_bond_details()
    five_year_yield = fb.get_observation()

    load_df(date_3, three_year_yield, five_year_yield)


update_bond_data()
