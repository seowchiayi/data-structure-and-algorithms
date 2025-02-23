# Leetcode notes

1. BFS
- find shortest path in grid
- print node values in specific order

questions:


2. DFS
- find longest path in tree
- uses last in first out concept
- common data structures: stack [], double ended queuecollections.deque([])

questions:


3. Stack
- delete from end of the list frequently


4. Hashmaps
- lookup with O(n)
- count number/character occurence

questions:

5. Two pointer/Binary search
- traverse an array

questions:

6. Min/Max Heap
- find Kth element

questions:


# Notes dump
1. subarray sum equals K/divisible by K/multiple of K is solved by using prefix sum
    - prefix sum is the accumulative sum of each numbers as you go along the array
    - commonly used with a hashmap to track historical seen sums
    - if the current sum is being seen before, it means K existed

2. speak out thoughts when solving leetcode questions
3. write down bullet points of how to solve a question
4. think about edge cases first before solution
5. show interviewer you have weigh the pros & cons of every solution
6. reverse traverse list with `for i in range(len(list) -1, -1, -1): list[i]...`
7. traverse a list with index and value at the same time with enumerate `eg: for index, value in enumerate(list): ...`
8. list should not be the key of a dictionary in python because list is mutable, only immutable data structures are valid for python dictionary keys, use tuple instead
9. return the values in a dictionary using dict.values()

# Solved leetcode questions
https://grape-wolf-71f.notion.site/191353924ffd80138f04d447d98b7e88?v=191353924ffd809bb185000cefa41d86&pvs=4

