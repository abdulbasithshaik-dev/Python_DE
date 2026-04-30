import asyncio
import time
#first task
async def api_call(url:str,delay:float=3):
    print(f"fetching data from {url}")
    await asyncio.sleep(delay)
    print (f"data fetched from {url}")

#second task

async def execution():
    time.sleep(5)
    print("execution completed")        

#third task

async def transformation():
     asyncio.sleep(4)
     print("transformation completed")

async def main():

    tasks=await asyncio.gather(
        api_call("https://reqres.in/api/users"),
        execution(),
        transformation()
    )
    print(tasks)

asyncio.run(main())