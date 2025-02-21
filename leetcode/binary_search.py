from typing import List
import collections
import random

class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sum = []

        total = 0
        for weight in w:
            total += weight

            self.prefix_sum.append(total)

        self.total = total

    def pickIndex(self):
        target = random.uniform(0, self.total)
        l = 0
        r = len(self.prefix_sum)

        while l < r:
            mid = (l + r) // 2
            if self.prefix_sum[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
    
class RandomPickIndex:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    #reservoir sampling
    def pick(self, target: int) -> int:
        count = picked_index = 0

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                #random.randint(low - inclusive, high - exclusive)
                if random.randint(1, count) == count:
                    picked_index = i
        return picked_index


if __name__ == "__main__":
    # instructions = ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    # input = [[[1,3]],[],[],[],[],[]]
    # res = []
    # for instruction in instructions:
    #     if instruction == "Solution":
    #         S = Solution(input[0][0])
    #         res.append(None)
    #     else:
    #         num = S.pickIndex()
    #         res.append(num)
    # print(res)

    instructions = ["Solution", "pick", "pick", "pick"]
    input = [[[1, 2, 3, 3, 3]], [3], [1], [3]]
    res = []
    for i in range(len(instructions)):
        if instructions[i] == "Solution":
            S = RandomPickIndex(input[i][0])
            res.append(None)
        else:
            print(input[i][0])
            num = S.pick(input[i][0])
            res.append(num)
    print(res)