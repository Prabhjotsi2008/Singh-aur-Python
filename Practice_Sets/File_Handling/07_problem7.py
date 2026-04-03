def fetch_data(file):
    with open(file) as f:
        return f.readlines()
    

lines_list = fetch_data("log.txt")

for line  in lines_list:
    if "python" in line:
        print(f"Word \'Python\' present in line no. {lines_list.index(line) + 1}")
        break

else: # runs if the for loop ends without break # means that the word "python" was not found in any line
    print("Word \'Python\' is not present")