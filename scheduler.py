import schedule
import time

def job():
   print("I am job")

def job1():
   print("I am job1")

schedule.every(10).seconds.do(job)
schedule.every(5).seconds.do(job1)


while True:
   schedule.run_pending()
   time.sleep(1)

