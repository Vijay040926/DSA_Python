def generate_hollow_square(n):
    lst = []
    for i in range(n):
        if i != 0 and i != n - 1:
            lst.append('*' + ' ' * (n - 2) + '*')
        else:
            lst.append('*' * n)
    return lst


result = generate_hollow_square(3)
print(result)