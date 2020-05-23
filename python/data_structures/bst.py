class BinarySearchTree:
    """
    Binary Search Tree implementation using only iterative methods

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
    
    TODO: turn inorder() into generator
    
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
        node = self.root
        while node and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node.val if node else None

    def insert(self, key, val):
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

    def delete(self, key):
        if not self.root or key == self.root.key:
            return self.__delete_root(self.root)

        node = self.root
        while True:
            if key < node.key:
                if not node.left or key == node.left.key:
                    node.left = self.__delete_root(node.left)
                    break
                node = node.left
            else:
                if not node.right or key == node.right.key:
                    node.right = self.__delete_root(node.right)
                    break
                node = node.right

        return self.root



    def __delete_root(self, root):
        if not root:
            return None

        if not root.right:
            return root.left
        
        node = root.right
        while node.left:
            node = node.left
        
        node.left = root.left
        return root.right


    def inorder(self, out=None):   
        if not out:
            out = []

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