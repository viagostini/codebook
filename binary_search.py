# Iterative Binary Search Function

# returns index of x in arr if present or -1 if not present
def binary_search(arr, x):
    l, r = 0, len(arr)-1

    while l <= r:
        mid = (l + r) // 2; 

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


# wrapper function for recursive binary search
def binary_search_recursive (arr, x):
    return _binary_search_recursive(arr, 0, len(arr)-1, x)

# returns index of x in arr if present or -1 if not present 
def _binary_search_recursive (arr, l, r, x): 
	if r >= l: 
		mid = l + (r - l) // 2

		# check if x is present at mid
		if x == arr[mid]: 
			return mid 
		
		# if x is greater, search in right half
		elif x > arr[mid]: 
			return _binary_search_recursive(arr, mid+1, r, x) 
		
		# if x is smaller, search in left half
		else:
			return _binary_search_recursive(arr, l, mid-1, x) 

	else: 
		# l > r, so x is not present in arr
		return -1

# returns index of first element > x or len(arr) if there is none
def upper_bound(arr, x):
    l, r = 0, len(arr)

    while l < r:
        mid = (l + r) // 2

        # the answer must be in [l, mid]
        if arr[mid] > x:
            r = mid
        
        # the answer must be in [mid+1, r]
        else:
            l = mid + 1

    return l

# returns index of first element >= x or len(arr) if there is none
def lower_bound(arr, x):
    l, r = 0, len(arr)

    while l < r:
        mid = (l + r) // 2

        # the answer must be in [mid+1, r]
        if arr[mid] < x:
            l = mid + 1
        
        # the answer must be in [l, mid]
        else:
            r = mid

    return l