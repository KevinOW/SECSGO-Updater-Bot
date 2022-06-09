# Script that will start both esportal.py & twitter-bot.py. It will run every 15 min.

import os
import schedule
import time


def job():
     print("I'm working...")

schedule.every(2).seconds.do(job)

while True:
    os.system("esportal.py && twitter-bot.py")
    schedule.run_pending()
    time.sleep(1)