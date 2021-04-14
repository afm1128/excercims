import re

def abbreviate(words):
    words = re.sub(r"'",'', words)
    words = re.sub(r"[_,.-]+",' ', words)
    words = re.sub(r"[\W|\s]+",' ', words)
    words = words + " "
    return re.sub(r"([\w])\S*\s", "\\1", words).upper()