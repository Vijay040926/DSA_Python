def remove_duplicates(s):
    s = list(s)
    l = []
    for i in s:
        if i not in l:
            l.append(i)
    s = ''.join(l)
    return s
res = remove_duplicates("programming")
print(res)