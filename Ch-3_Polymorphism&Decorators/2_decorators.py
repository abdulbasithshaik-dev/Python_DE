def my_decorator(fx):
    def mainfunc(*args):
        print("befoire calling the function")
        response=fx(*args)
        print("after calling the function")
        return response
    return mainfunc






@my_decorator
def fetch_datas(url:str,path:str):
    return  f"fetching data from {url} and saving to {path}"

response=fetch_datas("https://reqres.in/api/users","/home/user/data.json")
print(response)

