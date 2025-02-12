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

if __name__ == "__main__":
    instructions = ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    input = [[[1,3]],[],[],[],[],[]]
    res = []
    for instruction in instructions:
        if instruction == "Solution":
            S = Solution(input[0][0])
            res.append(None)
        else:
            num = S.pickIndex()
            res.append(num)
    print(res)