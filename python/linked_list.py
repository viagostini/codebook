class LinkedList(object):
    
    class ListNode(object):
        def __init__(self, data=0, next_node=None):
            self.data = data
            self.next = next_node

    def __init__(self, head=None):
        self.size = 0
        self.head = head

    # TODO: delete()

    def insert(self, data, pos=0):
        new_node = self.ListNode(data)

        if pos == 0:
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



a = LinkedList()
a.insert(1, 0)
a.insert(2, 1)
a.insert(3)
a.insert(4)
a.insert(7, 2)
a.insert(10, a.size)
print(a.to_list())
print(a.get(2))