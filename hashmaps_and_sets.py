from typing import List
from collections import Counter, defaultdict

def majorityElement(nums: List[int]) -> int:
    d = defaultdict(int)
    d = Counter(nums)
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_d[0][0]

def two_sum(nums, target):
    # dct = {}
    # for idx in range(len(nums)):
    #     for j in range(idx + 1, len(nums)):
    #         dct[nums[idx] + nums[j]] = [idx, j]
    #     if target in dct.keys():
    #         return dct[target]
    # return dct[target]

    #algomap's solution
    h = {}
    for i in range(len(nums)):
        h[nums[i]] = i
    
    for i  in range(len(nums)):
        y = target - nums[i]

        if y in h and h[y] != i:
            return [i,  h[y]]


def valid_sudoku(board: List[List[int]]) -> bool:
    # validate each row
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[i][j]
            if item in s:
                return False
            elif item != ".":
                s.add(item)
            
    # validate each column
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[j][i]
            if item in s:
                return False
            elif item != ".":
                s.add(item)
    # validate each box
    starts = [(0, 0), (0, 3), (0, 6),
              (3, 0), (3, 3), (3, 6),
              (6, 0), (6, 3), (6, 6)]
    for item in starts:
        s = set()
        idx0, idx1 = item[0], item[1]
        for i in range(idx0, idx0 + 3):
            for j in range(idx1, idx1 + 3):
                item = board[i][j]
                if item in s:
                    return False
                elif item != ".":
                    s.add(item)
    return True


def group_anagrams(strs: List[str]) -> List[List[str]]:
    # a dict that stores list as values
    master_d = defaultdict(list)

    for s in strs:
        frequency = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            frequency[index] += 1
        master_d[tuple(frequency)].append(s)

    return list(master_d.values())


def longest_consecutive_sequence(nums: List[int]):
    s = set(nums)
    longest = 0
    for num in s:
        length = 0
        if num - 1 not in s:
            length += 1
            next_num = num + 1
            while next_num in s:
                length += 1
                next_num = next_num + 1
            
            longest = max(longest, length)
    return longest


if __name__ == "__main__":
    # nums = [2,2,1,1,1,2,2]
    # print(majorityElement(nums))
    # print(two_sum([2,7,11,15], 9))
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    print(group_anagrams(["ddddddddddg","dgggggggggg"]))
    