def binary_to_decimal(binary_str):
    n= len(binary_str)
    decimal_rep=0
    for i in range(0,n):
        decimal_rep = int(binary_str[i])*2**(n-i-1)+decimal_rep
    return decimal_rep
res = binary_to_decimal('1101')
print(res)