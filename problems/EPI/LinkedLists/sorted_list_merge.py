def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    Solution: Traverse both lists at the same time appending the smaller
    node to the answer. In the end append any leftover nodes.
    
        head is needed in order to return the beginning of list
        tail keeps track of the end of our list to add new elements

    Time Complexity: O(N + M) where N = len(L1) and M = len(L2)
    Space Complexity: O(1)
    '''

    head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        
        tail = tail.next
    
    # here either L1 or L2 is null
    tail.next = L1 or L2
    return head.next
