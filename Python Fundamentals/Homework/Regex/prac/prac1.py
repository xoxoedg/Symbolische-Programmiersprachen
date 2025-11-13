import re

def get_all_upper(text):
    return re.findall(r"\b[A-Z][a-z]+",text)


def get_decimal(text):
    return re.findall(r"-?[0-9]+(?:\.\d+)?",text)

def a(text):
    pass