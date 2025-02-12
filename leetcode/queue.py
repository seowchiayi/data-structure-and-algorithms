from typing import List
import collections

def buildings_with_ocean_view(heights: List[int]) -> List[int]:
    # without queue
    # max_height = -1
    # res = []
    # for i in range(len(heights) - 1, -1, -1):
    #     if heights[i] > max_height:
    #         res.append(i)
    #     last_height = heights[i]
    #     max_height = max(last_height, max_height)
    
    # res.sort()
    # return res

    # with queue
    res = collections.deque([])
    max_height = -1

    for i in range(len(heights) -1, -1, -1):
        if heights[i] > max_height: # -> O(1) comparison
            res.appendleft(i) 
            max_height = heights[i] # -> O(1) update

    return list(res)

if __name__ == "__main__":
    print(buildings_with_ocean_view(heights=[4,2,3,1]))
    print(buildings_with_ocean_view(heights=[1,3,2,4]))