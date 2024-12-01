from typing import List

def reverse_string(s):
    l = 0 
    r = len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return s

def two_sum_2(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1
    while l < r:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l + 1, r + 1]
        else:
            if sum > target:
                r -= 1
            if sum < target:
                l += 1




if __name__ == "__main__":
    print(reverse_string(["h","e","l","l","o"]))
    print(two_sum_2(numbers=[2,7,11,15], target=9))