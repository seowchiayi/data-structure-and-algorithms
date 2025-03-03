from typing import Optional
import heapq
import collections
import unittest

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

class CopyListWithRandomPointerNode:
    def __init__(self, x: int, next: 'Node'=None, random: 'Node'=None):
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

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convert_binary_search_tree_to_sorted_doubly_linked_list(root: 'Optional[Node]'):
    stack = []
    head = None
    prev = None
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()

        if not head:
            head = current
        else:
            prev.right = current
            current.left = prev
        
        prev = current

        current = current.right

    tail = prev
    head.left = tail
    tail.right = head

    return head

class LinkedListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def insert_into_a_sorted_circular_linked_list(head, insertVal):
    # handle edge case where head = None
    # create a new list and append head pointer
    # set prev as None
    # set new_node = None(insertVal)
    # set head = None
    # if not head = set first current as head
    # if current >= insertVal: insertVal.right = current, current.left = insertVal
    # prev.right = new_node, new_node.left = prev
    # set prev as current
    # result.append(prev)
    # return result
    

    if not head:
        new_head = Node(insertVal)
        new_head.next = new_head

        return new_head
    
    current = head
    while current.next != head:
        if current.val <= insertVal <= current.next.val:
            new_node = Node(insertVal, current.next)

            current.next = new_node

            return head
        
        elif current.val > current.next.val:
            if insertVal >= current.val or insertVal <= current.next.val:
                new_node = Node(insertVal, current.next)
                current.next = new_node

                return head
        current = current.next
    
    new_node = Node(insertVal, current.next)
    current.next = new_node
    
    return head


if __name__ == "__main__":
    #print(copy_list_with_random_pointer)
    # head = SinglyLinkedList(1)
    # A = SinglyLinkedList(2)
    # B = SinglyLinkedList(3)

    # head.next = A
    # A.next = B
    # reverse_singly_linked_list(head)
    # root = Node(4)
    # a = Node(2)
    # b = Node(5)
    # c = Node(1)
    # d = Node(3)

    # root.left = a
    # root.right = b
    # a.left = c
    # a.right = d

    # current = convert_binary_search_tree_to_sorted_doubly_linked_list(root)

    # root = Node(-1)
    # b = Node(1)
    # c = Node(9)

    # root.right = b
    # b.right = c

    # current = convert_binary_search_tree_to_sorted_doubly_linked_list(root)
    
    # while current:
    #     print(current.val)
    #     current = current.right

    # root = Node(4)
    # a = Node(2)
    # b = Node(9)
    # c = Node(1)
    # d = Node(3)
    # e = Node(-1)
    # f = Node(-2)

    # root.left = a
    # root.right = b
    # a.left = c
    # a.right = d
    # c.left = e
    # e.left = f

    # current = convert_binary_search_tree_to_sorted_doubly_linked_list(root)

    root = LinkedListNode(3)
    a = LinkedListNode(4)
    b = LinkedListNode(1)

    root.next = a
    a.next = b
    b.next = root

    node = insert_into_a_sorted_circular_linked_list(root, 2)
