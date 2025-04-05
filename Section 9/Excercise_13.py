def generate_hollow_right_angled_triangle(n):
    lst = []
    for i in range(1, n + 1):
        if i == 1:
            lst.append('*')
        elif i < n:
            lst.append('*' + ' ' * (i - 2) + '*')
        else:
            lst.append('*' * i)

    return lst


res = generate_hollow_right_angled_triangle(5)
print(res)