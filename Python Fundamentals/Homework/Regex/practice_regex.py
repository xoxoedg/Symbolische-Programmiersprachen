import re
# Pattern: Lookahead (?=abc)
# Negative Lookahead
print(re.search(r"(?=abc)", "abcde").string)

# Findet Buchstaben, die vor einer Ziffer stehen
text = "a3 b4 c x9 y z0"
re.findall(r"[a-z](?=\d)", text)

# Findet Buchstaben, die nicht vor einer Ziffer stehen
re.findall(r"[a-z](?!\d)", text)