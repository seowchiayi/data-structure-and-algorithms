import string

def equal_substring(s: str, t: str, maxCost: int):
    if not s:
        return 0
    if not t:
        return 0

    l = 0
    r = 0
    total_cost = 0
    count = 0
    max_count = 0
    while r < len(s):
        cost = abs(ord(s[r]) - ord(t[r]))
        total_cost += cost
        if total_cost <= maxCost:
            r += 1
            count += 1
        elif total_cost > maxCost:
            total_cost -= abs(ord(s[l]) - ord(t[l]))
            l += 1
            r += 1
        max_count = max(count, max_count)
    return max_count

def equal_substring_improved(s: str, t: str, maxCost: int):
    if not s or not t:
        return 0
    
    max_length = 0
    l = 0

    for r in range(len(s)):
        current_cost += abs(ord(s[r]) - ord(t[r]))

        while current_cost > maxCost:
            current_cost -= abs(ord(s[l]) - ord(t[l]))
            l += 1

        max_length = max(max_length, r - l + 1)
                            

    return max_length


if __name__ == "__main__":
    # print(equal_substring("abcd", "bcdf", maxCost=3))
    # print(equal_substring("krrgw", "zjxss", maxCost=19))
    # print(equal_substring("pxezla", "loewbi", maxCost=25)) #-> output :4
    
    # print(ord('p') - ord('l'))
    # print(ord('x') - ord('o'))
    # print(ord('e') - ord('e'))
    # print(ord('z') - ord('w'))
    # print(ord('l') - ord('b'))
    # print(ord('a') - ord('i'))

    # print(equal_substring("jzmhzdq", "rymuemg", maxCost=17))
    # print(ord('j') - ord('r'))
    # print(ord('z') - ord('y'))
    # print(ord('m') - ord('m'))
    # print(ord('h') - ord('u'))
    # print(ord('z') - ord('e'))
    # print(ord('d') - ord('m'))
    # print(ord('q') - ord('g'))

    print(equal_substring(s="krpgjbjjznpzdfy", t="nxargkbydxmsgby", maxCost=14))