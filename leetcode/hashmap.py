import collections

def custom_sort_string(order, s):
    d = collections.defaultdict(int)
    res = ""

    for c in s:
        d[c] += 1

    for c in order:
        if c in d:
            while d[c] > 0:
                res += c
                d[c] -= 1
    
    for c in d:
        if d[c] > 0:
            while d[c] > 0:
                res += c
                d[c] -= 1
    
    return res



if __name__ == "__main__":
    print(custom_sort_string(order="cba", s="abcd"))
    print(custom_sort_string(order="hucw", s="utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"))