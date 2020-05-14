def is_balanced(tree_root):
    '''
    Function to test if a tree is "superbalanced".
    A tree is superbalanced if the depth of leaves differ by at most 1.

    Solution: Traverse the tree with DFS and each time we find a leaf,
    compare it's depth with the max depth so far.

    Time Complexity: O(N)
    Space Complexity: O(N)
    '''
    if tree_root is None:
        return True

    max_depth = -1
    
    # (node, depth)
    stack = [(tree_root, 0)]
    
    while len(stack):
        node, depth = stack.pop() 

        if (not node.left) and (not node.right):
            # if its the first leaf we've seen
            if max_depth == -1:
                max_depth = depth
            
            else:
                if abs(max_depth - depth) > 1:
                    return False
                    
                max_depth = max(max_depth, depth)
        
        else:
            if node.left:
                stack.append((node.left, depth+1))
            
            if node.right:
                stack.append((node.right, depth+1))
    
    return True


    def is_balanced(tree_root):
        '''
        This is the official solution to the above problem,
        by Interview Cake.
        '''

        # A tree with no nodes is superbalanced, since there are no leaves!
        if tree_root is None:
            return True

        # We short-circuit as soon as we find more than 2
        depths = []

        # We'll treat this list as a stack that will store tuples of (node, depth)
        nodes = []
        nodes.append((tree_root, 0))

        while len(nodes):
            # Pop a node and its depth from the top of our stack
            node, depth = nodes.pop()

            # Case: we found a leaf
            if (not node.left) and (not node.right):
                # We only care if it's a new depth
                if depth not in depths:
                    depths.append(depth)

                    # Two ways we might now have an unbalanced tree:
                    #   1) more than 2 different leaf depths
                    #   2) 2 leaf depths that are more than 1 apart
                    if ((len(depths) > 2) or
                            (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                        return False
            else:
                # Case: this isn't a leaf - keep stepping down
                if node.left:
                    nodes.append((node.left, depth + 1))
                if node.right:
                    nodes.append((node.right, depth + 1))

    return True