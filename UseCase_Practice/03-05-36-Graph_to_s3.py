import pandas as pd
import os
import requests
from dotenv import load_dotenv
import boto3
from pydantic import BaseModel,EmailStr,ConfigDict
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()

tenant_id=os.getenv("TENANT_ID")
client_id=os.getenv("CLIENT_ID")
client_secret=os.getenv("CLIENT_SECRET")
grant_type=os.getenv("GRANT_TYPE")
scope=os.getenv("SCOPE")
graph_api="https://graph.microsoft.com/v1.0/users"

url=f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
data={"client_id":client_id,
      "client_secret":client_secret,
      "grant_type":grant_type,
      "scope":scope}
filepath_valid="Valid_users.csv"
filepath_Invalid="InValid_users.csv"
bucket_name="shaikfirstbucket245"

def get_token():
    response=requests.post(url,data)
    token=response.json()
    access_token=token.get("access_token")
    if not access_token:
        raise Exception  (f"Token error: {token}")
    else:
        return access_token 


def fetch_users(token):
    header={"Authorization":f"Bearer {token}"}
    response=requests.get(graph_api,headers=header)
    get_response=response.json()
    value=get_response.get("value")
    return value

class UserSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")
    displayName:str
    givenName:str
    

    
def validate_users(users):
    valid = []
    invalid = []

    for user in users:
        try:
            obj = UserSchema(**user)
            valid.append(user)
        except Exception as e:
            invalid.append({"data": user, "error": str(e)})

    return valid, invalid

def write_to_csv(valid,invalid):
    df=pd.DataFrame(valid)
    df.to_csv("Valid_users.csv",index=False)
    logging.info("Successfully saved Valid.csv")
    df1=pd.DataFrame(invalid)
    df1.to_csv("Invalid_users.csv",index=False)
    logging.info("Successfully saved InValid.csv")


def upload_to_s3():
    s3_client=boto3.client("s3",
                           region_name=os.getenv("REGION"),
                           aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
                           aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
    logging.info("Connected to s3")
    
    try:
       
        s3_client.upload_file(
            filepath_valid,
            bucket_name,
            "Valid_users.csv"
        )
        logging.info("Uploaded Valid_users.csv to S3")

       
        s3_client.upload_file(
            filepath_Invalid,
            bucket_name,
            "Invalid_users.csv"
        )
        logging.info("Uploaded Invalid_users.csv to S3")

    except Exception as e:
        logging.error(f"S3 upload failed: {e}")
        raise

   


def main():
    logging.info("STEP 1: Token generation started")
    token = get_token()
    logging.info("STEP 2: Fetching users")
    users = fetch_users(token)
    logging.info("STEP 3: Validating users")
    valid, invalid = validate_users(users)
    logging.info("STEP 4: Writing CSV")
    csv=write_to_csv(valid,invalid)
    logging.info("STEP 5: Uploading to S3")
    s3=upload_to_s3()

main()
