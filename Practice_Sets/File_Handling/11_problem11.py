import os

def fetch_data(file):
    with open(file) as f:
        return f.read()
    

content = fetch_data("old.txt")

os.remove("old.txt") # removes file

def paste_data(file,content):
    with open(file,"w") as f :
        f.write(content)

paste_data("renamed_by_python.txt",content)