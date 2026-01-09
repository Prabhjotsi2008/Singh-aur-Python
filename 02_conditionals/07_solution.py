# COFFEE CUSTOMIZATION
order_size = input("Enter Coffee size (small, medium, large) : ")
extra_shot = input("Would you like to have an extra shot (Yes/No): ").lower()


# LOGIC
if extra_shot == "yes":
    order_size += " coffee with an extra shot"
else:
    order_size += " coffee only"


# OUTPUT
print(f"Your order is a {order_size}")