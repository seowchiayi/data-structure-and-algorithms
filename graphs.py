from typing import List
from collections import defaultdict

def course_schedule(numCourses: List[int], prerequisites: List[int]) -> bool:
    g = defaultdict(list)
    courses = prerequisites
    for a, b in courses:
        g[a].append(b)
    
    UNVISITED = 0
    VISITING = 1
    VISITED = 2
    states  = [UNVISITED] * numCourses

    def dfs():
        pass

if __name__ == "__main__":
    course_schedule()