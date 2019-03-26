# When's The Next Recession?

## :no_entry: Short the Bonds, Sell the Stocks cause a recession is on it's way baby. :no_entry:

In the Treasury market, shorter-term interest rates this week started to move above some longer-term rates.

That can be an early warning sign of a recession, as it was in 1990, 2001 and 2007, according to a study by Bespoke. The firm said that kind of bond market move may indicate that some of the more widely watched spreads could also soon flip, or invert, a precursor to a recession.

The 3-year Treasury yield Monday moved above the 5-year yield, and it was soon followed by the 2-year. The market most closely watches the spread between the 2-year and 10-year, as well as 3-month to 10-year spread, which is the one preferred by the Fed.

[Read More About This Here](https://www.cnbc.com/2018/12/04/the-yield-curve-explained-and-how-it-became--wall-streets-barometer.html)

## So what does this project do.

![](https://media.giphy.com/media/8c6YTRuQE9ejh2aXIy/giphy.gif)

Basically we have a small web app here where we fetch the interest rates daily from the stlouisfed API for the 3 Year and 5 Year bonds. We then calculate the difference in the interest dates and forecast it using a D3.js

#### It's very much near to impossible to actually predict a recession so basically this is just for speculation. 

We use the Facebook's Prophet library to do a simple time series forecasting on this data by extrapolating the curve to speculate when the next recession would happen based on the Yield Curve.


## Technology

We use a small flask web app in the backend to keep the system together. We have a couple of python scripts to run everyday to fetch the daily interest data and to do the forecasting.

The forecasting is done using [Facebook's Prophet](https://github.com/facebook/prophet). Which is really amazing in figuring out the patterns in the yield curves to give us the most likely outcome.

## How to Set Up the Project.

```

pip install -r requirements.txt

export FLASK_APP=app.py

export FLASK_ENV=development

flask run

```

## To Do's

- [x] Updating data async
- [x] Forecasting once a day saving, serving
- [x] Fix graph
- [x] Automate process daily
- [x] Auto data scraping
- [ ] Setup D3 in Node server
- [ ] Deploy to Docker and AWS
- [ ] Auto train model everyday
- [ ] Recession date calculation
- [ ] Add superior UX/UI
- [ ] Deploy on AWS
- [ ] Add support for multiple bonds
