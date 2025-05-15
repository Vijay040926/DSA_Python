def next_greatest_letter(letters, target):
    for i in range(len(letters)):
        if letters[i] > target:
            return letters[i]
    return letters[0]
letters = ['c', 'f', 'j']
target = 'k'
res = next_greatest_letter(letters, target)
print(res)