import string


punct = string.punctuation
name = input("Enter smth, i\'l do hashtag: ")
name = name.strip()
clean_text = ""
for _ in name:
    if _ not in punct:
        clean_text += _
words = clean_text.split()
result = "#"
for _ in words:
    result += _.capitalize()
result = result[:140]
print(result)