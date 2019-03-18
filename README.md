# When's The Next Recession?

In the Treasury market, shorter-term interest rates this week started to move above some longer-term rates.

That can be an early warning sign of a recession, as it was in 1990, 2001 and 2007, according to a study by Bespoke. The firm said that kind of bond market move may indicate that some of the more widely watched spreads could also soon flip, or invert, a precursor to a recession.

The 3-year Treasury yield Monday moved above the 5-year yield, and it was soon followed by the 2-year. The market most closely watches the spread between the 2-year and 10-year, as well as 3-month to 10-year spread, which is the one preferred by the Fed.

## What can we do about it.

![](https://media.giphy.com/media/8c6YTRuQE9ejh2aXIy/giphy.gif)

In this small web app, we'll set up a system to automatically scrap the Interest rates from the bonds and forecast the yield curve using a flask app.

## Technology

## How to Set Up

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