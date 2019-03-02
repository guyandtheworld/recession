import pickle
import pandas as pd
import json

from flask import Flask, render_template


app = Flask(__name__)


"""
- [ ] Forecasting once a day and saving data (Automating?)
- [ ] Auto data scraping and updation
- [ ] Auto train model everyday
- [ ] Deploy to Docker and AWS?
- [ ] Recession date calculation
- [ ] Setup D3 in Node server
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
    yield_curve = pd.read_csv('model/diff_df.csv').set_index('DATE')
    with open('model/yield_curve_model', 'rb') as handle:
        model = (pickle.load(handle))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
