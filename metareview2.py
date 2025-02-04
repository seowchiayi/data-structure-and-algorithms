import collections

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DoublyLinkedList:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.head, self.tail = DoublyLinkedList(-1, -1), DoublyLinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def display(self, head: DoublyLinkedList):
        elements = []
        curr = head
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        return " <-> ".join(elements)

    def get(self, key: int):
        if key not in self.node_map:
            return -1
        else:
            node = self.node_map[key]
            self._remove(node)
            self._add(node)
            return node.val
    def put(self, key: int, value: int):
        if key in self.node_map:
            old_node = self.node_map[key]
            node = DoublyLinkedList(key, value)
            self.node_map[key] = node
            self._remove(old_node)
            self._add(node)

        else:
            node = DoublyLinkedList(key, value)
            self.node_map[key] = node
            self._add(node)

        if len(self.node_map) > self.capacity:
            old_node = self.node_map[self.head.next.key]
            self._remove(old_node)
            del self.node_map[old_node.key]

    def _add(self, node: DoublyLinkedList):
        current_mru = self.tail.prev
        current_mru.next = node
        node.next = self.tail
        node.prev = current_mru

        self.tail.prev = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

class Solution:
    def __init__(self):
        self.largest_diameter = [0]

    def dfs(self, node):
        if not node:
            return 0
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        diameter = left_height  + right_height
        self.largest_diameter[0] = max(diameter, self.largest_diameter[0])

        return 1 + max(left_height, right_height)
    
    def diameter_of_bst(self, root):

        self.dfs(root)

        return self.largest_diameter[0]

def range_sum_of_vertical_order_traversal(root):
    column_items = collections.defaultdict(list)
    x = 0
    min_x = float('inf')
    max_x = float('-inf')
    queue = collections.deque([(x, root)])
    

    while queue:
        x, node = queue.popleft()
        column_items[x].append(node.val)
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        if node.left:
            queue.append((x - 1, node.left))
        if node.right:
            queue.append((x + 1, node.right))
    res = []
    for x in range(min_x, max_x + 1):
        res.append(column_items[x])
    
    return res



        
if __name__ == "__main__":
    #instructions = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    #vals = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    #instructions = ["LRUCache","put","get","put","get","get"]
    #vals = [[1],[2,1],[2],[3,2],[2],[3]]
    
    #instructions = ["LRUCache","put","put","get","put","put","get"]
    #vals = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

    # instructions = ["LRUCache","put","get","put","get","get"]
    # vals = [[1],[2,1],[2],[3,2],[2],[3]]

    # instructions = ["LRUCache","put","put","put","put","get","get"]
    # vals = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

    # res = []
    # for i in range(len(instructions)):
    #     if instructions[i] == "LRUCache":
    #         l = LRUCache(capacity=vals[i][0])
    #         res.append(None)
    #     elif instructions[i] == "put":
    #         l.put(vals[i][0], vals[i][1])
    #         res.append(None)
    #     elif instructions[i] == "get":
    #         val = l.get(vals[i][0])
    #         res.append(val)
    #     print(l.display(l.head))
    #     print(l.node_map)
    #     print(res)

    # print(res)
    # print(l.display(l.head))
    
    # root = TreeNode(1)
    # a = TreeNode(2)
    # b = TreeNode(3)
    # c = TreeNode(4)
    # d = TreeNode(5)

    # root.left = a
    # root.right = b
    # a.left = c
    # a.right = d

    # S = Solution()
    # print(S.diameter_of_bst(root))

    # root = TreeNode(1)
    # a = TreeNode(2)
    # b = TreeNode(3)
    # c = TreeNode(4)
    # d = TreeNode(10)
    # e = TreeNode(9)
    # f = TreeNode(11)
    # g = TreeNode(5)
    # h = TreeNode(6)


    # root.left = a
    # root.right = b
    # a.left = c
    # a.right = d
    # b.left = e
    # b.right = f
    # c.right = g
    # g.right = h

    # print(range_sum_of_vertical_order_traversal(root))

    s = "lee(t(c)o)de)"
    #s = "a)b(c)d"
    # "ab(c)d"
    print(minimum_remove_to_make_valid_parentheses(s))



