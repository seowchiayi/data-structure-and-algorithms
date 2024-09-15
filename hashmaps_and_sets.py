from typing import List
from collections import Counter, defaultdict


def majorityElement(nums: List[int]) -> int:
    d = defaultdict(int)
    d = Counter(nums)
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_d[0][0]


if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(majorityElement(nums))