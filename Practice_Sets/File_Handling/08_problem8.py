def fetch_data(file):
    with open(file) as f:
        return f.read()
    

content = fetch_data("this.txt")

def paste_data(file,content):
    with open(file,"w") as f :
        f.write(content)

paste_data("that.txt",content)