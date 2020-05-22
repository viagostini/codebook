class LinkedList(object):
    '''
    Implements a singly linked list with insert, delete and get methods.

    TODO: maybe one day make it a deque-like implementation with queue/stack
    functions.
    '''

    class ListNode(object):
        def __init__(self, data=0, next_node=None):
            self.data = data
            self.next = next_node

    def __init__(self, head=None):
        self.size = 0
        self.head = head

    def delete(self, pos=None):
        '''
        Deletes ListNode at position `pos`.
        Default position to delete from is at end of list.
        (Note that this is worst-case in terms of time complexity.)

        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        if pos is None:
            pos = self.size-1

        node = self.head
        if pos:
            for _ in range(pos-1):
                node = node.next
            node.next = node.next.next
        else:
            self.head = node.next

        self.size -= 1


    def insert(self, data, pos=None):
        '''
        Inserts a new ListNode with data `data` at position `pos`
        Default position to insert is at end of list.
        (Note that this is worst-case in terms of time complexity.)

        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        if pos is None:
            pos = self.size
        
        new_node = self.ListNode(data)

        if not pos:
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.head
            for _ in range(pos-1):
                node = node.next

            new_node.next = node.next
            node.next = new_node
        
        self.size += 1

    def get(self, pos=0):
        if self.size and pos < self.size:
            node = self.head
            for _ in range(pos):
                node = node.next
            return node.data
        else:
            return None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.data)
            node = node.next
        return out
