def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum
numbers = [1,2,3,4,5]
res = sum_list(numbers)
print(res)