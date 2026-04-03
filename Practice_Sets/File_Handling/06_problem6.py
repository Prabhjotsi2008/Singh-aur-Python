def fetchData(file):
    with open(file) as f:
        return f.read()
    

content = fetchData("log.txt")

if "python" in content:
    print("Word \'Python\' is present in log file")
else: print("Word \'Python\' is NOT present in log file")