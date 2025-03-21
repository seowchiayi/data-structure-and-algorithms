# Leetcode notes

1. BFS
- find shortest path in grid
- print node values in specific order
- traversal patterns: level order traversal (no preorder/inorder/postorder)

questions:


2. DFS
- find longest path in tree
- uses last in first out concept
- common data structures: stack [], double ended queue, collections.deque([])
- traversal patterns: preorder (node, left, right), inorder (left, node, right), postorder (left, right, node)
- ** inorder traversal always give you elements in ascending sorted order 

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

7. Sliding Window
- use 2 pointer approach
- normally left and right pointer start on the same index, right pointer moves forward, hits a condition and stops, then left pointer will move to meet right pointer and then right pointer will increment by one index and repeat the same process

questions: max consecutive ones


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
10. Space complexity for binary search trees is dependent on whether the nodes are balanced or skewed on one side
11. pre order runs the body of the node first and then the body of the left children and then the body of the right children
12. if you are able to simplify the question we wont have to think about the cases (ex: insert into sorted circular linked list)
13. calculate the ascii letter difference between two alphabets by using ord('a') - ord('b') = -1

# Best way to show problem solving skills in steps
1. Read question carefully
2. Internalize implementation steps in your mind
3. Verify if steps works with sample input
4. Verify again if steps covered edge cases
5. Write down internalized steps in bullet points
6. Modify any gaps that you didn't cover
7. Start coding

# Solved leetcode questions
https://grape-wolf-71f.notion.site/191353924ffd80138f04d447d98b7e88?v=191353924ffd809bb185000cefa41d86&pvs=4

