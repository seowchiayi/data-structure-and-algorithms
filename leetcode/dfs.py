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

    def dfs_iterative_with_stack(self, node):
        while self.stack:
            node = self.stack.pop()
            print(node.val)
            if node.right:
                self.stack.append(node.right)
            if node.left:
                self.stack.append(node.left)

    def dfs_iterative_with_queue(self, node):
        while self.queue:
            node = self.queue.pop()
            print(node.val)
            if node.right:
                self.queue.append(node.right)
            if node.left:
                self.queue.append(node.left)
            


if __name__ == "__main__":
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
    S.dfs_recursion_without_data_structure(root)
    S.stack = [root]
    S.dfs_iterative_with_stack(root)
    S.queue = collections.deque([root])
    S.dfs_iterative_with_queue(root)

