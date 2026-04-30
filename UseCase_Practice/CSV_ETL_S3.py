import csv
import os

def file_path():
    file_lis=os.listdir()
    for file in file_lis:
        if file.endswith("csv"):
            return file

def read_csv(file:str):
    with open(file,"r") as f:
        l=[]
        reader=csv.reader(f)
        for i in reader:
            l.append(i)
    return l

data=read_csv(file_path())

def tranform_data(data:list):
    for l in data:
        print(l)

tranform_data(data)
       
       
    
    

