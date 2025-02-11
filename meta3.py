from typing import List, Optional
import heapq
import collections
# Practice recursion with reversing singly linked list
class SinglyLinkedList():
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

def reverse(node: SinglyLinkedList):
    # Time: O(n) -> n is the number of nodes in the linkedin
    # Space: O(n) -> 
    if not node:
        return
    
    reverse(node.next)
    print(node.val)

def subset(nums: List[int]):
    res, sol = [], []
    def backtrack(i):
        if i == len(nums):
            print(sol[:])
            res.append(sol[:]) # we want res.append(sol[:]) instead of res.append(sol) because we want the snapshot of sol not just the reference of sol
            return
        
        # Don't pick nums[i] (go left)
        backtrack(i + 1)
        # Pick nums[i] (go right)
        sol.append(nums[i])
        backtrack(i + 1)
        sol.pop()
    
    backtrack(0)
    return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def dfs(self, node: Optional[TreeNode], low: int, high: int):
        # Time: O(n) -> worst case scenario we might have to traverse every node in the tree
        # Space: O(n) -> even though we are not defining extra space for storage, we have implicit space used by the recursive stack
        if not node:
            return 0
        if low <= node.val <= high:
            self.sum += node.val
        if low < node.val:
            self.dfs(node.left, low, high)
        if high > node.val:
            self.dfs(node.right, low, high)
        
    # recursive method        
    def range_sum_of_bst(self, root: Optional[TreeNode], low: int, high: int):
        self.dfs(root, low, high)
        return self.sum
    
    # iterative method
    def range_sum_of_bst_iterative(self, root: Optional[TreeNode], low: int, high: int):
        stack = [root]
        sum = 0

        while stack:
            node = stack.pop()

            if node:
                if low <= node.val <= high:
                    sum += node.val
                if low < node.val:
                    stack.append(node.left)
                if high > node.val:
                    stack.append(node.right)
        return sum

def k_closest_points_to_origin(points: List[List[int]], k: int):
    heap = []
    
    for point in points:
        if len(heap) < k:
            heapq.heappush(heap, (-((point[0]**2) + (point[1]**2)), point[0], point[1]))
        else:
            heapq.heappush(heap, (-((point[0]**2) + (point[1]**2)), point[0], point[1]))
            heapq.heappop(heap)

    return [[item[1], item[2]] for item in heap]

def continuous_subarray_sum(nums: List[int], k: int):
    remainder = {0: -1}
    total = 0
    for i, n in enumerate(nums):
        total += n
        r = total % k
        if r not in remainder:
            remainder[r] = i
        elif i - remainder[r] > 1: # ensures subarray has at least two elements
            return True
        
    return False

def pow(base, power):
    # if n > 0:
    #     i = 0
    #     sum = 1
    #     while i < n:
    #         sum *= x
    #         i += 1
    # else:
    #     i = 0
    #     sum = 1
    #     while i < (-n):
    #         sum /= x
    #         i += 1

    # return sum
    # for this (base if power % 2 else 1) - if power is odd multiply by base, if not multiply by 1
    def fast_pow(base, power):
        print(memo)
        if power in memo:
            
            print("if power in memo")
            print(memo)
            print(power)
            return memo[power]
        if power == 0:
            print("if power == 0")
            return 1
        elif power == 1:
            print("elif power == 1")
            return base
        memo[power] = fast_pow(base, power // 2) * fast_pow(base, power // 2) * (base if power % 2 else 1)
        print("ended")
        return memo[power]

    is_neg = power < 0
    power = abs(power)
    memo = {}
    res = fast_pow(base, power)

    return 1/res if is_neg else res

def merge_intervals(intervals: List[List[int]]):
    res = []
    intervals.sort()
    for interval in intervals:
        if len(res) > 0:
            if res[-1][1] >= interval[0] and res[-1][1] <= interval[1]:
                res[-1] = ([res[-1][0], interval[1]])
            elif res[-1][1] >= interval[0] and res[-1][1] >= interval[1]:
                continue
            else:
                res.append(interval)

        else:
            res.append(interval)

    return res

def find_first_and_last_position_of_element_in_sorted_array(nums, target):
    # res = []
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         res.append(i)
        
    # if len(res) == 0:
    #     return [-1, -1]
    # else:
    #     return [res[0], res[-1]]
    
    # use binary search for Log n time complexity
    l = 0
    r = len(nums)
    m = (l + r) // 2

    res = []
    # leftBias = True (we are looking for left most index for target), leftBias = False (we are looking for right most index for target)
    
def binary_tree_right_side_view(root: Optional[TreeNode]):
    if not root:
        return []
    
    # BFS so we are using queue
    queue = collections.deque([root])
    res = []

    while queue:
        level_length = len(queue)

        for i in range(level_length):
            print(f"start: level length: {level_length} {i}")
            for item in queue:
                print(item.val)
            node = queue.popleft()
            if i == level_length - 1:
                res.append(node.val)
                print("res")
                print(res)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
    return res



if __name__ == "__main__":
    # head = SinglyLinkedList(1)
    # A = SinglyLinkedList(2)
    # B = SinglyLinkedList(3)

    # head.next = A
    # A.next = B
    # Debug this function
    #reverse(head)
    #print(subset(nums = [1, 2, 3]))
    # lst = [10,5,15,3,7,None,18]
    # c = TreeNode(val=3, left=None, right=None)
    # d = TreeNode(val=7, left=None, right=None)
    # e = TreeNode(val=18, left=None, right=None)
    # a = TreeNode(val=5, left=c, right=d)
    # b = TreeNode(val=15, left=None, right=e)
    # root = TreeNode(val=10, left=a, right=b)

    # S = Solution()

    #print(S.range_sum_of_bst(root=root, low=7, high=15))
    #print(S.range_sum_of_bst_iterative(root=root, low=7, high=15))
    #print(k_closest_points_to_origin(points=[[1,3],[-2,2]], k=1))
    print(continuous_subarray_sum(nums=[1, 2, 3, 4], k=6))
    #print(continuous_subarray_sum(nums=[23,2,4,6,7], k=6))
    #print(continuous_subarray_sum(nums=[5,0,0,0], k=3))
    #print(continuous_subarray_sum(nums=[1,2,3], k=5))
    #print(pow(2, 5))
    #print(pow(2, 10))
    #print(pow(2, -200000000))
    #print(merge_intervals(intervals=[[1,3],[2,6],[8,10],[15,18]]))
    #print(merge_intervals(intervals=[[1,4],[0,4]]))
    #print(find_first_and_last_position_of_element_in_sorted_array(nums=[5,7,7,8,8,10], target=8))
    
    # e = TreeNode(4)
    # d = TreeNode(3)
    # c = TreeNode(5)
    # b = TreeNode(2)

    # root = TreeNode(1, b, d)
    # b.right = c
    # b.left = None
    # d.right = e
    # d.left = None

    # root = TreeNode(1)
    # a = TreeNode(2)
    # b = TreeNode(3)
    # c = TreeNode(4)
    # d = TreeNode(5)


    # root.left = a
    # root.right = b
    # a.left = c
    # c.left = d

    # print(binary_tree_right_side_view(root))
