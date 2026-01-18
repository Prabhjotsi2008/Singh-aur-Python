friends_group = {}

for i in range(4):
    key = input("Enter your name: ")
    val = input("Enter your favourite Language: ")
    friends_group[key] = val

for k,v in friends_group.items():
    print(k,":",v)