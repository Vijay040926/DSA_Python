def is_palindromic_tuple(tup):
    tup1= tup
    if tup == tup1[::-1]:
        return True
    else:
        return False
tup=(1,2,3,2,1)
res=is_palindromic_tuple(tup)
print(res)