import random

def shuffle(arr, left=0, right=None):
    '''
    Shuffles arr[l:r+1] unbiasedly with Fisher-Yates algorithm

    Note that the interval includes both l and r
    '''

    if not right:
        right = len(arr) - 1

    while right - left:
        idx = random.randint(left, right)
        arr[right], arr[idx] = arr[idx], arr[right]
        right = right - 1
