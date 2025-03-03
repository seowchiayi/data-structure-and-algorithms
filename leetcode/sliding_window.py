from typing import List

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
    
            

if __name__ == "__main__":
    print(max_consecutive_ones_iii([1,1,1,0,0,0,1,1,1,1,0], 2))
    print(max_consecutive_ones_iii([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))