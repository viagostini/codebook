class Stack:
    '''
    Implements a Stack with max() operation using Python lists.
    max_so_far[i] = max element with the bottommost i elements in stack.
    In particular, max_so_far[-1] is max of entire stack.

    All operations have O(1) time complexity.
    '''
    
    def __init__(self):
        self.arr = []
        self.max_so_far = [float('-inf')]

    def empty(self) -> bool:
        return len(self.arr) == 0

    def max(self) -> int:
        return self.max_so_far[-1]

    def pop(self) -> int:
        self.max_so_far.pop()
        return self.arr.pop()

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.max_so_far.append(max(x, self.max_so_far[-1]))