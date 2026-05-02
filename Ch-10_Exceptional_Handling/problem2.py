try:
    with open("output.csv","r") as f:
        print("reading file")
except FileNotFoundError as error:
    print(error)