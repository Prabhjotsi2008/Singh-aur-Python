# TEXT-CLEANER

import re

text = input("Enter text: ")
pattern = r"[^\w\s]+" # \w -> A-Za-z0-9_ # \s -> whitespaces

cleaned_text = re.sub(pattern,"",text)

print(cleaned_text)