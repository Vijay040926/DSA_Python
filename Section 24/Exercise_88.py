def count_digits(n):
    if n>=1 and n<=9:
        return 1
    n = int(n/10)
    ans = count_digits(n)
    res = 1 + ans
    return res

print(count_digits(12345))