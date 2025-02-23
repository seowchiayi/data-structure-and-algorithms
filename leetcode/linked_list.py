from typing import Optional
import heapq

# Practice recursion with reversing singly linked list
class SinglyLinkedList():
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

def reverse_singly_linked_list(node: SinglyLinkedList):
    # Time: O(n) -> n is the number of nodes in the linkedin
    # Space: O(n) -> 
    if not node:
        return
    
    reverse_singly_linked_list(node.next)
    print(node.val)

class Node:
    def __init__(self, x: int, next: 'Node'=None, random: 'Node'=None)
        self.val = int(x)
        self.next = next
        self.random = random
        

def copy_list_with_random_pointer(head: 'Optional[Node]'):
    if not head: return None

    curr = head
    old_to_new = {}

    while curr:
        node = Node(x=curr.val)
        old_to_new[curr] = node
        curr = curr.next
    
    curr = head
    while curr:
        new_node = old_to_new[curr]
        new_node.next = old_to_new[curr.next] if curr.next else None
        new_node.random = old_to_new[curr.random] if curr.random else None
        curr = curr.next

    return old_to_new[head]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

        D = ListNode()
        cur = D
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return D.next


if __name__ == "__main__":
    #print(copy_list_with_random_pointer)
    head = SinglyLinkedList(1)
    A = SinglyLinkedList(2)
    B = SinglyLinkedList(3)

    head.next = A
    A.next = B
    reverse_singly_linked_list(head)