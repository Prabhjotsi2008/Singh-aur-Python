# LIST UNIQUESNESS CHECKER
items = ["guava","apple", "banana", "orange", "apple", "mango"]

# MY APPROACH
# for item in items:
#     print(item)
#     if items.count(item) > 1:
#         print(f"Duplicate Item : {item}")
#         break


# CHAI APPROACH
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate item :", item)
        break
    unique_item.add(item)
