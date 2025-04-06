def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
res = is_prime(5)
print(res)