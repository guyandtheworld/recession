import schedule
import time

from utils import update_bond_data, train_prophet


def job():
    update_bond_data()
    train_prophet()


schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
