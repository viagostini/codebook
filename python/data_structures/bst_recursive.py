class BinarySearchTree:
    class TreeNode:
        def __init__(self, key, val, parent=None):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.parent = parent
    
    def __init__(self):
        self.__root = None
        self.__size = 0
    
    def size(self):
        return self.__size
    
    def empty(self):
        return self.__size == 0

    def search(self, key):
        assert not self.empty()
        return self.__search(self.__root, key)

    def __search(self, root, key):
        if not root:
            return None  
        if key == root.key:
            return root.val
        if key < root.key:
            return self.__search(root.left, key)
        return self.__search(root.right, key)

    def insert(self, key, val):
        self.__size += 1
        self.__root = self.__insert(self.__root, key, val)

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

    def inorder(self):
        return self.__inorder(self.__root)

    def __inorder(self, root):
        if not root:
            return []

        left = self.__inorder(root.left)
        right = self.__inorder(root.right)

        return left + [(root.key, root.val)] + right