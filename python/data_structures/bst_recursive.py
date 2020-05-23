class BinarySearchTree:
    """
    Binary Search Tree implementation using only recursive methods

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
        Wrapper for internal __search function
        """

        return self.__search(self.root, key)

    def insert(self, key, val):
        """
        Wrapper for internal __insert function
        """

        self.size += 1
        self.root = self.__insert(self.root, key, val)

    def inorder(self):
        """
        Wrapper for internal __inorder function
        """
        return self.__inorder(self.root)
    


    def __search(self, root, key):
        """
        Recursively searches for key in binary search tree and returns
        associated value if it exists, None otherwise
        """

        if not root:
            return None  
        
        if key == root.key:
            return root.val

        if key < root.key:
            return self.__search(root.left, key)

        return self.__search(root.right, key)

    def __insert(self, root, key, val):
        """
        Recursively inserts key value pair in binary search tree.
        If the key already exists, replaces its value with the new one
        """

        if not root:
            return self.TreeNode(key, val)

        if key == root.key:
            root.val = val
        elif key < root.key:
            root.left = self.__insert(root.left, key, val)
        else:
            root.right = self.__insert(root.right, key, val)
        
        return root

    def __inorder(self, root):
        """
        Recursively traverse nodes in sorted order and return them in
        list format.
        """

        if not root:
            return []

        left = self.__inorder(root.left)
        right = self.__inorder(root.right)

        return left + [(root.key, root.val)] + right