import pandas as pd
table_df=pd.read_csv("etl_practice_data.csv")
print(f'highest salary: {table_df["salary"].max()}')