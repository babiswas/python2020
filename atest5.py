import asyncio
import random

async def mycoroutine(id):
   ptime=random.randint(1,3)
   await asyncio.sleep(ptime)
   print(f"Coroutine {id} has sucessfully completed afetr {ptime} time")


async def main():
   tasks=[]
   for i in range(10):
     tasks.append(asyncio.ensure_future(mycoroutine(i)))
   await asyncio.gather(*tasks)

if __name__=="__main__":
   loop=asyncio.get_event_loop()
   loop.run_until_complete(main())
   loop.close()


