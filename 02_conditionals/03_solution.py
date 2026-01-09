# GRADE CALCULATOR
marks = int(input("Enter your score (out of 100) : "))

# CHECK VALIDATION OF MARKS
if marks > 100 or marks < 0:
    print("Invalid marks entered")
    exit() # works same as return 0; in CPP


# RUNS ONLY IF MARKS IS VALID
grade = ""
# LOGIC
if(marks>=90):
    grade = "A"
elif marks>=80:
    grade = "B"
elif marks>=70:
    grade = "C"
elif marks>=60:
    grade = "D"
else:
    grade = "F"

# OUTPUT
print("Marks Obtained :", marks)
print("Calculated Grade :", grade)