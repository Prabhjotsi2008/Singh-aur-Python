# Meta-Characters 
> These are `special characters` that have a specific meaning in regular expressions.

> They are used to `define patterns` and control the behavior of the regex engine. Here are some common meta-characters:

| Meta-Character | Description | Example |
| --- | --- | --- |
| . (dot) | matches any character except a newline | `r"H.llo"` will match "Hello", "Hillo", "H3llo", etc. |
| ^ (caret) | matches the start of the string | `r"^Hello"` will match "Hello" at the beginning of the string |
| $ (dollar sign) | matches the end of the string | `r"World$"` will match "World" at the end of the string |
| * (asterisk) | matches zero or more occurrences of the preceding character | `r"a*"` will match "a", "aa", "aaa", etc. |
| + (plus) | matches one or more occurrences of the preceding character | `r"a+"` will match "a", "aa", "aaa", etc. |
| ? (question mark) | matches zero or one occurrence of the preceding character | `r"a?"` will match "a" or "" |
| [] (square brackets) | matches any character within the brackets | `r"[aeiou]"` will match any vowel |
| \| (pipe) | acts as an OR operator | `r"Hello\|World"` will match either "Hello" or "World" |
| () (parentheses) | groups patterns together | `r"(Hello\|World)"` will group the two alternatives together |

---

# Character Classes (Escape Sequences)
> These are special sequences that match specific types of characters.

| Character Class | Description | Example |
| --- | --- | --- |
| \d | matches any digit (0-9) | `r"\d+"` will match "123", "0", etc. |
| \D | matches any non-digit character | `r"\D+"` will match "abc", "Hello", etc. |
| \w | matches any word character (a-z, A-Z, 0-9, _) | `r"\w+"` will match "Hello123", "test_var", etc. |
| \W | matches any non-word character | `r"\W+"` will match "!@#", spaces, etc. |
| \s | matches any whitespace character (space, tab, newline) | `r"\s+"` will match spaces, tabs, newlines |
| \S | matches any non-whitespace character | `r"\S+"` will match "Hello", "123", etc. |
| \b | matches a word boundary (between \w and \W) | `r"\bHello\b"` will match "Hello" as a complete word |
| \B | matches a non-word boundary | `r"\B\w+"` will match characters not at word start |

---

# Character Ranges
> Define ranges of characters to match within square brackets.

| Pattern | Description | Example |
| --- | --- | --- |
| [a-z] | matches any lowercase letter | `r"[a-z]+"` will match "hello", "world" |
| [A-Z] | matches any uppercase letter | `r"[A-Z]+"` will match "HELLO", "WORLD" |
| [0-9] | matches any digit | `r"[0-9]+"` will match "123", "999" |
| [a-zA-Z] | matches any letter (upper or lower) | `r"[a-zA-Z]+"` will match "HelloWorld" |
| [a-zA-Z0-9] | matches any alphanumeric character | `r"[a-zA-Z0-9]+"` will match "Test123" |
| [^abc] | matches any character NOT in the brackets | `r"[^abc]"` will match any character except a, b, c |

---

# Quantifiers
> Specify how many times a pattern should occur.

| Quantifier | Description | Example |
| --- | --- | --- |
| * | zero or more times | `r"a*"` matches "", "a", "aa", "aaa" |
| + | one or more times | `r"a+"` matches "a", "aa", "aaa" (NOT empty) |
| ? | zero or one time (optional) | `r"a?"` matches "" or "a" |
| {n} | exactly n times | `r"a{3}"` matches "aaa" |
| {n,} | n or more times | `r"a{2,}"` matches "aa", "aaa", "aaaa" |
| {n,m} | between n and m times | `r"a{2,4}"` matches "aa", "aaa", "aaaa" |

---

# Special Regex Flags
> Modify the behavior of regex matching.

| Flag | Description | Usage |
| --- | --- | --- |
| re.IGNORECASE or re.I | Case-insensitive matching | `re.search(r"hello", text, re.IGNORECASE)` |
| re.MULTILINE or re.M | ^ and $ match line boundaries | `re.search(r"^line", text, re.MULTILINE)` |
| re.DOTALL or re.S | . matches newlines too | `re.search(r".*", text, re.DOTALL)` |
| re.VERBOSE or re.X | Ignore whitespace in pattern | `re.search(r"[a-z] +", text, re.VERBOSE)` |

---

# Common Regex Patterns
> Practical patterns for common use cases.

| Pattern | Purpose | Example |
| --- | --- | --- |
| `r"^\d{10}$"` | Matches exactly 10 digits | Phone number (no special chars) |
| `r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"` | Matches email | Email validation |
| `r"^\d{4}-\d{2}-\d{2}$"` | Matches date (YYYY-MM-DD) | Date format |
| `r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"` | Strong password | At least 8 chars with uppercase, lowercase, digit, special char |
| `r"^\+?1?\d{9,15}$"` | Matches phone numbers | International phone format |
| `r"^https?://"` | Matches URL protocol | HTTP or HTTPS URLs |