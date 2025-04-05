import math
def find_largest(numbers):
    largest = float('-inf')
    for i in numbers:
        largest = max(i,largest)
    return largest
numbers=[-1,-2,-3,-4,-5]
res = find_largest(numbers)
print(res)