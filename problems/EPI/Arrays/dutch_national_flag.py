def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    '''
    Solution: Count occurrence of each color and fill in with all RED
    followed by all WHITE followed by all BLUE (Note that this is always
    a valid partitioning).

    Time Complexity: O(N)
    Space Complexity: O(1)
    '''
    count = [0, 0, 0]
    for x in A:
        count[x] += 1

    j = 0
    for i in range(3):
        while count[i]:
            A[j] = i
            count[i] -= 1
            j += 1

    return A

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]

    '''
    Solution: Keep the following invariants during partitioning:
        bottom group: A[:smaller]
        middle group: A[smaller:equal]
        unclassified: A[equal:larger]
        top group: A[larger:]
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    '''
    smaller, equal, larger = 0, 0, len(A)
    
    # iterate while there is an unclassified element
    while equal < larger:
        # A[equal] is the next unclassified element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

    return A