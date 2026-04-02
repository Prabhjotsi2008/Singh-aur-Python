file = open("file.txt","r")

first_list = file.readline() # gives first line

## NOTE: Since file is an iterator by default so if we do readline() again then it will give the next line and so on until the end of the file (EOF). After that it will give empty string "".

lines = file.readlines() # gives a list of all the lines in the file 
# NOTE: Since we have already read the first line using readline() so it will give the remaining lines in the file as a list. If we do readlines() again then it will give an empty list [] because we have already reached the end of the file (EOF).

print(first_list)
print(lines)

file.close()


with open("file.txt","r") as f:
    for index,line in enumerate(f,start=1):
        print(f"Line {index}: {line}")