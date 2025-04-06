def int_to_binary(n):
    if n == 0:
        return '0'
    binary_rep = ''
    is_negative = n < 0
    if is_negative:
        n = -n

    while n > 0:
        remainder = n % 2
        binary_rep = str(remainder) + binary_rep
        n = n // 2

    if is_negative:
        binary_rep = '-' + binary_rep

    return binary_rep


res = int_to_binary(5)
print(res)