import re
# Lookahead

def is_valid_email(email):
    """
    TODO: Check if email (str) is a valid email format.
    Output: Bool, True if valid, otherwise False.
    """
    return re.match(r"^[a-z]+\.[a-z]+@[a-z]+\.[a-z]{2,}$", email) is not None


def find_mentions(text):
    """
    TODO: Extract all mentions (@username) from text (str).
    Output: List of mentions
    """
    return re.findall(r"@[a-zA-Z]+", text)

def redact_mentions(text, replace_with):
    """
    TODO: Replace all mentions (@username) in text (str)
    with replace_with (str).
    Output: Modified text (str)
    """
    return re.sub(r"@[a-zA-Z0-9]+", replace_with, text)

def is_strong_password(password):
    """
    TODO: Determine if password (str) is strong (rules within function).
    A strong password is defined as one that is at least 10 characters long, contains both uppercase and lowercase characters, has at least one numeral, and does not contain any spaces or tabs.
    Output: Bool, True if strong, otherwise False.
    """
    return re.match(r"\.{10,}")

def replace_links(text, replace_with):
    """
    TODO: Replace all URLs/links in text (str) with replace_with (str).
    Output: Modified text (str)
    """
    pass
