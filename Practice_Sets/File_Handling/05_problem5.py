def fetch_file(file):
    with open(file) as f:
        text = f.read()
    return text

def update_file(file,content):
    with open(file, "w") as f:
        f.write(content)


content = fetch_file("censored_words.txt")

censored = ["donkey","idiot","fool"]

for word in censored:
    content = content.replace(word,"#"*len(word))
    

print(content)


update_file("censored_words.txt",content)
