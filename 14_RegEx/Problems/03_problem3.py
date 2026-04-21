# Email-EXTRACTOR

import re
text = "Contact me at test123@gmail.com or hello@company.in"
pattern = r"\b[\w.-]+@[\w.-]+\.\w{2,}\b"
email_list = re.findall(pattern,text) # ['test123@gmail', 'hello@company']

print(f"Emails are: {', '.join(email_list)}") # Emails are: test123@gmail, hello@company