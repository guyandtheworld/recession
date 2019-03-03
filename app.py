import pickle
import pandas as pd
import json

from flask import Flask, render_template

# from utils import update_bond_data

app = Flask(__name__)


"""
- [x] Updating data
- [ ] Automate process daily
- [ ] Forecasting once a day saving, serving
- [ ] Setup D3 in Node server
- [ ] Deploy to Docker and AWS
- [ ] Auto data scraping and     
- [ ] Auto train model everyday
- [ ] Recession date calculation
- [ ] Decorate
- [ ] Deploy
- [ ] Add support for customizable yield dates
"""


@app.route("/forecast", methods=['GET'])
def forecast_curve():
    future = model.make_future_dataframe(periods=1260, freq='D')
    forecast = model.predict(future)

    data = []

    forecast_data = forecast[['ds', 'yhat_upper']]
    forecast_data['ds'] = pd.to_datetime(forecast_data['ds'])

    forecast_data = forecast_data[forecast_data['ds'] > '2019-02-08']

    # Take only the forecasted data
    for row in forecast_data.iterrows():
        data.append({"date": str(row[1]['ds']), "value": row[1]['yhat_upper']})

    return json.dumps(data)


@app.route("/data", methods=['GET'])
def data():
    return yield_curve.to_json(orient='index')


@app.route("/")
def index():
    return render_template("index.html")


@app.before_first_request
def load_model():
    global model, yield_curve
    yield_curve = pd.read_csv('data/diff_df.csv').set_index('DATE')
    with open('model/yield_curve_model', 'rb') as handle:
        model = (pickle.load(handle))
