import schedule
import time

from utils import update_bond_data, train_prophet


def job():
    """
    Update data and forecast it.
    """
    update_bond_data()
    train_prophet()


schedule.every().day.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
