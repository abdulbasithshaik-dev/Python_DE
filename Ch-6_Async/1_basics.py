import asyncio
import time

#coroutine function
async def main():
    print("hello") #prints immediately
    await asyncio.sleep(3) #thread is idle
    print("world")  #this will be executed right after the thread is idle

asyncio.run(main())