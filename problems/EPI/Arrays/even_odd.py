def even_odd(A: List[int]) -> None:
    '''
    Solution: Keep pointers to where next even and odd numbers
    should go, swap accordingly during while loop.

    Time Complexity: O(N)
    Space Complexity: O(1)
    '''
    next_even, next_odd = 0, len(A) - 1

    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1