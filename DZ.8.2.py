def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]



assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('OP') == False
assert is_palindrome('a.') == True
assert is_palindrome('aurora') == False

print("OK")