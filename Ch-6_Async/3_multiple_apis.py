import asyncio

#coroutine function
async def api_call(url:str,delay:float):
    print(f"fetching data from {url}")
    await asyncio.sleep(delay)
    print (f"data fetched from {url}")
    return f"data fetched from api from {url}"

async def main():
    
    #creating tasks with gather
    tasks=await asyncio.gather(
        api_call("https://reqres.in/api/users",1),
        api_call("https://reqres.in/api/posts",3),
        api_call("https://reqres.in/api/comments",2)
    )
    
    #another way to create tasks with create_task
    #tasks=[api_call("https://reqres.in/api/users"),api_call("https://reqres.in/api/posts"),api_call("https://reqres.in/api/comments")]
    #results=await asyncio.gather(*tasks)

    print("all api calls executed")

asyncio.run(main())
