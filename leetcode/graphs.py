import collections
from typing import List
# directed graph question
def course_schedule(numCourses: int, prerequisites: List[List[int]]):
    # detect if there is any cycle (interdependency) in the graph, if there is return False
    # turn List of List of int to adjacency lists when working with graph questions so its easier 
    g = collections.defaultdict(list)
    courses = prerequisites
    for a, b in courses:
        g[a].append(b)

    UNVISITED = 0
    VISITING = 1
    VISITED = 2
    states = [UNVISITED] * numCourses

    def dfs(node):
        state = states[node]
        if state == VISITED: return True
        elif state == VISITING: return False

        states[node] = VISITING

        for nei in g[node]:
            if not dfs(nei):
                return False

        states[node] = VISITED
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    

    return True

if __name__ == "__main__":
    print(course_schedule(numCourses=5, prerequisites=[[0,1], [2,3], [3,4], [2,1], [4,2]]))