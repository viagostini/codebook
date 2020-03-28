# Iterative Binary Search Function

# returns index of x in arr if present or -1 if not present
def binarySearch(arr, x):
    l, r = 0, len(arr)-1

    while l <= r:
        mid = l + (r - l) // 2; 

        # check if x is present at mid 
        if x == arr[mid]: 
            return mid 

        # if x is greater, search in right half 
        elif x > arr[mid]: 
            l = mid + 1

        # if x is smaller, search in left half 
        else: 
            r = mid - 1
    
    # l > r, so x is not present in arr
    return -1


# test array 
arr = [2, 7, 12, 20, 42, 57] 

# test case: element present in the beginning
ans = binarySearch(arr, 2)
assert ans == 0, "Result was {} but expected result is: 0".format(ans)

# test case: element present in the middle
ans = binarySearch(arr, 20)
assert ans == 3, "Result was {} but expected result is 3".format(ans)

# test case: element present in the end
ans = binarySearch(arr, 57)
assert ans == 5, "Result was {} but expected result is 5".format(ans)

# test case: element not present and smaller than first element
ans = binarySearch(arr, -3)
assert ans == -1, "Result was {} but expected result is -1".format(ans)

# test case: element not present and greater than last element
ans = binarySearch(arr, 60)
assert ans == -1, "Result was {} but expected result is -1".format(ans)