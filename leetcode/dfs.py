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

    


def sum_root_to_leaf_numbers(root):
    # using 
    #       4
    #      / \
    #     9  0
    #    / \
    #   5  1
    # initialize level = 0
    # initialize sum = root.val (4) because we will always want to add root.val in any case
    # initialize dfs 
    # initialize multiplier = 10
    # add node 0, 9 to empty stack
    # sum += 4 * 10
    # pop value 9
    # sum += 4 * 10 * 10 + 9
    # divide multiplier by 10
    # add value 1, 5 to stack -> [0, 1, 5]
    # pop value 5, add value, stack = [0, 1]
    # sum += 4 * 10 * 10 * 10 + 9 + 5
    # once there is no left and right, reset sum to 495 - 5, add sum to total sum += 495
    # have 4 conditions if right if left if not right or left if not stack: reset sum to 4
    
    stack = [(root, 0)]
    total_sum = 0
    sum = root.val
    while stack:
        node, sum = stack.pop()
        sum = (sum * 10) + node.val
        if node.right:
            stack.append((node.right, sum))
        if node.left:
            stack.append((node.left, sum))
        if not node.left and not node.right:
            total_sum += sum
    
    return total_sum


def count_depth(node):
    max_level = 0
    stack = [(node, 0)]

    while stack:
        node, level = stack.pop()
        max_level = max(level, max_level)
        if node.right:
            stack.append((node.right, level + 1))
        if node.left:
            stack.append((node.left, level + 1))
    return max_level + 1

def smallest_subtree_with_all_deepest_nodes(node):
    if not node:
        return TreeNode(None)
    stack = [node]

    while stack:
        node = stack.pop()
        if not node.right:
            right_depth = 0
        if not node.left:
            left_depth = 0
        if node.right:
            right_depth = count_depth(node.right)
        if node.left:
            left_depth = count_depth(node.left)
        if right_depth > left_depth:
            stack.append(node.right)
        if right_depth < left_depth:
            stack.append(node.left)
    return node
    
def dfs_postorder(root):
    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def dfs_inorder(root):
    stack = []
    res = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        res.append(current.val)

        current = current.right
    
    return res
        
        
if __name__ == "__main__":
    #       1
    #      / \
    #     2  3
    #    /
    #   4
    #  /
    # 5
    # root = TreeNode(val=1)
    # a = TreeNode(val=2)
    # b = TreeNode(val=3)
    # c = TreeNode(val=4)
    # d = TreeNode(val=5)

    # root.left = a
    # root.right = b
    # a.left = c
    # c.left = d
    # S = TreeNode()
    # expected to print 1, 2, 4, 5, 3 
    #S.dfs_recursion_without_data_structure(root)
    #S.stack = [root]
    #S.dfs_post_order_iterative_with_stack(root)
    #S.queue = collections.deque([root])
    #S.dfs_post_order_iterative_with_queue(root)
    # root = TreeNode(4)
    # a = TreeNode(2)
    # b = TreeNode(5)
    # c = TreeNode(1)
    # d = TreeNode(3)

    # root.left = a
    # root.right = b
    # a.left = c
    # a.right = d
    # print(S.dfs_in_order_iterative_with_queue(root))

    # root = TreeNode(-1)
    # b = TreeNode(1)
    # c = TreeNode(9)

    # root.right = b
    # b.right = c

    # print(S.dfs_in_order_iterative_with_queue(root))
    # root = TreeNode(3)
    # a = TreeNode(5)
    # b = TreeNode(1)
    # c = TreeNode(6)
    # d = TreeNode(2)
    # e = TreeNode(0)
    # f = TreeNode(8)
    # g = TreeNode(7)
    # h = TreeNode(4)

    # root.left = a
    # root.right = b
    # a.left = c
    # a.right = d
    # d.left = g
    # d.right = h
    # b.left = e
    # b.right = f

    # smallest_node = smallest_subtree_with_all_deepest_nodes(root)
    # print(smallest_node.val)

    # root = TreeNode(0)
    # a = TreeNode(1)
    # b = TreeNode(3)
    # c = TreeNode(2)

    # root.left = a
    # root.right = b
    # a.right = c

    # smallest_node = smallest_subtree_with_all_deepest_nodes(root)
    # print(smallest_node.val)

    # root = TreeNode(0)
    # a = TreeNode(1)
    # b = TreeNode(3)
    # c = TreeNode(2)
    # d = TreeNode(6)
    # e = TreeNode(5)
    # f = TreeNode(4)

    # root.left = a
    # a.left = b
    # a.right = c
    # b.left = d
    # c.left = e
    # c.right = f

    # smallest_node = smallest_subtree_with_all_deepest_nodes(root)
    # print(smallest_node.val)
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)
    f = TreeNode(7)
    g = TreeNode(3)
    h = TreeNode(8)
    i = TreeNode(9)

    root.left = a
    root.right = b
    a.left = c
    a.right = d
    d.left = e
    d.right = f
    b.right = h
    h.left = i

    dfs_inorder(root)
