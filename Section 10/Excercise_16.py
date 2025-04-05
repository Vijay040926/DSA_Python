def celsius_to_fahrenheit(C):
    if C==C:
        F = (9/5*C)+32
    else:
        return False
    return F
res = celsius_to_fahrenheit(24)
print(res)