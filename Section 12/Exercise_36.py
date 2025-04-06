def sum_of_even_numbers(n):
    n = 2 * n + 1
    sum = 0
    for i in range(1, n):
        if i % 2 == 0:
            sum += i
    return sum


res = sum_of_even_numbers(3)
print(res)