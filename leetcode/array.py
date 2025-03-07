from typing import List

def merge_sorted_array(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    x = m + n - 1
    y = n - 1
    z = m - 1

    if nums2[y] > nums1[x]:
        nums1[z] = nums2[y]
    elif nums2[y] < nums1[x]:
        nums1[x] = nums2[y]
        
        
def diagonal_traverse(mat):
    res = []
    i, j = 0, 0
    going_up = True
    while len(res) != len(mat) * len(mat[0]):
        if going_up:
            while i >= 0 and j < len(mat[0]):
                res.append(mat[i][j])
                i -= 1
                j += 1
                # print(i, j)
            if j == len(mat[0]):
                i += 2
                j -= 1
            else:
                i += 1
            going_up = False
        else:
            while i < len(mat) and j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1
            
            if i == len(mat):
                i -= 1
                j += 2
            else:
                j += 1
            going_up = True


    return res

def toeplits_matrix(matrix: List[List[int]]) -> bool:   

    def is_same_value(row, col) -> bool:
        val = matrix[row][col]

        while row < len(matrix) and col < len(matrix[0]):
            if matrix[row][col] != val:
                return False
            row += 1
            col += 1
        
        return True
        
    for col in range(len(matrix[0])):
        if not is_same_value(0, col):
            return False
    for row in range(1, len(matrix)):
        if not is_same_value(row, 0):
            return False
    
    return True

def kth_missing_positive_number(arr: List[int], k: int) -> int:
    if arr[0] != 1:
        if arr[0] - 1 >= k:
            return k
        else:
            k -= arr[0] - 1
    
    i = 0

    while i < len(arr) - 1: # -> we will be comparing to index + 1
        diff = arr[i + 1] - arr[i]
        if diff != 1:
            for num in range(arr[i] + 1, arr[i + 1]):
                k -= 1
                if not k: # if k reaches 0 will trigger if not k to return True
                    return num
        
        i += 1
    
    if k:
        return arr[-1] + k
    
def number_of_island(grid):
    num_islands = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def set_island_zeros(grid, row, col):
        if (0 <= row < len(grid)) and (0 <= col < len(grid[0])) and grid[row][col] == "1":
            grid[row][col] = "0"

            for row_inc, col_inc in directions:
                set_island_zeros(grid, row + row_inc, col + col_inc)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                num_islands += 1

                set_island_zeros(grid, row, col)
    
    return num_islands

class MakeALargeIsland:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.island_id = -1
        self.island_areas = {}

        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # go over every single tile in grid -> O(n^2)
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                if grid[m][n] == 1:
                    island_area = self.dfs(grid, m, n)

                    self.island_areas[self.island_id] = island_area
                    
                    self.island_id -= 1
        max_area = 0

        # go through every tile in the grid for the second time -> O(n^2)
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                if not grid[m][n]:
                    area = 1

                    surrounding = set()

                    for m_inc, n_inc in self.directions:
                        new_m = m + m_inc
                        new_n = n + n_inc

                        if (0 <= new_m < len(grid)) and (0 <= new_n < len(grid[0])) and grid[new_m][new_n] != 0:
                            surrounding.add(grid[new_m][new_n])
                    
                    for island_id in surrounding:
                        area += self.island_areas[island_id]
                    
                    max_area = max(max_area, area)
        
        return max_area if max_area else len(grid) ** 2

    def dfs(self, grid, m, n):
        if (0 <= m < len(grid)) and (0 <= n < len(grid[m])) and grid[m][n] == 1:
            grid[m][n] = self.island_id

            area = 1

            for m_inc, n_inc in self.directions:
                area += self.dfs(grid, m + m_inc, n + n_inc)

            return area
        else:
            return 0
        
def alphabet_board_path(target: str):
    board = {'a': [0, 0], 'b': [0, 1], 'c': [0, 2],
        'd': [0, 3], 'e': [0, 4], 'f': [1, 0],
        'g': [1, 1], 'h': [1, 2], 'i': [1, 3],
        'j': [1, 4], 'k': [2, 0], 'l': [2, 1],
        'm': [2, 2], 'n': [2, 3], 'o': [2, 4],
        'p': [3, 0], 'q': [3, 1], 'r': [3, 2],
        's': [3, 3], 't': [3, 4], 'u': [4, 0],
        'v': [4, 1], 'w': [4, 2], 'x': [4, 3],
        'y': [4, 4], 'z': [5, 0]}
    
    origins = []
    for c in target:
        if c in list(board.keys()):
            origins.append(board[c])
    
    dests = []
    for origin in origins:
        origin_r, origin_c = origin[0], origin[1]
        if not dests:
            dest_r, dest_c = origin_r, origin_c
            dests.append([dest_r, dest_c])
            prev = [origin_r, origin_c]
        else:
            origin_r, origin_c = origin[0], origin[1]
            dest_r, dest_c = origin_r - prev[0], origin_c - prev[1]
            dests.append([dest_r, dest_c])
            prev = [origin_r, origin_c]
    
    res = ""
    for dest in dests:
        dest_r, dest_c = dest[0], dest[1]
        if dest_r > dest_c:
            if dest_c < 0:
                while dest_c != 0:
                    res += 'L'
                    dest_c += 1
            if dest_c > 0:
                while dest_c != 0:
                    res += 'R'
                    dest_c -= 1
            if dest_r < 0:
                while dest_r != 0:
                    res += 'U'
                    dest_r += 1
            if dest_r > 0:
                while dest_r != 0:
                    res += 'D'
                    dest_r -= 1
        else:
            if dest_r < 0:
                while dest_r != 0:
                    res += 'U'
                    dest_r += 1
            if dest_r > 0:
                while dest_r != 0:
                    res += 'D'
                    dest_r -= 1
            if dest_c < 0:
                while dest_c != 0:
                    res += 'L'
                    dest_c += 1
            if dest_c > 0:
                while dest_c != 0:
                    res += 'R'
                    dest_c -= 1
        res += "!"
    return res

def alphabet_board_path_improved(target: str):
    board = {'a': [0, 0], 'b': [0, 1], 'c': [0, 2],
    'd': [0, 3], 'e': [0, 4], 'f': [1, 0],
    'g': [1, 1], 'h': [1, 2], 'i': [1, 3],
    'j': [1, 4], 'k': [2, 0], 'l': [2, 1],
    'm': [2, 2], 'n': [2, 3], 'o': [2, 4],
    'p': [3, 0], 'q': [3, 1], 'r': [3, 2],
    's': [3, 3], 't': [3, 4], 'u': [4, 0],
    'v': [4, 1], 'w': [4, 2], 'x': [4, 3],
    'y': [4, 4], 'z': [5, 0]}
    
    cur_r, cur_c = 0, 0
    res = ""
    for c in target:
        dest_r, dest_c = board[c][0], board[c][1]
        print(f"dest: {dest_r, dest_c}")
        if cur_r == 5 and cur_c == 0:
            # move vertically first then horizontally
            if dest_r > cur_r:
                while cur_r != dest_r:
                    cur_r += 1
                    res += "D"
            elif dest_r < cur_r:
                while cur_r != dest_r:
                    cur_r -= 1
                    res += "U"
            if dest_c > cur_c:
                while cur_c != dest_c:
                    cur_c += 1
                    res += "R"
            elif dest_c < cur_c:
                while cur_c != dest_c:
                    cur_c -= 1
                    res += "L"
        else:
            # move horizontally first then vertically
            if dest_c > cur_c:
                while cur_c != dest_c:
                    cur_c += 1
                    res += "R"
            elif dest_c < cur_c:
                while cur_c != dest_c:
                    cur_c -= 1
                    res += "L"
            if dest_r > cur_r:
                while cur_r != dest_r:
                    cur_r += 1
                    res += "D"
            elif dest_r < cur_r:
                while cur_r != dest_r:
                    cur_r -= 1
                    res += "U"
            
        res += "!"
        print(f"cur: {cur_r, cur_c}")

    return res

if __name__ == "__main__":
    #print(diagonal_traverse(mat=[[1,2,3],[4,5,6],[7,8,9]]))
    #print(toeplits_matrix(matrix=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    #print(toeplits_matrix(matrix=[[1,2],[2,2]]))
    #print(toeplits_matrix(matrix=[[65,98,57]]))
    #print(toeplits_matrix(matrix=[[22,33,98],[34,22,33]]))
    #print(toeplits_matrix(matrix=[[11,74,7,93],[40,11,74,7]]))
    #print(toeplits_matrix(matrix=[[53,0,70,43,30,54,99,21,42,96,64,77,24],[68,53,95,70,43,30,54,99,21,42,96,64,77],[39,68,53,95,70,43,30,54,99,21,42,96,64]]))
    # print(kth_missing_positive_number(arr = [2,3,4,7,11], k = 5))
    # print(kth_missing_positive_number(arr = [1,2,3,4], k = 2))
    # print(number_of_island(grid = [
    #     ["1","1","0","0","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","1","0","0"],
    #     ["0","0","0","1","1"]
    # ]))
    #print(alphabet_board_path("leet"))
    #print(alphabet_board_path("zdz"))
    #print(alphabet_board_path_improved("leet"))
    print(alphabet_board_path_improved("zdz"))