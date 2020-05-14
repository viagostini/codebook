def is_palindromic(s: str) -> bool:
    '''
    Solution: s[~i] = s[-(i+1)] for i in [0, len(s) - 1]

    Time Complexity: O(N), where N = len(s)
    Space Complexity: O(1)
    '''
    return all(s[i] == s[~i] for i in range(len(s) // 2))
