from misc.shuffle import *

def test_shuffle():
    '''
    This only tests the integrity of the shuffled array.

    This is not a statistical test to assert its randomness.
    '''

    arr = list(range(10000))
    shuffled_arr = arr.copy()
    shuffle(shuffled_arr)
    
    assert sorted(shuffled_arr) == arr

def test_shuffle_slice():
    '''
    This only tests the integrity of the shuffled array.

    This is not a statistical test to assert its randomness.
    '''

    arr = list(range(10000))
    shuffled_arr = arr.copy()
    shuffle(shuffled_arr, 2000, 8000)

    assert sorted(shuffled_arr) == arr