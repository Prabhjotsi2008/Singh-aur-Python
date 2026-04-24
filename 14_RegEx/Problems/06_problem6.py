# URL-Extractor

import re

text = "Visit https://google.com and http://example.org"

pattern = r"\bhttps?://[A-Za-z]+\.[a-zA-z]+\b"

url_list = re.findall(pattern,text)

print(f"URLs are: {', '.join(url_list)}")