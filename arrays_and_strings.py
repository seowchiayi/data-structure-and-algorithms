from typing import List


# recording my attempts so I can see my progress
def maxProfit(prices: List[int]) -> int:
        # first attempt
        # lowest_price = float('inf')
        # lowest_price_idx = -1
        # for i in range(len(prices)):
        #     if prices[i] < lowest_price:
        #         lowest_price = prices[i]
        #         lowest_price_idx = i
        # if lowest_price_idx == len(prices) - 1:
        #     return 0
        # highest_price = float('-inf')
        # for price in prices[lowest_price_idx + 1:]:
        #     if price > highest_price:
        #         highest_price = price
        
        # return highest_price - lowest_price

        # second attempt
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         if prices[i] < prices[j]:
        #             if prices[j] - prices[i] > max_profit:
        #                 max_profit = prices[j] - prices[i]
        # return max_profit

        # third attempt
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit

def longestCommonPrefix(strs: List[str]) -> str:
    # min_length = float('inf')
    # for s in strs:
    #     if len(s) < min_length:
    #         min_length = len(s)
    # i = 0
    # while i < min_length:
    #     for s in strs:
    #         if s[i] != strs[0][i]:
    #             return s[:i]
    #     i += 1

    # return s[:i]
    
    # second attempt
    shortest_str = min(strs, key=len)
    i = 0
    while i < len(shortest_str):
        for s in strs:
            if s[i] != shortest_str[i]:
                return s[:i]
        i += 1
    return s[:i]
    

def summaryRanges(nums: List[int]) -> List[str]:
    # i, j = 0, 0
    # res = []
    # s = ""
    # while i < len(nums) and j + 1 < len(nums):
    #     if nums[j + 1] == nums[j] + 1:
    #         print("hit")
    #         s = str(nums[i]) + "->" + str(nums[j + 1])
    #     else:
    #         if s == "":
    #             res.append(str(nums[i]))
    #         if i == len(nums) - 1:
    #             res.append(str(nums[i]))
    #         else:
    #             i = j + 1
    #             res.append(s)
    #     j += 1
        
    #return res

    # second attempt
    ans = []
    i = 0
    while i < len(nums):
        start = nums[i]
        while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
            i += 1
        if start != nums[i]:
            ans.append(str(start) + "->" + str(nums[i]))
        else:
            ans.append(str(start))
        i += 1
    return ans


def productExceptSelf(nums: List[int]) -> List[int]:
    # first attempt
    # Time: O(n^2)
    answer = []

    for i in range(len(nums)):
        total = 1
        if i != 0:
            pre = nums[:i]
            suff = nums[i + 1:]
            for k in pre:
                total *= k
            for l in suff:
                total *= l
            answer.append(total)
        
        else:
            for j in nums[i + 1: ]:
                total *= j
            answer.append(total)
    
    return answer

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    lst = []
    i = 0
    while i < len(intervals):
            if len(lst) == 0:
                lst.append(intervals[i])
                i += 1
            elif intervals[i][0] <= lst[-1][1] and intervals[i][1] >= lst[-1][1]:
                lst[-1] = [lst[-1][0], intervals[i][1]]
                i += 1
            elif intervals[i][0] <= lst[-1][1] and intervals[i][1] <= lst[-1][1]:
                lst[-1] = [lst[-1][0], lst[-1][1]]
                i += 1
            else:
                lst.append(intervals[i])
                i += 1
    return lst


def find_closest_number_to_zero(nums: List[int]):
    smallest_dist = float('inf')

    for num in nums:
        if abs(num) == abs(smallest_dist):
            if num > smallest_dist:
                smallest_dist = num

        elif abs(num) < abs(smallest_dist):
            smallest_dist = num
        
    return smallest_dist


def merge_strings_alternately(word1, word2):
    s = ""
    if len(word1) < len(word2):
        length = len(word1)
        remaining = word2[length:]
    else:
        length = len(word2)
        remaining = word1[length:]

    i = 0
    while i < length:
        s += word1[i]
        s += word2[i]
        i += 1
    
    s += remaining
    return s

def best_time_to_buy_and_sell_stock(prices: List[int]):
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    
    return max_profit


           


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    #print(maxProfit(prices))
    strs = ["flower","flow","flight"]
    #print(longestCommonPrefix(strs))
    # nums = [0,1,2,4,5,7]
    nums = [0,2,3,4,6,8,9]
    #print(summaryRanges(nums))
    #nums = [1,2,3,4]
    nums = [-1,1,0,-3,3]
    #print(productExceptSelf(nums))
    #intervals = [[1,3],[2,6],[8,10],[15,18]]
    #intervals = [[1,4],[4,5]]
    intervals = [[1,4],[0,4]]
    #print(merge(intervals))
    print(find_closest_number_to_zero([2,-1,1]))
    print(find_closest_number_to_zero([-4,-2,1,4,8]))
    print(merge_strings_alternately(word1 = "abc", word2 = "pqr"))
    print(merge_strings_alternately(word1 = "abcd", word2 = "pq"))