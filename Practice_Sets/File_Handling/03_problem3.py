# MY-WAY    
# def generate_table(num):
#     with open("table.txt", "a") as file:
#         for i in range(1,11):
#             line = f"{num} X {i} = {num*i}\n"
#             file.write(line)
        
#         file.write("\n")


# HARRY-WAY
def generate_table(num):
    table = f"TABLE OF {num}\n\n"
    for i in range(1,11):
        table += f"{num} X {i} = {num*i}\n"
    
    with open(f"tables/table_{num}.txt","w") as t:
        t.write(table)

    


for i in range(2,21):
    generate_table(i)