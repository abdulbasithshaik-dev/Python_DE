import boto3
import pandas
import os
import requests
from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()

aws_access_key_id=os.getenv("aws_access_key")
aws_secret_access_key=os.getenv("aws_secret_access_key")
region_name=os.getenv("REGION_NAME")

client_id=os.getenv("CLIENT_ID")
client_secret=os.getenv("CLIENT_SECRET")
grant_type=os.getenv("GRANT_TYPE")
scope=os.getenv("SCOPE")
tenant_id=os.getenv("TENANT_ID")
url=f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"


def graph_api_calling():
    data={"client_id":client_id,
          "client_secret":client_secret,
          "scope":scope,
          "grant_type":grant_type
          }
    response=requests.post(url,data)
    token_extract=response.json()
    access_token=token_extract.get("access_token")
    return access_token

graph_api_calling()
