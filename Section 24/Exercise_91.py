def count_down(n):
    if n == 1:
        return [1]
    return [n] + count_down(n - 1)


print(count_down(5))