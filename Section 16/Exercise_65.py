def is_palindrome(lst):
    if lst == lst[::-1]:
        return True
    return False
lst = [7, 8, 9, 8, 7]
res = is_palindrome(lst)
print(res)