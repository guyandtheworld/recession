#app.py
from flask import Flask, request
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # turn json format into pandas dataframe
        df = pd.DataFrame.from_records(request.json)

        # make predictions and create a df out of them
        pred = house_price_model.predict(df)
        pred = pd.DataFrame(pred, columns=['Price'])

        # combine with original data to return it all together
        pred = pd.concat([df, pred], axis=1)

        return(str(pred.to_dict()))

@app.before_first_request
def load_model():
    global house_price_model
    with open('model/house_price_model', 'rb') as handle:
        house_price_model = (pickle.load(handle))
