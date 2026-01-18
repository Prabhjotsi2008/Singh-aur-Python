my_list = []

for i in range(3):
    num = float(input(f"Enter Subject {i+1} marks: "))
    my_list.append(num)

total_percent = (sum(my_list) * 100) / 300

m1,m2,m3 = my_list

if(total_percent>=40 and m1>=33 and m2>=33 and m3>=33):
    print("Result: Pass")
else:
    print("Result: Fail")

print("Percentage:",total_percent)