from typing import List
import collections

def max_consecutive_ones_iii(nums: List[int], k: int):
    # initialize 2 while loops
    # initialize sum of 1s = 0
    # initialize sum of 0s = 0
    # left_ptr_idx = 0
    # the outer while loop tracks the index of pointer < len(input)
    # the inner while loop tracks the sum of 0s <= k
    # the sum of 0s reset to 0 whenever we've converted k times of 0 to 1
    # record the biggest sum we've seen so far by adding sum of 0s and sum of 1s
    # return the biggest sum
    l = 0
    largest_sum = 0
    zero_count = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[l] == 0:
                zero_count -= 1
            l += 1
        
        largest_sum = max(largest_sum, r - l + 1)
    
    return largest_sum
    
class DataStream:

    # def __init__(self, value: int, k: int):
    #     self.value = value
    #     self.k = k
    #     self.queue = collections.deque([])

    # def consec(self, num: int) -> bool:
    #     self.queue.append(num)
        
    #     if len(self.queue) < self.k:
    #         return False
    #     elif len(self.queue) == self.k:
    #         for val in self.queue:
    #             if self.value != val:
    #                 return False
    #     elif len(self.queue) > self.k:
    #         while len(self.queue) > self.k:
    #             self.queue.popleft()
    #         for val in self.queue:
    #             if self.value != val:
    #                 return False
        
    #     return True
    
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = collections.deque([])
        self.mismatch_count = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        
        if self.value != num:
            self.mismatch_count += 1
            return False
        if len(self.queue) < self.k:
            return False
        if len(self.queue) > self.k:
            removed = self.queue.popleft()
            if self.value != removed:
                self.mismatch_count -= 1
        if self.mismatch_count > 0:
            return False
        return True

if __name__ == "__main__":
    #print(max_consecutive_ones_iii([1,1,1,0,0,0,1,1,1,1,0], 2))
    #print(max_consecutive_ones_iii([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
    instructions = ["DataStream", "consec", "consec", "consec", "consec"]
    vals = [[4, 3], [4], [4], [4], [3]]
    res = []
    # instructions = ["DataStream","consec","consec","consec","consec","consec"]
    # vals = [[1,2],[1],[2],[1],[1],[1]]

    for i in range(len(instructions)):
        if instructions[i] == "DataStream":
            c = DataStream(value=vals[i][0], k=vals[i][1])
            res.append(None)
        elif instructions[i] == "consec":
            target = vals[i][0]
            flag = c.consec(target)
            res.append(flag)

    print(res)
    

            
