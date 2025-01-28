from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_a_binary_tree(root: Optional[TreeNode]) -> int:
    # Time: O(n) - number of nodes in the tree
    # Spapce: O(n) - number of nodes in the tree
    largest_diameter = [0]

    def height(root):
        if not root:
            return 0
        
        left_height = height(root.left)
        right_height = height(root.right)

        diameter = left_height + right_height
        largest_diameter[0] = max(largest_diameter[0], diameter)

        # return height
        return 1 + max(left_height, right_height)
    
    height(root)
    return largest_diameter[0]


def simplify_path(path):
    # Time: O(n) - we go through every items in path
    # Space: O(n) - we might need to store every items in the path
    items = path.split("/")
    stack = []

    if len(items) == 1 and items[0] == "..":
        return "/"
            
    for idx in range(len(items)):
        if items[idx] == "" or items[idx] == ".":
            continue
        if items[idx] == "..":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(items[idx])
    
    return "/" + "/".join(stack)

def merge_sorted_array(nums1, m, nums2, n):
    # Time: O(n+m)
    # Space: O(1)
    x = m - 1
    y = n - 1

    for z in range(m + n - 1, -1, -1):
        if x < 0:
            nums1[z] = nums2[y]
            y -= 1
        elif y < 0:
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x -= 1
        else:
            nums1[z] = nums2[y]
            y -= 1
    
    print(nums1)

def valid_palindrome(s: str):
    # Time: O(n)
    # Space: O(1)
    l = 0
    r = len(s) - 1
    
    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        
        l += 1 
        r -= 1
    
    return True

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    # we are interacting with 2 data structures here for this LC problem 
    # 1. self.cache (dictionary) 2. self.left, self.right (doubly linked list)
    # A node is self.cache[key], Node(key, value) -> looks like this when printed <__main__.Node object at 0x102df7ec0>

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node (node is the pointer for both the key, value pair)

        #left = least recently used node, right = most recently used node
        self.left, self.right = Node(0, 0), Node(0, 0)
        # initially we want lru to be connect to mru because when we put in new node we want it to be in the middle of lru and mru, we can do this with pointers
        self.left.next, self.right.prev = self.right, self.left
        
    # helper function 1 for our linked list
    # remove node from the left most side of the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # helper function 2 for our linked list
    # insert node on the right most side of the linkedin list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        # everytime we get a node from the cache, we want to move the node to the mru in the list
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

def maximum_swap(num: int):

    #brute force method O(n^2)
    # largest_num = num
    # lst = str(num)
    # c = []
    # for ch in lst:
    #     c.append(ch)
    # for i in range(len(lst)):
    #     for j in range(len(lst)):
    #         z = c.copy()
    #         if i != j:
    #             z[i] = lst[j]
    #             z[j] = lst[i]
    #             tmp_int = int("".join(z))
    #             if int(tmp_int) > int(largest_num):
    #                 largest_num = tmp_int
    # return largest_num


    # find left most smallest number to swap with rightmost largest number
    # Time: O(n) -> N = number of digits inside of num
    # Space: O(n)
    if num <= 11:
        return num
    num_as_arr = collections.deque()

    while num:
        num_as_arr.appendleft(num % 10)
        num //= 10
    
    max_seen = -1
    max_seen_at = len(num_as_arr) # we havent process the array yet

    i = len(num_as_arr) - 1

    while i >= 0:
        cur_num = num_as_arr[i]
        num_as_arr[i] = (cur_num, max_seen, max_seen_at)
        #print(num_as_arr)

        if cur_num > max_seen:
            max_seen = cur_num
            max_seen_at = i
        i -= 1
    
    i = 0

    while i < len(num_as_arr):
        cur_num, max_to_right, max_seen_at = num_as_arr[i]
        if max_to_right > cur_num:
            num_as_arr[i], num_as_arr[max_seen_at] = num_as_arr[max_seen_at], num_as_arr[i]
            
            break
        
        i += 1

    for cur_num, _, _ in num_as_arr:
        num = num * 10 + cur_num
    
    return num

def find_peak_element(nums):
    # Time: log n (required)
    # solution is conceptually wrong but accepted by leetcode for some reasons
    # n = nums.copy()
    # n.sort()
    # biggest_num = n[-1]
    
    # for i in range(len(nums)):
    #     if nums[i] == biggest_num:
    #         return i
    
    # binary tree method
    l = 0
    r = len(nums) - 1
    

    while l <= r:
        # m = l + r //2 might overflow
        m = l + ((r - 1) // 2)
        # left neighbor greater
        if m > 0 and nums[m] < nums[m - 1]:
            r = m - 1
        # right neighbor greater
        elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
            l = m + 1
        else:
            return m
        
def valid_palindrome_2(s):
    # brute force
    # l = 0
    # r = len(s) - 1
    # new_s = ""
    # while l < r:
    #     if s[l] != s[r]:
    #         new_s = s[l:r+1]
    #         break

    #     l += 1
    #     r -= 1

    # l = 1
    # r = len(new_s) - 1

    # flag = True

    # while l < r:
    #     if new_s[l] != new_s[r]:
    #         flag = False
        
    #     l += 1
    #     r -= 1

    # if flag == True:
    #     return True
    
    # flag = True
    # l = 0
    # r = len(new_s) - 1 - 1
    # while l < r:
    #     if new_s[l] != new_s[r]:
    #         flag = False
    #     l += 1
    #     r -= 1
    
            
    # return flag

    # Time: O(n)
    # Space: O(1) -> constant space allocation for l and r
    def is_palindrome(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
        
            l += 1
            r -= 1
        return True
        
    l = 0 
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return is_palindrome(s, l+1, r) or is_palindrome(s, l, r-1)
        l += 1
        r -= 1
    return True


    



    

if __name__ == "__main__":
    #print(diameter_of_a_binary_tree(root=[1,2,3,4,5]))
    #print(simplify_path(path="/home/../usr//bin/./script"))
    #print(merge_sorted_array(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
    #print(valid_palindrome(s = "A man, a plan, a canal: Panama"))
    # instructions = ["LRUCache","put","put","get","put","get","put","get","get","get"]
    # items = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    # res = []
    # l = LRUCache(items[0][0])
    # res.append(None)
    # for i in range(1, len(instructions)):
    #     if instructions[i] == "put":
    #         l.put(items[i][0], items[i][1])
    #         res.append(None)
    #     if instructions[i] == "get":
    #         r = l.get(items[i][0])
    #         res.append(r)

    # print(res)
    # print(maximum_swap(2736))
    # print(maximum_swap(9973))
    #print(find_peak_element(nums=[1, 2, 3, 1]))
    #print(find_peak_element(nums=[4, 3, 2, 1]))
    print(valid_palindrome_2("abdceeedba"))