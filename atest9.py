import asyncio
import time

async def myworker(lock):
   print("Attempting to attain lock")
   with await lock:
      print("Currently locked")
      time.sleep(2)
   print("Unlocked from critical section")


async def main():
  lock=asyncio.Lock()
  await asyncio.wait([myworker(lock),myworker(lock)])


loop=asyncio.get_event_loop()
loop.run_until_complete(main())
print("All workers completed")
loop.close()
