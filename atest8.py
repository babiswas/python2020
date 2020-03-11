import asyncio


async def test1():
    print("Hello test")
    await asyncio.sleep(2)
    print("Complete")

async def task_gather():
   task=[]
   for i in range(3):
      task.append(test1())
   await asyncio.gather(*task)

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(task_gather()))
loop.close()