def is_subsequence(s,t):
    i,j=0,0
    while i < len(s) and j<len(t):
        if s[i] == t[j]:
            j+=1
        i+=1
    return j == len(t)
res = is_subsequence( s = "abcde", t = "ace")
print(res)