import re


# search() checks for a match anywhere in the string
pattern = "Hello"
text = "Hi World, Hello Python"

search1 = re.search(pattern, text)
print(search1)  # <re.Match object; span=(10, 15), match='Hello'>
print(search1.span())  # (10, 15) # gives the start and end indices of the match
print(search1.group())  # Hello # gives the matched string



# pattern = r"\b[A-Z]\w+\b" # checks if word starts with a capital letter and ends with a word boundary
pattern = r"\d{10}" # checks for a sequence of exactly 10 digits, which is a common pattern for phone numbers
text = "Hi guys, I am Prabhjot Singh, 18 Years old. The phone1212121212 number is 1234567890"

search2 = re.search(pattern,text)
print(search2) # <re.Match object; span=(64, 74), match='1234567890'>
print("Matched String:",search2.group()) # 1234567890
print("Start index:", search2.start())
print("End index:", search2.end())



pattern = r"\b\d{10}\b" # checks for a sequence of exactly 10 digits that is a whole word (not part of a larger number or string)

search3 = re.search(pattern,text)
print(search3) # <re.Match object; span=(64, 74), match='1234567890'>, because the 10-digit number is a whole word in the text