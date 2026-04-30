import os

su=(os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data")))
las_load="2026-04-29"
for i in su:
    if i.split(".")[0]>las_load:

        print(f"{i} is new file")
