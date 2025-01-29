from typing import List, Optional
import heapq
import collections

class SparseVector:
    # Solution 1: good because we are only storing non zero values, bad because what if hash function sucks
    # Time: O(n) -> This solution uses hash table but lookups/insertion is taking O(n) instead of O(1)
    # Space: O(n) -> This solution uses hash table but lookups/insertion is taking O(n) instead of O(1)
    # def __init__(self, nums: List[int]):
    #     vec_d = {}
    #     for i in range(len(nums)):
    #         if nums[i] != 0:
    #             vec_d[i] = nums[i]
        
    #     self.vec_d = vec_d

    # # Return the dotProduct of two sparse vectors
    # def dotProduct(self, vec: 'SparseVector') -> int:
    #     res = 0
    #     for key in self.vec_d.keys():
    #         if key in vec.vec_d.keys():
    #             res += self.vec_d[key] * vec.vec_d[key]
        
    #     return res
    
    # Solution 2: two pointer + tuple solution

    def __init__(self, nums: List[int]):
        vec_d = []

        # Time: O(N + M)
        # Space: O(N + M)
        for i in range(len(nums)):
            if nums[i] != 0:
                vec_d.append((i, nums[i]))
        
        self.vec_d = vec_d

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        l = 0
        l1 = 0

        # Time: O(N + M)
        # Space: O(N + M)

        while l < len(self.vec_d) and l1 < len(vec.vec_d):
            if self.vec_d[l][0] > vec.vec_d[l1][0]:
                l1 += 1
            elif self.vec_d[l][0] < vec.vec_d[l1][0]:
                l += 1
            else:
                res += self.vec_d[l][1] * vec.vec_d[l1][1]
                l1 += 1
                l += 1
        
        return res

def kth_largest_element(nums: List[int], k: int):
    # 1st method: max heap
    # default python is min heap so you have to negate all values (so that biggest number is on top)
    # Time: O(N + k log N)
    # Space: O(1)

    
    # for i in range(len(nums)):
    #     nums[i] = -nums[i]
    
    # heapq.heapify(nums)

    # for _ in range(k-1):
    #     heapq.heappop(nums)
    
    # return -heapq.heappop(nums)

    # 2nd method: minheap
    # Pop operation: N log k
    # Space: O(k)
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappushpop(min_heap, num)
    return min_heap[0]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowest_common_ancestor_of_binary_tree(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
    # Use DFS to traverse around the tree
    # Time: O(n) - number of nodes in the tree
    # Space: O(h) - height of the tree
    # 3 scenarios: 
    # 1. p and q is on opposite sides of tree, we want to find the first node where they converge where they would met
    # 2. q is the descendant of p, where p is the lca 
    # 3. p is the descendant of q, q is the lca
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor_of_binary_tree(root.left, p, q)
    right = lowest_common_ancestor_of_binary_tree(root.right, p, q)

    if left and right:
        return root

    return left or right

def binary_tree_vertical_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    # For any tree questions, handle the base case first
    # Time: O(n) -> we have to travel through every node
    # Space: O(n) -> we are storing the coordinates of every node
    
    # if root is null return an empty list
    if not root:
        return []
    
    column_items = collections.defaultdict(list)

    # This is a BFS solution so we are using queue
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

def minimum_remove_to_make_valid_parentheses(s):
    stack = []
    d = collections.defaultdict(int)

    for c in s:
        if c == ")":
            if d["("] > d[")"]:
                d[")"] += 1
                stack.append(c)
        elif c == "(":
            d["("] += 1
            stack.append(c)
        elif c.isalpha() and c.islower():
            stack.append(c)
    if d["("] == d[")"]:
        return "" + "".join(stack)
    else:
        new_stack = []
        for i in stack[::-1]:
            if i == "(" and not d["("] <= d[")"]:
                d["("] -= 1
            else:
                new_stack.append(i)
        return "" + "".join(new_stack[::-1]) 




def valid_word_abbreviation(word, abbr):
    word_ptr = abbr_ptr = 0
    while word_ptr < len(word) and abbr_ptr < len(abbr):
        if abbr[abbr_ptr].isdigit():
            steps = 0

            if abbr[abbr_ptr] == "0":
                return False
            
            while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                steps = steps * 10 + int(abbr[abbr_ptr])
                abbr_ptr += 1
            word_ptr += steps
        else:
            if word[word_ptr] != abbr[abbr_ptr]:
                return False
            word_ptr += 1
            abbr_ptr += 1
    
    return word_ptr == len(word) and abbr_ptr == len(abbr)


        
        






if __name__ == "__main__":
    # Your SparseVector object will be instantiated and called as such:
    # nums1 = [1,0,0,2,3]
    # nums2 = [0,3,0,4,0]
    # v1 = SparseVector(nums1)
    # v2 = SparseVector(nums2)
    # ans = v1.dotProduct(v2)
    # print(ans)
    # print(kth_largest_element([3, 2, 1, 5, 6, 4], 2))
    # root = TreeNode([3,5,1,6,2,0,8,None,None,7,4])
    # p = TreeNode(5)
    # q = TreeNode(1)
    # print(lowest_common_ancestor_of_binary_tree(root, p, q))
    #print(binary_tree_vertical_order_traversal([3, 9, 20, None, None, 15, 7]))
    #print(minimum_remove_to_make_valid_parentheses("lee(t(c)o)de)"))
    #print(minimum_remove_to_make_valid_parentheses("))(("))
    #print(minimum_remove_to_make_valid_parentheses("(a(b(c)d)"))
    print(valid_word_abbreviation(word = "internationalization", abbr = "i12iz4n"))
    print(valid_word_abbreviation(word = "internationalization", abbr = "i5a11o1"))
    #print(valid_word_abbreviation(word = "apple", abbr = "a2e"))
    