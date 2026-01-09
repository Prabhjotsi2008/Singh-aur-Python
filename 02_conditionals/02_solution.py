# MOVIE TICKET PRICING
age = int(input("Enter your age : "))
day = input("Enter Day : ")

# LOGIC USING SHORTHAND
price = 12 if age >=18 else 8 # shorthand of if-else
price -= 2 if day=="Wednesday" or "wednesday" else 0 # discount of 2 if "Wednesday" or "wednesday", else no discount


# LOGIC USING FULL IF-ELSE
# if(age<18):
#     price = 8
# else:
#     price = 12

# if(day=="Wednesday" or day=="wednesday"):
#     price -= 2

# FINAL OUTPUT
print("Movie Ticket Price : $", price)