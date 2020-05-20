
class MinHeap():

    def __init__(self):
        self.heap = [0]

    def build_heap(self, seq):
        '''
        Builds a min-heap from a list. Starting from the middle elements
        and using heapify_down can be shown to be the most efficient way,
        achieving linear time bounds.

        Time Complexity: O(n) 
        '''
        i = len(seq) // 2
        self.heap = [0] + seq[:]
        
        for i in range(i, 0, -1):
            self.heapify_down(i)

    def min_element(self):
        '''
        Returns smallest element in heap, but does not remove it.

        Time Complexity: O(1)
        '''
        return self.heap[1] if self.size() else None 

    def insert(self, val):
        '''
        Inserts a new element in the heap and reorders nodes
        accordingly so that min-heap invariant holds.

        Time Complexity: O(log n)
        '''
        self.heap.append(val)
        self.heapify_up(self.size())

    def extract_min(self):
        '''
        Returns the smallest element in the heap and removes it,
        reordering nodes accordingly so that min-heap invariant holds.

        Time Complexity: O(log n)
        '''
        ret = self.heap[1]
        
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        
        self.heapify_down(1)
        return ret


    def heapify_down(self, idx):
        '''
        Function used to sift an element down the heap to a
        correct position.

        Time Complexity: O(log n)
        '''
        while 2*idx <= self.size():
            child = self.min_child(idx)
            if self.heap[idx] > self.heap[child]:
                self.swap(idx, child)
            idx = child

    def heapify_up(self, idx):
        '''
        Function used to sift an element up the heap to a
        correct position.

        Time Complexity: O(log n)
        '''
        while (parent := idx // 2) > 0:
            if self.heap[idx] < self.heap[parent]:
                self.swap(idx, parent)
            idx = parent
    
    def swap(self, i, j): 
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def min_child(self, idx):
        if 2*idx + 1 > self.size():
            return 2*idx
        
        if self.heap[2*idx] < self.heap[2*idx + 1]:
            return 2*idx
        
        return 2*idx + 1

    def size(self):
        return len(self.heap) - 1
