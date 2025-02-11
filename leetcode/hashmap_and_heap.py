import collections
import heapq

def top_k_frequent_elements(nums, k):
    d = collections.defaultdict(int)
    res = []
    heap = []
    for num in nums:
        d[num] += 1
    
    for key, val in d.items():
        heapq.heappush(heap, (-val, key))
    
    for _ in range(k):
        val, key = heapq.heappop(heap)
        res.append(key)


    return res


if __name__ == "__main__":
    print(top_k_frequent_elements(nums=[1,1,1,2,2,3], k=2))