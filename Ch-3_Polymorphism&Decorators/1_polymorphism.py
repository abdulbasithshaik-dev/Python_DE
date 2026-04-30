import requests
import boto3
import os
from dotenv import load_dotenv
load_dotenv()
print(os.environ["aws_access_key_id"])
class api_fetch:

    def fetch(self,url:str,headers:dict):
        self.url=url
        self.headers=headers
        response=requests.get(self.url,headers=self.headers)
        print(response.json())

class db_fetch:

    def fetch(self):
        print("fetching data from database")

class s3_fetch:

    def fetch(self):
        s3_client=boto3.client("s3",
        aws_access_key_id=os.environ["aws_access_key_id"],
        aws_secret_access_key=os.environ["aws_secret_access_key"],
        region_name=os.environ["aws_region"])
        response=s3_client.list_buckets()
        for bucket in response["Buckets"]:
            print(bucket["Name"])
        


obj=api_fetch()
obj.fetch("https://reqres.in/api/users",{"x-api-key":"reqres_22300d4dcdaa4ef6a1f65e992fd838f8"})
obj2=db_fetch()
obj2.fetch()
obj3=s3_fetch()
obj3.fetch()