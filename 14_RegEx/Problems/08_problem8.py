# DATE-Extractor

import re

text = "Today is 24-04-2026 and tomorrow will be  25-04-2026"
# pattern = r"\b[0-3][0-9]-[0-1][0-9]-[1-2]\d{3}\b" # output will be a string as there is no groups

# pattern = r"\b(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(0[1-9]|1[0-2])-(\d{4})\b" # capturing-groups # output is a tuple, not a string

pattern = r"\b(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])-(?:0[1-9]|1[0-2])-(?:\d{4})\b" # used ?: for non-capturing groups


date_list = re.findall(pattern,text)

print(f"Dates are: {" ".join(date_list)}")
# print(date_list)