def are_equal_strings(s,t):
    n = len(s); n1 = len(t)
    if n == n1:
        if s == '' and t == '':
            return True
        else:
            for i in range(n):
                if s[i] == t[i]:
                    return True
                else:
                    return False
res = are_equal_strings('hello','hello')
print(res)