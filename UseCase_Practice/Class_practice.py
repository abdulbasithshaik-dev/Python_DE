import pandas as pd
import boto3
import requests
from dotenv import load_dotenv
import os

load_dotenv()

url="https://reqres.in/api/users?page=1"
headers={"x-api-key":f"{os.getenv("DUMMY_API")}"}

def api_calling(url):
    response=requests.get(url,headers=headers)
    json_response=response.json()
    raw_data=json_response["data"]
    return raw_data

def validate_data(raw_data):
    valid_rows=[]
    invalid_rows=[]
    for record in raw_data:
        if record.get("first_name") and record.get("email"):
            valid_rows.append(record)
        else:
            invalid_rows.append(record)
    return valid_rows,invalid_rows


def create_csv(valid_rows):
    df=pd.DataFrame(valid_rows)
    df.to_csv("shaik.csv",index=True)
    print("CSV created!")


def upload_to_s3(file_path,bucket_name):
    s3_client=boto3.client("s3",
                           region_name='ap-south-1',
                           aws_access_key_id=os.environ["aws_access_key"],
                           aws_secret_access_key=os.environ["aws_secret_access_key"])
    print("connected successfully")
    upload=s3_client.upload_file(file_path, bucket_name, os.environ["aws_secret_access_key"])
    print("uploaded successfully to s3")

# execution
raw_data = api_calling(url)
valid_rows, invalid_rows = validate_data(raw_data)
create_csv(valid_rows)
upload_to_s3("shaik.csv","shaikfirstbucket245")



