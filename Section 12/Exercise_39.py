import math
def is_perfect_square(num):
    q = int(math.sqrt(num))
    if q**2 == num:
        return True
    return False
res = is_perfect_square(81)
print(res)