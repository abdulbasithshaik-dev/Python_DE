import os

#current working directory
print(os.getcwd())

#full path
print(os.path.abspath(__file__))

#current directory
print(os.path.dirname(os.path.abspath(__file__)))

#list all files and directories in current directory
print(os.listdir())


for i in os.listdir():
    if os.path.isfile(i):
        print(f"{i} is a file")
    elif os.path.isdir(i):
        print(f"{i} is a directory")
