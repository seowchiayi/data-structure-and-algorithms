import collections
# Reviewing concepts/questions I am weak at - dfs with recursion, dfs with iterative loop, bfs with recursion, bfs with iterative loop, range sum of bst
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def __init__(self):
        self.sum = 0
    # def range_sum_of_bst(self, root, low, high):
    #     self.sum = 0
    #     if not root:
    #         return
    #     self.dfs(root, low, high)
    #     return self.sum
    
    # def dfs(self, node, low, high):
    #     if node:
    #         if low <= node.val <= high:
    #             self.sum += node.val
    #         if low < node.val:
    #             self.dfs(node.left, low, high)
    #         if high > node.val:
    #             self.dfs(node.right, low, high)
    # def range_sum_of_bst(self, root, low, high):
    #     if not root:
    #         return
    #     self.dfs(root, low, high)

    #     return self.sum
    
    def range_sum_of_bst(self, root, low, high):
        if not root:
            return
        queue = collections.deque([root])
        self.bfs(queue, low, high)

        return self.sum
    
    # def dfs(self, node, low, high):
    #     if node:
    #         if low <= node.val <= high:
    #             self.sum += node.val
    #         if low < node.val:
    #             self.dfs(node.left, low, high)
    #         if high > node.val:
    #             self.dfs(node.right, low, high)
    def bfs(self, queue, low, high):

        while queue:
            node = queue.popleft()
            if node:
                if low <= node.val <= high:
                    self.sum += node.val
                if low < node.val:
                    queue.append(node.left)
                if high > node.val:
                    queue.append(node.right)
            


# Graphs

def convert_array_of_edges_to_adjacency_matrix(A):
    n = len(A)
    # Convert array of edges to adjacency matrix
    M = []
    for i in range(n):
        M.append([0] * n)
    for u, v in A:
        #M[u][v] = 1
        # Uncomment the following line if the graph is undirected - becomes diagonal matrix, represents the opposite connection
        M[v][u] = 1

def convert_array_of_edges_to_adjacency_list(A):
    from collections import defaultdict
    D = defaultdict(list)

    for u, v in A:
        D[u].append(v)

    
    # print(D[3]) <- what is node 3 (key) connected to? (values)
    return D

def dfs_recursion(node):
    if node:
        print(node.val)
        if node.left:
            dfs_recursion(node.left)
        if node.right:
            dfs_recursion(node.right)


def dfs_iterative(node):
    stack = [node]

    while stack:
        if node:
            node = stack.pop()
            print(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def dfs_recursion_with_adjacency_lst(adjacency_lst, seen, root):
    print(root)
    for children in adjacency_lst[root]:
        if children not in seen:
            
            seen.add(children)
            dfs_recursion_with_adjacency_lst(adjacency_lst, seen, children)
            
def dfs_iterative_with_adjacency_lst(adjacency_lst, seen, stack):
    while stack:
        node = stack.pop()
        print(node)
        for children in adjacency_lst[node]:
            if children not in seen:
                seen.add(children)
                stack.append(children)

def bfs_iterative_with_adjacency_lst(adjacency_lst, seen, queue):
    while queue:
        node = queue.popleft()
        print(node)
        for children in adjacency_lst[node]:
            if children not in seen:
                seen.add(children)
                queue.append(children)

def bfs_recursion(queue):
    if queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        
        return bfs_recursion(queue)


def binary_tree_vertical_order_traversal(root):
    if not root:
        return []
    column_items = collections.defaultdict(list)

    queue = collections.deque([(0, root)])
    min_x = float('inf')
    max_x = float('-inf')
    res = []

    while queue:
        x, node = queue.popleft()
        column_items[x].append(node.val)
        min_x = min(min_x, x)
        max_x = max(max_x, x)

        if node.left:
            queue.append((x - 1, node.left))
        if node.right:
            queue.append((x + 1, node.right))
    
    for level in range(min_x, max_x + 1):
        res.append(column_items[level])
    
    return res





if __name__ == "__main__":
    root = TreeNode(10)
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(7)
    d = TreeNode(15)
    e = TreeNode(18)

    root.left = a
    root.right = d
    a.left = b
    a.right = c
    d.right = e

    S = Solution()
    print(S.range_sum_of_bst(root, 7, 15))
    
    # Array of edges (directed)
    # A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
    #convert_array_of_edges_to_adjacency_matrix(A)
    # adjacency_lst = convert_array_of_edges_to_adjacency_list(A)

    # root = TreeNode(10)
    # a = TreeNode(5)
    # b = TreeNode(3)
    # c = TreeNode(7)
    # d = TreeNode(15)
    # e = TreeNode(18)

    # root.left = a
    # root.right = d
    # a.left = b
    # a.right = c
    # d.right = e

    #dfs_recursion(root)
    #dfs_iterative(root)
    # root = 0
    # seen = set()
    # seen.add(root)

    #dfs_recursion_with_adjacency_lst(adjacency_lst, seen, root)

    # root = 0
    # seen = set()
    # stack = [root]
    # dfs_iterative_with_adjacency_lst(adjacency_lst, seen, stack)

    # source = 0
    # seen = set()
    # queue = collections.deque([source])

    # bfs_iterative_with_adjacency_lst(adjacency_lst, seen, queue)

    root = TreeNode(3)
    a = TreeNode(9)
    b = TreeNode(20)
    c = TreeNode(15)
    d = TreeNode(7)

    root.left = a
    root.right = b
    b.left = c
    b.right = d

    #queue = collections.deque([root])
    #bfs_recursion(queue)
    binary_tree_vertical_order_traversal(root)
