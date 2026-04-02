def getData():
    name = input("Enter Name: ").capitalize()
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (M/F): ").upper()

    return f"Name: {name}\nAge: {age}\nGender: {gender}\n\n"

output = getData()

file = open("db.txt","a")

file.write(output) # if we opened in read "r" mode then it will give error # io.UnsupportedOperation: not writable

file.close()