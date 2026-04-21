# DIGIT EXTRACTOR

import re
text = "I have 2 apples and 10 bananas"
pattern = r"\b\d+\b"
digit_list = re.findall(pattern,text)

print(digit_list) # ['2', '10']