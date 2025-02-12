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

class MovingAverage:
    # - we are dealing with 2 cases here:
    # 1. number of variables collected is smaller than window size
    # 2. number of variables collected is bigger than window size and we need to slice the collected list of numbers
    # find the average by summing the numbers divided by window size 

    def __init__(self, size: int):
        self.size = size
        self.memory = {}
        self.count = 1
        self.sum = 0

    def next(self, val: int) -> float:
        self.sum += val
        self.memory[self.count] = self.sum
        self.count += 1
        map_len = len(self.memory)

        if map_len < self.size:
            return self.memory[map_len] / map_len
        elif map_len == self.size:
            return self.memory[map_len] / self.size
        else:
            return (self.memory[map_len] - self.memory[map_len - self.size])  / self.size
        
def minimum_add_to_make_valid_parentheses(s: str) -> int:
    ## TODO: move this to array.py! you don't need hashmap for this
    if not s:
        return 0
    elif "(" not in s and ")" not in s:
        return 2
    else:
        string_builder = []
        d = collections.defaultdict(int)
        for c in s:
            if c == "(":
                d[c] += 1
                string_builder.append(c)
            elif c == ")":
                if d["("] > d[")"]:
                    string_builder.append(c)
                    d[")"] += 1
                else:
                    d["added"] += 1

        d["added"] += d["("] - d[")"]
    
        return d["added"]
    
    


if __name__ == "__main__":
    # print(custom_sort_string(order="cba", s="abcd"))
    # print(custom_sort_string(order="hucw", s="utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"))
    # movingAverage = MovingAverage(3)
    # print(movingAverage.next(1)) # return 1.0 = 1 / 1
    # print(movingAverage.next(10)) # return 5.5 = (1 + 10) / 2
    # print(movingAverage.next(3)) # return 4.66667 = (1 + 10 + 3) / 3
    # print(movingAverage.next(5)) # return 6.0 = (10 + 3 + 5) / 3

    print(minimum_add_to_make_valid_parentheses(s="((("))
    print(minimum_add_to_make_valid_parentheses(s=")))"))
    #print(minimum_add_to_make_valid_parentheses(s="lee(t(c)o)de)(("))