# WORD-EXTRACTOR

import re

text = "Hello! My name is Prabh."
pattern = r"\b\w+\b"
# words_iter = re.finditer(pattern,text) # returns an iterator , not a list

words_list = re.findall(pattern,text) # returns a list
print(words_list) # ['Hello', 'My', 'name', 'is', 'Prabh']