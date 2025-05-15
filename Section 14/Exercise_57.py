def insertion_sort(lst):
    n = len(lst)
    for i in range(1,n):
        currentPos = lst[i]
        correctPos = i - 1
        while correctPos >=0 :
            if lst[correctPos] < currentPos:
                break
            else:
                lst[correctPos+1] = lst[correctPos]
                correctPos-=1
            lst[correctPos+1] = currentPos
    return lst
lst = [12, 11, 13, 5, 6]
res = insertion_sort(lst)
print(res)