def count_consonants(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    s = s.replace(',','').strip('.,!?;:')
    s=s.replace(' ','')
    for i in range(len(s)):
        if s[i] not in vowels:
            count+=1
    return count
res = count_consonants("Hello, World!")
print(res)