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
    queue = collections.deque([(0, root)])
    res = []
    column_items = collections.defaultdict(list)
    min_x = float('inf')
    max_x = float('-inf')
    while queue:
        x, node = queue.pop()
        column_items[x].append(node.val)
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        if node.left:
            queue.append((x - 1, node.left))
        if node.right:
            queue.append((x + 1, node.right))
    
    
    for i in range(min_x, max_x + 1):
        if len(column_items[i]) > 1:
            sort = column_items[i].sorted()
            res.append(sort)
        else:
            res.append(column_items[i])
    
    return res



if __name__ == "__main__":
    # a = NestedInteger([1,1])
    # b = NestedInteger(2)
    # c = NestedInteger([1,1])
    # print(nested_list_weight_sum(nestedList=[a,b,c]))
    a = NestedInteger(1)
    b = NestedInteger([4, [6]])
    #print(nested_list_weight_sum(nestedList=[a, b]))
    print(diagonal_traverse(mat=[[1,2,3],[4,5,6],[7,8,9]]))

    root = TreeNode(3)
    a = TreeNode(9)
    b = TreeNode(20)
    c = TreeNode(15)
    d = TreeNode(7)


    root.left = a
    root.right = b
    b.left = c
    b.right = d
    # [[9], [3, 15], [20], [7]]
    print(vertical_order_traversal_of_binary_tree(root))

    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(6)
    e = TreeNode(5)
    f = TreeNode(7)


    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f
    # [[4], [2], [1, 5, 6], [3], [7]]
    print(vertical_order_traversal_of_binary_tree(root))

    root = TreeNode(3)
    a = TreeNode(1)
    b = TreeNode(4)
    c = TreeNode(0)
    d = TreeNode(2)
    e = TreeNode(2)

    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    # [[0],[1],[3,2,2],[4]]
    print(vertical_order_traversal_of_binary_tree(root))

    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)
    f = TreeNode(7)

    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    # [[4],[2],[1,5,6],[3],[7]]
    print(vertical_order_traversal_of_binary_tree(root))


    