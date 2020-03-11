import asyncio
import random

task=[]

async def task1():
     print("Task1 Executed")
     await asyncio.sleep(random.randint(1,3))
     print("Task1 completed")

async def task2():
     print("Task2 Executed")
     await asyncio.sleep(random.randint(1,3))
     print("Task2 completed")

async def task3():
     print("Task3 Executed")
     await asyncio.sleep(random.randint(1,3))
     print("Task3 Completed")

def add_task(task_def):
    global task
    task.append(task_def())

async def gather_task():
   await asyncio.gather(*task)


if __name__=="__main__":
   add_task(task1())
   add_task(task2())
   add_task(task3())
   loop=asyncio.get_event_loop()
   loop.run_until_complete(gather_task())
   loop.close()

   

