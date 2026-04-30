#normal synchronous function
'''import time
def api_call():
    time.sleep(3)
    return "data fetched from api"

def execute():
    print("executing api call")
    data=api_call()
    print(data)

execute()'''


import asyncio

#corotuine function
async def api_call():
    await asyncio.sleep(3)
    return "data fetched from api"

async def execute():
    print("executing api call")
    data=await api_call()
    print(data)

asyncio.run(execute())

