def plus_one(digits):
    digits_list = [str(i) for i in digits]
    num = ''.join(digits_list)
    num = int(num)
    num+=1
    digits_list = [int(i) for i in str(num)]
    return digits_list

digits=[1, 2, 3]
res = plus_one(digits)
print(res)