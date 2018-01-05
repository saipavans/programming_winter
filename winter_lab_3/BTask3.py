def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("python"))
print(is_palindrome("rotor"))