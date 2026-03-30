import keyword
import string


name = input("vvedite stroku")
punc = string.punctuation.replace("_","")

result = True
if name == "":
    result = False
else:
    if name[0].isdigit():
        result = False
    if name in keyword.kwlist:
        result = False
    for _ in name:
        if _ in punc:
            result = False
        if _.isupper():
            result = False
        if _== " ":
            result = False

    if name.count("_") > 1:
        result = False

print(result)