class BinarySearchTree:
    """
    Binary Search Tree implementation using only iterative methods

    This binary search tree behaves like a tree map since you store
    (key, value) pairs and they are sorted internally by key (if you
    do an inorder traversal). This makes it so that most operations
    on the tree will be O(log n) instead of O(1) with hash maps, in
    exchange for being able to mantain order.

    Implemented Methods
    -----------------
    inorder()        : O(n)
    search(key)      : O(log n)
    insert(key, val) : O(log n)

    TODO: this class is a work in progress
    """

    class TreeNode:
        def __init__(self, key, val, parent=None):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.parent = parent
    

    def __init__(self):
        self.root = None
        self.size = 0

    def search(self, key):
        """
        Iteratively searches for key in binary search tree and returns
        associated value if it exists, None otherwise
        """

        node = self.root
        while node and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node.val if node else None

    def insert(self, key, val):
        """
        Iteratively inserts key value pair in binary search tree.
        If the key already exists, replaces its value with the new one
        """

        if not self.size:
            self.root = self.TreeNode(key, val)
            self.size += 1
            return
        
        node = self.root
        while True:
            if key == node.key:
                node.val = val
                break
            elif key < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = self.TreeNode(key, val)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = self.TreeNode(key, val)
                    break

        self.size += 1

    def inorder(self, out=[]):
        """
        Iteratively traverse nodes in sorted order and return them in
        list format.
        """       

        node, stack = self.root, []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                out.append((node.key, node.val))
                node = node.right
            
        return out