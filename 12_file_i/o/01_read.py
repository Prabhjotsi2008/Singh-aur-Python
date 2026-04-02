# AAM-ZINDAGI
file = open("file.txt") # by default read mode "r"
data = file.read()
print(data)
file.close()


# MENTOS-ZINDAGI
file = open("file.txt","r")
# file = open("file.txt") # same as above

with file as f: # implicitally closes the file
    print(f.read())


# file.read() # ValueError: I/O operation on closed file.