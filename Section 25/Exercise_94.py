def find_indices(arr, element):
    def helper(index):
        # Base case: if index is equal to the length of the array, return empty list
        if index == len(arr):
            return []

        # Check if the current index contains the element
        if arr[index] == element:
            # Include the current index and proceed with the next index
            return [index] + helper(index + 1)
        else:
            # Proceed with the next index without including the current index
            return helper(index + 1)

    # Start the recursive search from index 0
    return helper(0)


print(find_indices([1, 2, 3, 2, 4, 2], 2))