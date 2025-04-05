def generate_square(n):
    lst = ['*' * n for i in range(0, n)]
    return lst


test_square_size_1 = generate_square(1)
generate_square(3)
generate_square(5)
print(test_square_size_1)