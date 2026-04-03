def fetch_data(file):
    with open(file) as f:
        return f.read()
    
content1 = fetch_data("file1.txt")
content2 = fetch_data("file2.txt")

def compare_content(c1,c2):
    # return c1 == c2
    if c1 == c2:
        print("The two files are identical")
    else: print("The two files are not identical")

compare_content(content1,content2)