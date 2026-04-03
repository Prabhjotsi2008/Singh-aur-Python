def fetch_file(file):
    with open(file) as f:
        text = f.read()
    return text

def update_file(file,content):
    with open(file, "w") as f:
        f.write(content)

censored = ["donkey","idiot","fool"]

content = fetch_file("donkey_file.txt")

print(content)
updated_content = content.replace("donkey", "######").replace("Donkey","######")

update_file("donkey_file.txt", updated_content)
