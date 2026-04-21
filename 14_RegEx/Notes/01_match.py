import re

# match() checks for a match only at the beginning of the string
pattern = r"Hello"
text = "Hello World, Hello Python"


match1 = re.match(pattern, text)
print(match1)  # <re.Match object; span=(0, 5), match='Hello'>
print(match1.span())  # (0, 5) # gives the start and end indices of the match
print(match1.group())  # Hello # gives the matched string


text = "Hi World, Hello Python"
match2 = re.match(pattern, text)
print(match2)  # None, because the pattern does not match at the beginning of the string