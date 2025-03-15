import collections
from typing import List

class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise, initializes a single integer equal to value.
        """
        if value is None:
            self.data = []
        elif isinstance(value, int):
            self.data = value
        else:
            self.data = [NestedInteger(v) for v in value]  # Convert each element into a NestedInteger

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.data, int)

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and add a nested integer elem to it.
        """
        if self.isInteger():
            self.data = [NestedInteger(self.data)]  # Convert existing int to list
        self.data.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        """
        self.data = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer.
        Return None if this NestedInteger holds a nested list.
        """
        return self.data if self.isInteger() else None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list.
        Return None if this NestedInteger holds a single integer.
        """
        return self.data if not self.isInteger() else None


def nested_list_weight_sum(nestedList: List[NestedInteger]):
    depth = 1
    res = 0

    queue = collections.deque(nestedList)

    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()

            if cur.isInteger():
                res += cur.getInteger() * depth
            else:
                # use .extend instead of .append to spread out elements within list and put elements in queue
                queue.extend(cur.getList()) 
        depth += 1
    
    return res

def diagonal_traverse(mat):
    res = []
    i, j = 0, 0
    going_up = True
    while len(res) != len(mat) * len(mat[0]):
        if going_up:
            while i >= 0 and j < len(mat[0]):
                res.append(mat[i][j])
                i -= 1
                j += 1
                # print(i, j)
            if j == len(mat[0]):
                i += 2
                j -= 1
            else:
                i += 1
            going_up = False
        else:
            while i < len(mat) and j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1
            
            if i == len(mat):
                i -= 1
                j += 2
            else:
                j += 1
            going_up = True


    return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order_traversal_of_binary_tree(root):
    if not root:
        return []
    queue = collections.deque([(0, 0, root)])
    res = []
    min_j = float('inf')
    max_j = float('-inf')
    column_items = collections.defaultdict(list)
    while queue:
        i, j, node = queue.popleft()

        column_items[j].append((node.val, i))

        min_j = min(j, min_j)
        max_j = max(j, max_j)

        if node.left:
            queue.append((i + 1, j - 1, node.left))
        if node.right:
            queue.append((i + 1, j + 1, node.right))

    for j in range(min_j, max_j + 1):
        items = column_items[j]

        items.sort(key=lambda x:(x[1], x[0]))

        items = [val for val, _ in items]

        res.append(items)

    return res


def even_odd_tree(root):
    queue = collections.deque([(root, 0)]) 
    seen = {}
    while queue:
        node, level = queue.pop()
        if level == 0:
            if root.val != node.val:
                return False
            if not node.val % 2 == 0:
                return False
        elif level not in seen:
            if level % 2 == 0:
                if node.val % 2 == 0:
                    return False
                seen[level] = node.val
            elif not level % 2 == 0:
                if not node.val % 2 == 0:
                    return False
                seen[level] = node.val
        elif level in seen:
            if level % 2 == 0:
                if node.val % 2 == 0:
                    return False
                if seen[level] >= node.val:
                    return False
                seen[level] = node.val
            elif not level % 2 == 0:
                if not node.val % 2 == 0:
                    return False
                if seen[level] <= node.val:
                    return False
                seen[level] = node.val

        if node.left:
            queue.appendleft((node.left, level + 1))
        
        if node.right:
            queue.appendleft((node.right, level + 1))

    return True

def closest_nodes_queries_in_a_binary_search_tree(root, queries):
    # in order traversal bfs
    queue = collections.deque([])
    res = []
    current = root
    while current or queue:
        while current:
            queue.append(current)
            current = current.left
        current = queue.pop()
        res.append(current.val)

        current = current.right

    l = 0
    r = len(res) - 1
    d = collections.defaultdict(list)
    final_res = []

    for target in queries:
        if target not in d:
            while l <= r:
                m = (l + r) // 2
                if res[m] > target:
                    r = m - 1
                elif res[m] < target:
                    l = m + 1
                elif res[m] == target:
                    d[target].append(target)
                    d[target].append(target)
                    final_res.append([target, target])
                    break

            if d[target] == []:
                min_val = res[r] if r >= 0 else -1
                max_val = res[l] if l < len(res) else -1
                d[target].append(min_val)
                d[target].append(max_val)
                final_res.append([min_val, max_val])

            l = 0
            r = len(res) - 1
        else:
            final_res.append(d[target])

    return final_res
                
if __name__ == "__main__":
    # a = NestedInteger([1,1])
    # b = NestedInteger(2)
    # c = NestedInteger([1,1])
    # print(nested_list_weight_sum(nestedList=[a,b,c]))
    #a = NestedInteger(1)
    #b = NestedInteger([4, [6]])
    #print(nested_list_weight_sum(nestedList=[a, b]))
    #print(diagonal_traverse(mat=[[1,2,3],[4,5,6],[7,8,9]]))

    # root = TreeNode(3)
    # a = TreeNode(9)
    # b = TreeNode(20)
    # c = TreeNode(15)
    # d = TreeNode(7)


    # root.left = a
    # root.right = b
    # b.left = c
    # b.right = d
    # [[9], [3, 15], [20], [7]]
    # print(vertical_order_traversal_of_binary_tree(root))

    # root = TreeNode(1)
    # a = TreeNode(2)
    # b = TreeNode(3)
    # c = TreeNode(4)
    # d = TreeNode(6)
    # e = TreeNode(5)
    # f = TreeNode(7)


    # root.left = a
    # root.right = b
    # a.left = c
    # a.right = d
    # b.left = e
    # b.right = f
    # [[4], [2], [1, 5, 6], [3], [7]]
    # print(vertical_order_traversal_of_binary_tree(root))

    # root = TreeNode(3)
    # a = TreeNode(1)
    # b = TreeNode(4)
    # c = TreeNode(0)
    # d = TreeNode(2)
    # e = TreeNode(2)

    # root.left = a
    # root.right = b
    # a.left = c
    # a.right = d
    # b.left = e
    # [[0],[1],[3,2,2],[4]]
    # print(vertical_order_traversal_of_binary_tree(root))

    # root = TreeNode(1)
    # a = TreeNode(2)
    # b = TreeNode(3)
    # c = TreeNode(4)
    # d = TreeNode(5)
    # e = TreeNode(6)
    # f = TreeNode(7)

    # root.left = a
    # root.right = b
    # a.left = c
    # a.right = d
    # b.left = e
    # [[4],[2],[1,5,6],[3],[7]]
    # print(vertical_order_traversal_of_binary_tree(root))

    # root = TreeNode(1)
    # a = TreeNode(10)
    # b = TreeNode(4)
    # c = TreeNode(3)
    # d = TreeNode(7)
    # e = TreeNode(9)
    # f = TreeNode(12)
    # g = TreeNode(8)
    # h = TreeNode(6)
    # i = TreeNode(2)

    # root.left = a
    # root.right = b
    # a.left = c
    # c.left = f
    # c.right = g
    # b.left = d
    # b.right = e
    # d.left = h
    # e.right = i
    
    # print(even_odd_tree(root))

    # root = TreeNode(2)
    # a = TreeNode(12)
    # b = TreeNode(8)
    # c = TreeNode(5)
    # d = TreeNode(9)
    # e = TreeNode(18)
    # f = TreeNode(16)

    # root.left = a
    # root.right = b
    # a.left = c
    # a.right = d
    # c.left = e
    # c.right = f
    
    # print(even_odd_tree(root))

    root = TreeNode(6)
    a = TreeNode(2)
    b = TreeNode(13)
    c = TreeNode(1)
    d = TreeNode(4)
    e = TreeNode(9)
    f = TreeNode(15)
    g = TreeNode(14)

    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f
    f.left = g
    
    print(closest_nodes_queries_in_a_binary_search_tree(root, queries=[2, 5, 16]))

    root = TreeNode(4)
    a = TreeNode(9)

    root.right = a
    

    print(closest_nodes_queries_in_a_binary_search_tree(root, queries=[3]))

    root = TreeNode(16)
    a = TreeNode(14)
    b = TreeNode(4)
    c = TreeNode(15)
    d = TreeNode(1)

    root.left = a
    a.left = b
    a.right = c
    b.left = d

    print(closest_nodes_queries_in_a_binary_search_tree(root, queries=[10, 6, 2, 9]))

    root = TreeNode(9)
    a = TreeNode(6)
    b = TreeNode(14)
    c = TreeNode(13)
    d = TreeNode(20)
    e = TreeNode(12)

    root.left = a
    root.right = b
    b.left = c
    b.right = d
    c.left = e

    print(closest_nodes_queries_in_a_binary_search_tree(root, queries=[19,10,9,17,19,6,10,19,13,6]))