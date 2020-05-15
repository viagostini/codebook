def delete_after(node: ListNode) -> None:
    '''
    Delete the node past this one. Assume node is not a tail.
    '''
    node.next = node.next.next