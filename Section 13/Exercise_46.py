def is_palindrome(s):
    s = s.lower().replace(' ', '')
    s1 = s[::-1]
    if s1 == s:
        return True
    else:
        return False
res = is_palindrome("A man a plan a canal Panama")
print(res)