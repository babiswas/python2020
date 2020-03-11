import asyncio

async def mycoroutine():
   print("Test the coroutine")

def main():
  loop=asyncio.get_event_loop()
  loop.run_until_complete(mycoroutine())
  loop.close()

if __name__=="__main__":
   main()
