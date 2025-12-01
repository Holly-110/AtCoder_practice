import string
import sys

S = str(input())

all_letters = set(string.ascii_lowercase)

s_letters = set(S)

missing_letters = all_letters - s_letters

if len(S) == 1:
    print(sorted(list(missing_letters))[0])
else :
    print(sorted(list(missing_letters))[0])