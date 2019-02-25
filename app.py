import pickle
import pandas as pd
import datetime


from flask import Flask, render_template


app = Flask(__name__)


"""
- [ ] Return the forecast on a different end-point
- [ ] Append forecast to the D3 Graph
- [ ] Auto data scraping and updation
- [ ] Auto train model everyday
"""


@app.route("/forecast", methods=['GET'])
def forecast_curve():
    future = model.make_future_dataframe(periods=1260, freq='D')
    forecast = model.predict(future)
    # {"date":"1985-01-02T00:00:00.000Z","value":0.61}
    data = []

    forecast_data = forecast[['ds', 'yhat_upper']]
    for row in forecast_data.iterrows():
        data.append({"date": row[1]['ds'], "value": row[1]['yhat_upper']})

    return forecast_data[:1000:7].to_json()


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
