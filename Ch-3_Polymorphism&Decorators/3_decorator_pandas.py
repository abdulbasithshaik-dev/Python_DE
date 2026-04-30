import pandas as pd
def pandas_decorator(fx):
    def mainfunc(*args):
        response=fx(*args)

        #do some pandas operations here

        response.to_parquet("data.parquet")
        return response
    
    return mainfunc

@pandas_decorator
def csv_to_parquet(file_path:str):
    df=pd.read_csv(file_path)
    return df


response=csv_to_parquet("Ch-1_OOP/Files/orders.csv")
print(response.head())