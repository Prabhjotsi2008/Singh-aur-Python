msg = input("Enter a message: ")

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"


if p1 in msg or p2 in msg or p3 in msg or p4 in msg:
    print("It is a spam message")
else:
    print("It is a genuine message")