import collections
# dfs algorithm with trees
class TreeNode:
    def __init__(self, val=None, left=None, right=None, queue=None, stack=None):
        self.val = val
        self.left = left
        self.right = right
        self.queue = queue
        self.stack = stack

    def dfs_recursion_without_data_structure(self, node):
        if not node:
            return
        if node:
            print(node.val)
            if node.left:
                self.dfs_recursion_without_data_structure(node.left)
            if node.right:
                self.dfs_recursion_without_data_structure(node.right)
    
    def dfs_post_order_iterative_with_stack(self, node):
        while self.stack:
            node = self.stack.pop()
            print(node.val)
            if node.right:
                self.stack.append(node.right)
            if node.left:
                self.stack.append(node.left)
    
    def dfs_post_order_iterative_with_queue(self, node):
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            if node.right:
                queue.appendleft(node.right)
            if node.left:
                queue.appendleft(node.left)
    
    def dfs_in_order_iterative_with_stack(self, node):
        stack = []
        result = []
        current = root

        while current or stack:

            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(node.val)

            current = current.right
        
        return result


if __name__ == "__main__":
    #       1
    #      / \
    #     2  3
    #    /
    #   4
    #  /
    # 5
    root = TreeNode(val=1)
    a = TreeNode(val=2)
    b = TreeNode(val=3)
    c = TreeNode(val=4)
    d = TreeNode(val=5)

    root.left = a
    root.right = b
    a.left = c
    c.left = d
    S = TreeNode()
    # expected to print 1, 2, 4, 5, 3 
    #S.dfs_recursion_without_data_structure(root)
    S.stack = [root]
    #S.dfs_post_order_iterative_with_stack(root)
    S.queue = collections.deque([root])
    #S.dfs_post_order_iterative_with_queue(root)
    root = TreeNode(4)
    a = TreeNode(2)
    b = TreeNode(5)
    c = TreeNode(1)
    d = TreeNode(3)

    root.left = a
    root.right = b
    a.left = c
    a.right = d
    print(S.dfs_in_order_iterative_with_queue(root))

    root = TreeNode(-1)
    b = TreeNode(1)
    c = TreeNode(9)

    root.right = b
    b.right = c

    print(S.dfs_in_order_iterative_with_queue(root))

