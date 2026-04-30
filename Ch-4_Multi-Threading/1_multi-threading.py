import time
from concurrent.futures import ThreadPoolExecutor

def fetch_data(url:str):
    print(f"fetching data from {url}")
    time.sleep(2)
    print(f"data fetched from {url}")
    return f"data from {url}"
    
results=[]
urls=["https://reqres.in/api/users","https://jsonplaceholder.typicode.com/posts","https://jsonplaceholder.typicode.com/comments"]
with ThreadPoolExecutor(max_workers=len(urls)) as executor:
    futures=executor.map(fetch_data,urls)
    results.extend(futures)

print(results)
