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


# def binary_tree_vertical_order_traversal(root):
#     if not root:
#         return []
#     column_items = collections.defaultdict(list)

#     queue = collections.deque([(0, root)])
#     min_x = float('inf')
#     max_x = float('-inf')
#     res = []

#     while queue:
#         x, node = queue.popleft()
#         column_items[x].append(node.val)
#         min_x = min(min_x, x)
#         max_x = max(max_x, x)

#         if node.left:
#             queue.append((x - 1, node.left))
#         if node.right:
#             queue.append((x + 1, node.right))
    
#     for level in range(min_x, max_x + 1):
#         res.append(column_items[level])
    
#     return res


def binary_tree_vertical_order_traversal(root):
    if not root:
        return
    queue = collections.deque([(0, root)])
    column_items = collections.defaultdict(list)
    min_x = float('inf')
    max_x = float('-inf')
    x = 0
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
    for col in range(min_x, max_x + 1):
        res.append(column_items[col])
    return res

class Solution():
    def __init__(self):
        pass
    def dfs(self, node):
        if node:
            node = self.stack.pop()
            print(node.val)
            if node.left:
                self.stack.append(node.left)
                self.dfs(node.left)
            if node.right:
                self.stack.append(node.right)
                self.dfs(node.right)
    def diameter_of_binary_tree(self, root):
        largest_diameter = [0]

        def height(root):
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            diameter = left_height + right_height
            largest_diameter[0] = max(largest_diameter[0], diameter)

            return 1 + max(left_height, right_height)
    
        height(root)
        return largest_diameter[0]

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    # The functions get and put must each run in O(1) average time complexity.
    # We can't use hashmap because we wouldn't be able to know when was the most recently added key 
    # While we could add timestamp, popping might end up requiring O(n)
    # To get/put in O(1) we can either - Ordered Dictionary/Doubly linked list

    def __init__(self, capacity: int):
        self.capacity = capacity

        # map from each key to the node that represents it in our cache
        self.node_map = {}

        # placeholder for head and tail of linked list so we can access it anytime
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        # we are using doubly linked list so we need to link both head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int):
        if key in self.node_map:
            node = self.node_map[key]
            
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1
    def put(self, key: int, value: int):
        if key in self.node_map:
            old_node = self.node_map[key]
            self._remove(old_node)

        node = ListNode(key, value)
        self.node_map[key] = node
        self._add(node)

        if len(self.node_map) > self.capacity:
            node_to_delete = self.head.next
            self._remove(node_to_delete)
            del self.node_map[node_to_delete.key]
    
    def _add(self, node):
        # we want to add node to the end because whenever we want to add it means it is most recently used node
        prev_end = self.tail.prev
        prev_end.next = node
        node.next = self.tail

        self.tail.prev = node
    
    def _remove(self, node):
        # given a node, remove from linked list
        node.prev.next = node.next
        node.prev.prev = node.prev

# class SinglyNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#     def __str__(self):
#         return str(self.val)
    
#     # Traverse the list - O(n)
# class Traverse:
#     def __init__(self):
#         pass
#     def traverse_the_list(self, head: SinglyNode):
#         curr = head
#         while curr:
#             print(curr)
#             curr = curr.next
#     def display_the_list(self, head: SinglyNode):
#         elements = []
#         curr = head
#         while curr:
#             elements.append(str(curr.val))
#             curr = curr.next
#         return " -> ".join(elements)
#     def search(self, head, val):
#         curr = head
#         while curr:
#             if curr.val == val:
#                 return True
#             curr = curr.next
#         return False

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.val)

class Traverse:
    def display_the_list(self, head: DoublyNode):
        elements = []
        curr = head
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        return " <-> ".join(elements)
    def insert_at_beginning(self, head: DoublyNode, tail: DoublyNode, val):
        new_node = DoublyNode(val, head, None)
        head.prev = new_node
        head.next = tail

        return new_node, tail



# if __name__ == "__main__":
    # head = SinglyNode(1)
    # a = SinglyNode(3)
    # b = SinglyNode(4)
    # c = SinglyNode(7)

    # head.next = a
    # a.next = b
    # b.next = c

    # t = Traverse()
    # print(t.display_the_list(head))
    # print(t.search(head, 4))

    # head = tail = DoublyNode(1)
    # a = DoublyNode(3)
    # b = DoublyNode(4)
    # c = DoublyNode(7)

    # head.next = a
    # tail.prev = c
    # a.prev = head
    # a.next = b
    # b.prev = a
    # b.next = c
    # c.prev = b
    # c.next = tail

    # t = Traverse()
    
    # new_node, tail = t.insert_at_beginning(head, tail, 3)
    # print(t.display_the_list(new_node))
    



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

    # root = TreeNode(3)
    # a = TreeNode(9)
    # b = TreeNode(20)
    # c = TreeNode(15)
    # d = TreeNode(7)

    # root.left = a
    # root.right = b
    # b.left = c
    # b.right = d

    #queue = collections.deque([root])
    #bfs_recursion(queue)
    # print(binary_tree_vertical_order_traversal(root))

    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(10)
    e = TreeNode(9)
    f = TreeNode(11)
    g = TreeNode(5)
    h = TreeNode(6)


    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f
    c.right = g
    g.right = h

    print(binary_tree_vertical_order_traversal(root))

    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)

    root.left = a
    root.right = b
    a.left = c
    a.right = d

    S = Solution()
    print(S.diameter_of_binary_tree(root))

    

    