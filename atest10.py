import asyncio
import time
import random

async def newsProducer(myqueue):
     while True:
       await asyncio.sleep(1)
       print("Putting new item onto queue")
       await myqueue.put(random.randint(1,5))

async def newConsumer(id,myqueue):
   while True:
       print(f"Consumer:{id} attempting to get from queue")
       item=await myqueue.get()
       if item is None:
          break
       print(f"Consumer {id} consumed with id")

async def main(loop):
   myqueue=asyncio.Queue(loop=loop,maxsize=10)
   await asyncio.wait([newsProducer(myqueue),newsConsumer(lock)])

loop=asyncio.get_event_loop()
loop.run_until_complete(main(loop))
print("All workers completed")
loop.close()


       