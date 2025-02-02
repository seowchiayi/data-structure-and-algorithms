import collections
# Reviewing concepts I am weak at - dfs with recursion, dfs with iterative loop
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def range_sum_of_bst(self, root, low, high):
        self.sum = 0
        if not root:
            return
        self.dfs(root, low, high)
        return self.sum
    
    def dfs(self, node, low, high):
        if node:
            if low <= node.val <= high:
                self.sum += node.val
            if low < node.val:
                self.dfs(node.left, low, high)
            if high > node.val:
                self.dfs(node.right, low, high)

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


            

if __name__ == "__main__":
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

    # S = Solution()
    # print(S.range_sum_of_bst(root, 7, 15))
    
    # Array of edges (directed)
    A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
    #convert_array_of_edges_to_adjacency_matrix(A)
    adjacency_list = convert_array_of_edges_to_adjacency_list(A)

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

    dfs_recursion(root)
    dfs_iterative(root)
