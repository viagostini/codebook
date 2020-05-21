def find_all_occurrences(pattern, text):
    '''
    Finds the starting index for all occurrences of pattern inside text.

    First we concatenate the pattern and the text in order to compute
    the Z values. Then, there is an occurrence of pattern starting at index
    i if Z[i] >= len(pattern).

    Time Complexity: O(|pattern| + |text|)
    Space Complexity: O(|pattern| + |text|)
    '''
    z = z_function(pattern + text)
    
    retval = []
    for idx, zi in enumerate(z):
        if idx >= len(pattern) and zi >= len(pattern):
            retval.append(idx - len(pattern))
    
    return retval

def z_function(string):
    '''
    Computes Z values for a given string in linear time.

    Code based on: https://cp-algorithms.com/string/z-function.html

    Time Complexity: O(|string|)
    Space Complexity: O(|string|)
    '''
    n = len(string)
    z = [0] * n

    left = right = 0
    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        
        while i + z[i] < n and string[z[i]] == string[i + z[i]]:
            z[i] += 1
        
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    
    return z