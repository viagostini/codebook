class BinarySearchTree:
    """
    Binary Search Tree implementation using only recursive methods

    This binary search tree behaves like a tree map since you store
    (key, value) pairs and they are sorted internally by key (if you
    do an inorder traversal). This makes it so that most operations
    on the tree will be O(h) instead of O(1) with hash maps, in
    exchange for being able to mantain order.

    Implemented Methods
    -----------------
    inorder()        : O(n)
    search(key)      : O(h)
    insert(key, val) : O(h)
    delete(key)      : O(h)

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
        self.size += 1
        self.root = self.__insert(self.root, key, val)

    def delete(self, key):
        self.__delete(self.root, key)

    def inorder(self):
        return self.__inorder(self.root)


    def __search(self, root, key):
        if not root:
            return None  
        
        if key == root.key:
            return root.val

        if key < root.key:
            return self.__search(root.left, key)

        return self.__search(root.right, key)

    def __insert(self, root, key, val):
        if not root:
            return self.TreeNode(key, val)

        if key == root.key:
            root.val = val
        elif key < root.key:
            root.left = self.__insert(root.left, key, val)
        else:
            root.right = self.__insert(root.right, key, val)
        
        return root

    def __delete(self, root, key):
        if not root:
            return root
        
        if key < root.key:
            root.left = self.__delete(root.left, key)
        elif key > root.key:
            root.right = self.__delete(root.right, key)
        else:
            if not root.left or not root.right:
                node = root.left or root.right
                root = None
                return node

            node = self.__min_child(root.right)
            root.key = node.key
            root.right = self.__delete(root.right, node.key) 
        
        return root


    def __min_child(self, root):
        node = root

        while node.left:
            node = node.left
        
        return node

    def __inorder(self, root):
        if not root:
            return

        yield from self.__inorder(root.left)
        yield (root.key, root.val)
        yield from self.__inorder(root.right)

    # operators

    def __setitem__(self, key, val):
        self.insert(key, val)

    def __contains__(self, key):
        if self.search(key):
            return True
        return False

    def __getitem__(self, key):
        return self.search(key)

    def __delitem__(self,key):
        self.delete(key)

    def __iter__(self):
        yield from self.__inorder(self.root)