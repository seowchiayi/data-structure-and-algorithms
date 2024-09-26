from typing import List


def merge_meeting_times(meetings):
    meetings.sort(key=lambda k:k[0])
    merged = []

    for meeting in meetings:
        if len(merged) == 0:
            merged.append(meeting)
        elif meeting[0] > merged[-1][0] and meeting[1] < merged[-1][1]:
            continue
        elif meeting[0] > merged[-1][0] and meeting[1] > merged[-1][1]:
            merged[-1] = (merged[-1][0], meeting[1])
        elif meeting[0] == merged[-1][1]:
            merged[-1] = (merged[-1][0], meeting[1])
        else:
            merged.append(meeting)
    
    return merged

def reverse_chars_in_string(lst: List[str]) -> List[str]:
    # first solution
    # new_lst = [c for c in lst[::-1]]
    # return new_lst
    
    #second solution
    left_idx = 0
    right_idx = len(lst) - 1

    while left_idx < len(lst)/2:
        lst[left_idx], lst[right_idx] = lst[right_idx], lst[left_idx]
        left_idx += 1
        right_idx -= 1

    return lst

def my_reverse_words(lst: List[str]) -> List[str]:
    # first solution - not in place so its incorrect
    # new_lst = []
    # s = ''
    # for c in lst:
    #     if c != ' ':
    #         s += c
    #     elif c == ' ':
    #         new_lst.append(s)
    #         s = ''
    #     if c == lst[-1]:
    #         new_lst.append(s)
    
    # left_idx = 0
    # right_idx = len(new_lst) - 1

    # while left_idx < len(new_lst)/2:
    #     new_lst[left_idx], new_lst[right_idx] = new_lst[right_idx], new_lst[left_idx]
    #     left_idx += 1
    #     right_idx -= 1

    # return new_lst

    # second solution
    left_idx = 0
    right_idx = len(lst) - 1

    while left_idx < len(lst)/2:
        lst[left_idx], lst[right_idx] = lst[right_idx], lst[left_idx]
        left_idx += 1
        right_idx -= 1
    
    left_idx = 0
    for i in range(len(lst)):
        if lst[i] == ' ':
            right_idx = i - 1
            while left_idx < left_idx + ((right_idx - left_idx)/2):
                lst[left_idx], lst[right_idx] = lst[right_idx], lst[left_idx]
                left_idx += 1
                right_idx -= 1
        if i == len(lst) - 1:
            right_idx = i
            while left_idx < left_idx + ((right_idx - left_idx)/2):
                lst[left_idx], lst[right_idx] = lst[right_idx], lst[left_idx]
                left_idx += 1
                right_idx -= 1
        if lst[i-1] == ' ':
            left_idx = i

    return lst


def reverse_words(message):
    # First we reverse all the characters in the entire message
    reverse_characters(message, 0, len(message)-1)

    # This gives us the right word order
    # but with each word backward

    # Now we'll make the words forward again
    # by reversing each word's characters

    # We hold the index of the *start* of the current word
    # as we look for the *end* of the current word
    current_word_start_index = 0

    for i in range(len(message) + 1):
        # Found the end of the current word!
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            # If we haven't exhausted the message our
            # next word's start is one character ahead
            current_word_start_index = i + 1
    
    return message


def reverse_characters(message, left_index, right_index):
    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index  += 1
        right_index -= 1


def merge_lists(my_list, alices_list):
    lst = []
    total_len = len(my_list) + len(alices_list)
    while len(lst) < total_len:
        if len(my_list) == 0:
            lst.append(alices_list[0])
        elif len(alices_list) == 0:
            lst.append(my_list[0])
        elif alices_list[0] < my_list[0]:
            lst.append(alices_list[0])
            alices_list = alices_list[1:]
        else:
            lst.append(my_list[0])
            my_list = my_list[1:]
    
    return lst

def cafe_order_checker(take_out_orders, dine_in_orders, served_orders):
    for order in served_orders:
        if len(take_out_orders) > 0 and order == take_out_orders[0]:
            take_out_orders = take_out_orders[1:]
        elif len(dine_in_orders) > 0 and order == dine_in_orders[0]:
            dine_in_orders = dine_in_orders[1:]
        else:
            return False
        
    return True


if __name__ == "__main__":
    #meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    #meetings = [(1, 2), (2, 3)]
    #meetings = [(1, 10), (2, 6), (3, 5), (7, 9)]
    # meetings =  [(1, 3), (2, 4)]
    # print(merge_meeting_times(meetings))
    # print(reverse_chars_in_string(['h', 'e', 'l', 'l', 'o']))
    # print(reverse_words([ 'c', 'a', 'k', 'e', ' ',
    #         'p', 'o', 'u', 'n', 'd', ' ',
    #         's', 't', 'e', 'a', 'l' ]))
    # print(my_reverse_words([ 'c', 'a', 'k', 'e', ' ',
    #         'p', 'o', 'u', 'n', 'd', ' ',
    #         's', 't', 'e', 'a', 'l' ]))
    # print(merge_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]))
    # print(cafe_order_checker([1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3]))
    # print(cafe_order_checker([17, 8, 24], [12, 19, 2], [17, 8, 12, 19, 24, 2]))
    