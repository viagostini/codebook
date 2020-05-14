def int_to_string(x: int) -> str:
    '''
    Time Complexity: O(log N) = number of digits of N
    Space Complexity: O(log N) = number of digits of N
    '''
    ans = [] if x else ['0']
    sign = '-' if x < 0 else ''

    while x := abs(x):
        ans.append(str(x % 10))
        x = x // 10

    return sign + ''.join(reversed(ans))


def string_to_int(s: str) -> int:
    '''
    Time Complexity: O(log N) = number of digits of N
    Space Complexity: O(log N) = number of digits of N
    '''
    ans, base = 0, 1
    sign = -1 if s[0] == '-' else 1

    if not s[0].isdigit():
        s = s[1:]

    for ch in s:
        ans = (ans * 10) + int(ch)
        base *= 10

    return ans * sign