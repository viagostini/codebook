def count_bits(x: int) -> int:
    '''
    Solution: Isolate last bit with x & 1 and count if it is set.
        Note that a better solution is presented in parity.py

    Time Complexity: O(n) where n is total number of bits in x
    Space Complexity: O(1)
    '''
    num_bits = 0

    while x:
        num_bits += x & 1
        x >>= 1
    
    return num_bits