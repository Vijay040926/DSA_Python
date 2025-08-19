def count_to_n(n):
    if n == 1:
        return [1]
    # Recursive case: append n to the result of count_to_n(n - 1)
    return count_to_n(n - 1) + [n]