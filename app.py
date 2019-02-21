import pickle
import pandas as pd

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/forecast", methods=['GET'])
def forecast_curve():
    future = model.make_future_dataframe(periods=1260, freq='D')
    forecast = model.predict(future)

#     forecast_data = forecast[['ds', 'yhat',
#                               'yhat_lower', 'yhat_upper']].set_index('ds')

    forecast_data = forecast[['ds', 'yhat_upper']].set_index('ds')
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
