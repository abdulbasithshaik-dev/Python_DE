import requests
from dotenv import load_dotenv
import os
import pandas as pd
load_dotenv()
tenant_id=os.getenv("TENANT_ID")
client_id=os.getenv("CLIENT_ID")
client_secret=os.getenv("CLIENT_SECRET")
grant_type= os.getenv("GRANT_TYPE")
scope=os.getenv("SCOPE")
url=f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
graph_api="https://graph.microsoft.com/v1.0/users"
payload={"client_id":client_id,
        "client_secret":client_secret,
        "grant_type":"client_credentials",
        "scope":scope}

def call_entra(url):
    data=requests.post(url,data=payload)
    token=data.json()
    access_token=token.get("access_token")
    if not access_token:
        raise Exception (f"Token error: {token}")
    return access_token

def call_graph_api():
    access_token=call_entra(url)
    header={
    "Authorization":f"Bearer {access_token}"}
    try:
        data=requests.get(graph_api,headers=header)
        if data.status_code==200:
            print(f"Sucess:{data.json()}")
        else:
            print(F"Api Error:{data.status_code}")
    except Exception as e:
        print("Something failed:", str(e))
    return data.json()

def create_csv():
    api_data=call_graph_api()
    df=pd.DataFrame(api_data)
    df.to_csv("graph_excel.csv",index=False)
    print("csv created")


create_csv()

