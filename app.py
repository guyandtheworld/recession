import pandas as pd
import json
import datetime

from flask import Flask, render_template

# from utils import update_bond_data

app = Flask(__name__)


"""
- [x] Updating data
- [x] Forecasting once a day saving, serving
- [x] Fix shitty graph
- [x] Automate process daily
# - [ ] Setup D3 in Node server
- [ ] Deploy to Docker and AWS
- [ ] Auto data scraping
- [ ] Auto train model everyday
- [ ] Fix the graph!
- [ ] Recession date calculation
- [ ] Decorate
- [ ] Deploy
- [ ] Add support for customizable yield dates
"""


def check_changes(yield_curve, forecast):
    """
    Check if the dataframe has any changes, if it does
    update the global variables. This function would be
    invoked at the certain time of day.
    """
    df = pd.read_csv('data/diff_df.csv').set_index('DATE')
    if list(df.index)[-1] != list(yield_curve.index)[-1]:
        forecast = pd.read_csv('data/forecast.csv')
        yield_curve = df


@app.route("/forecast", methods=['GET'])
def forecast_curve():
    data = []

    # Take only the forecasted data

    for row in forecast.iterrows():
        data.append({"date": str(row[1]['ds']), "value": row[1]['yhat_upper']})
    return json.dumps(data)


@app.route("/data", methods=['GET'])
def data():

    # now = datetime.datetime.now()
    # print(now)

    # yield_curve, forecast = check_changes(yield_curve, forecast)

    return yield_curve.to_json(orient='index')


@app.route("/")
def index():
    return render_template("index.html")


@app.before_first_request
def load_model():
    global yield_curve, forecast
    forecast = pd.read_csv('data/forecast.csv')
    yield_curve = pd.read_csv('data/diff_df.csv').set_index('DATE')
