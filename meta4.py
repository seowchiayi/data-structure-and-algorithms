import collections
def shortest_path_in_binary_matrix(grid):
    # - this is a bfs question
    # - each grid can move in 8 directions (right, left, up, down, diagonal up left, diagonal up right, diagonal down left, diagonal down right )
    # - initialize a queue, store first initial i, j index in queue
    # - increment i, j check if i, j index is still within bounds
    # - initialize a path length, increment path length if grid[i][j] is 1
    # - return final path length
    if grid[0][0] != 0 or grid[len(grid)-1][len(grid)-1] != 0:
            return -1
    
    queue = collections.deque([(0, 0, 1)])
    # (right, left, up, down, diagonal up left, diagonal up right, diagonal down left, diagonal down right)
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    grid[0][0] = 1
    
    while queue:
        i, j, path_len = queue.popleft()

        if (i, j) == (len(grid) - 1, len(grid) - 1):
            return path_len

        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]

            if 0 <= new_i <= len(grid) - 1 and 0 <= new_j <= len(grid) - 1 and grid[new_i][new_j] == 0:
                grid[new_i][new_j] = 1
                queue.append((new_i, new_j, path_len + 1))

    return -1

def basic_calculator_ii(s):
    i = 0
    cur = prev = res = 0
    cur_operation = "+"

    while i < len(s):
        cur_char = s[i]

        if cur_char.isdigit():
            while i < len(s) and s[i].isdigit():
                cur = cur * 10 + int(s[i])

                i += 1
            
            i -= 1

            if cur_operation == "+":
                res += cur

                prev = cur
            elif cur_operation == "-":
                res -= cur

                prev = -cur
            elif cur_operation == "*":
                res -= prev
                res += prev * cur

                prev = cur * prev
            else:
                res -= prev
                res += int(prev / cur)

                prev = int(prev / cur)
            
            cur = 0
        elif cur_char != " ":
            cur_operation = cur_char

        i += 1

    return res


def subarray_sum_equals_k(nums, k):
    # - this question is an array question
    # - please look at code because only code makes sense for this question, not bullet points
    # - initialize a dictionary to record the number of times you see a unique sum at each cumulation
    # - iterate through list of numbers, add number to total sum, save current sum number in dictionary
    # - return result of number of repeated sums seen that meant K existed
   
    if not nums:
        return 0
    
    prefix_d = collections.defaultdict(int)
    prefix_d[0] = 1

    prefix_sum = res = 0

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_d:
            # an example is if k = 12 and we have seen sums of 14 and 26, it means we have came across k before
            res += prefix_d[prefix_sum - k]
        

        prefix_d[prefix_sum] += 1

    return res

if __name__ == "__main__":
    #print(shortest_path_in_binary_matrix(grid = [[0,1],[1,0]]))
    #print(shortest_path_in_binary_matrix(grid = [[0,0,0],[1,1,0],[1,1,0]]))
    #print(basic_calculator_ii("23+2* 2 "))
    print(subarray_sum_equals_k(nums=[1, 2, 3], k=3))


