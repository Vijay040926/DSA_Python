def count_vowels(s):
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    count = 0
    n = len(s)
    for i in range(n):
        if s[i] in vowels:
            count+=1
    return count
res = count_vowels("Hello World!")
print(res)