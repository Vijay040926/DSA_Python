def is_anagram(s,t):
    t = list(t)
    if len(s)==len(t):
        if s == '' and t == '':
            return False
        for i in range(len(s)):
            if s[i] not in t:
                return False
        return True
res = is_anagram("anagram","nagaram")
print(res)