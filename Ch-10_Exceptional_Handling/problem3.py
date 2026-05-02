import boto3
import requests
from pydantic import BaseModel, ValidationError
from dotenv import load_dotenv
import os
load_dotenv()


class UserModel(BaseModel):
    id:int
    email:str
    first_name:str

def api_calling(url,headers):
    try:
        response=requests.get(url,headers=headers)
        data=response.json()
        real_data=data.get("data")
    except requests.exceptions.InvalidURL as errror:
        print(errror)
    except requests.exceptions.InvalidSchema as error:
        print(error)
    return real_data

sure=api_calling("https://reqres.in/api/users",headers={"x-api-key":f"{os.getenv("DUMMY_API")}"})

for record in sure:
    print(record)


