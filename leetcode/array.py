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


def making_a_large_island():


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
    print(number_of_island(grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]))