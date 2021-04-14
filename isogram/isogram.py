from collections import Counter
import string as stringlib

def is_isogram(string):
    input = string.lower().replace('-','').translate({ ord(ch): None for ch in stringlib.whitespace })
    letters = Counter(input)
    for item in letters.most_common():
        if item[1] > 1: return False
    return True