import collections
def shortest_path_in_binary_matrix(grid):
    # - this is a bfs question
    # - you go through every grid, while checking if its gonna go all the way towards the right, bottom or diagonal
    # - reset sum count every time you change direction
    queue = collections.deque((grid[0][0], grid[0][1]))

    while queue:
        x, y = queue.popleft()
        print(x, y)
        break
if __name__ == "__main__":
    #grid = [[0,1],[1,0]]
    shortest_path_in_binary_matrix(grid = [[0,1],[1,0]])