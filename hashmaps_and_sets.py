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


if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(majorityElement(nums))
    print(two_sum([2,7,11,15], 9))