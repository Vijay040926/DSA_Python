def is_substring(s,t):
    s= s.split()
    if t == '':
        return True
    else:
        for i in range(len(s)):
            if s[i] == t:
                return True
        return False
res = is_substring(s = "hello world", t = "world")
print(res)