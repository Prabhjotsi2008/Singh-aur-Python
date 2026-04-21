import re

# findall() returns a list of all non-overlapping matches of the pattern in the string

pattern = r"\b[A-Z]\w+\b" # checks if word starts with a capital letter and ends with a word boundary such that it is a whole word and not a part of a larger word"
text = "Hi guys, I am Prabhjot Singh, 18 Years old."

match_list = re.findall(pattern, text)
print(match_list)  # ['Hi', 'I', 'Prabhjot', 'Singh'] # returns a list of all the words that start with a capital letter and are whole words in the text

