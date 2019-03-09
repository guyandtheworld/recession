import pandas as pd

from fbprophet import Prophet
from model.fetch_bonds import FetchBonds


def load_df(last_observation_date, three_year_yield, five_year_yield):
    df = pd.read_csv("data/diff_df.csv")

    print("Updating observations from: {}".format(df.iloc[-1]['DATE']))

    if df.iloc[-1]['DATE'] != last_observation_date:
        """
        We currently aren't supporting missing more than last date
        Also, I'm not doing premature optimization.
        """
        # Add a new row to the end of the dataframe with the difference
        # in interest rates.
        for observation in range(1, len(three_year_yield)):
            five_year = five_year_yield[observation]['value']
            three_year = three_year_yield[observation]['value']
            obv_date = three_year_yield[observation]['date']

            interest = float(five_year) - float(three_year)

            df = df.append({'DATE': obv_date,
                            'DIFF': interest}, ignore_index=True)
            print("Updated for {}".format(obv_date))

    df.to_csv("data/diff_df.csv", index=False)


def update_bond_data():
    df = pd.read_csv("data/diff_df.csv")
    last_date = df.iloc[-1]['DATE']

    fb = FetchBonds()

    fb.set_bond('3_year_yield')
    date_3 = fb.get_bond_details()
    three_year_yield = fb.get_observation(last_date)

    fb = FetchBonds()

    fb.set_bond('5_year_yield')
    date_5 = fb.get_bond_details()
    five_year_yield = fb.get_observation(last_date)
    load_df(date_3, three_year_yield, five_year_yield)


def train_prophet():
    # Load and train prophet with the data
    df_prophet = pd.read_csv("data/diff_df.csv")
    df_prophet.columns = ['ds', 'y']

    last_date = df_prophet.iloc[[-1]].ds.values[0]

    print("Predicting for data...")
    model = Prophet(changepoint_prior_scale=1, changepoint_range=1)
    model.fit(df_prophet)

    print("Finished predicting...")
    future = model.make_future_dataframe(periods=1260, freq='D')
    forecast = model.predict(future)

    forecast_data = forecast[['ds', 'yhat_upper']]
    forecast_data['ds'] = pd.to_datetime(forecast_data['ds'])

    forecast_data = forecast_data[forecast_data['ds'] > last_date]
    forecast_data.to_csv('data/forecast.csv', index=False)
    print("Finished forecasting...")
