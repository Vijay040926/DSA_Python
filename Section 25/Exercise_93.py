def find_first_index(arr, element):
    if len(arr) == 0:
        return -1
    if arr[0] == element:
        return 0
    ans = find_first_index(arr[1:],element)
    if ans == -1:
        return ans
    else:
        return ans + 1