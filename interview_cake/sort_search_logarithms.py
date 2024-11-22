import string
from typing import List
from collections import Counter, defaultdict
import pandas

def find_rotation_point(words):
    # for i in range(len(words)):
    #     if i - 1 >= 0:
    #         if words[i][0] < words[i-1][0]:
    #             return i
    # binary search approach
    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:
        # Guess a point halfway between floor and ceiling
        guess_index = floor_index + ((ceiling_index - floor_index) // 2)
        print('guess index')
        print(guess_index)
        # If guess comes after first word or is the first word
        if words[guess_index] >= first_word:
            # Go right
            floor_index = guess_index
            print('floor index')
            print(floor_index)
        else:
            # Go left
            ceiling_index = guess_index
            print('celling index')
            print(ceiling_index)

        # If floor and ceiling have converged
        if floor_index + 1 == ceiling_index:
            # Between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return ceiling_index
    

def find_a_duplicate(numbers: List[int]) -> int:
    # we have at least one integer which appears at least twice
    # Time: O(n)
    # Space: O(n)
    # seen = set()
    # for num in numbers:
    #     if num not in seen:
    #         seen.add(num)
    #     else:
    #         return num
    
    # binary search approach
    floor = 1
    ceiling = len(numbers) - 1
    print(floor)
    print(ceiling)

    while floor < ceiling:
        print('inside while loop')
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling
        print(lower_range_floor)
        print(lower_range_ceiling)
        print(upper_range_floor)
        print(upper_range_ceiling)
        # Count number of items in lower range
        items_in_lower_range = 0
        for item in numbers:
            # Is it in the lower range?
            print("item")
            print(item)
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            lower_range_ceiling
            - lower_range_floor
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor


def sort_scores(unsorted_list: List[int], highest_possible_score: int) -> List[int]:
    score_counts = [0] * (highest_possible_score+1)

    for score in unsorted_list:
        score_counts[score] += 1
        
    sorted_scores = []

    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]
        for time in range(count):
            sorted_scores.append(score)
    
    return sorted_scores


def merge_meeting_times(meetings):
    sorted_meetings = sorted(meetings)
    merged_meetings = [sorted_meetings[0]]

    for meeting in sorted_meetings[1:]:
        if meeting[0] <= merged_meetings[-1][1]:
            merged_meetings[-1] = (merged_meetings[-1][0], max(merged_meetings[-1][1], meeting[1]))
        else:
            merged_meetings.append((meeting[0], meeting[1]))
    return merged_meetings




if __name__ == "__main__":
#     print(find_rotation_point(words = [
#     'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',  # <-- rotates here!
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage',
# ]))
    # print(find_a_duplicate([1, 2, 5, 5, 5, 5]))
    print(sort_scores([37, 89, 41, 65, 91, 53], 91))
    print(merge_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
