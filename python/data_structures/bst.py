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

        node = self.__root
        while node and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node.val if node else None

    def insert(self, key, val):
        if self.empty():
            self.__root = self.TreeNode(key, val)
            self.__size += 1
            return
        
        node = self.__root
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

        self.__size += 1

    def inorder(self, out=[]):        
        node, stack = self.__root, []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                out.append((node.key, node.val))
                node = node.right
            
        return out