from collections import Counter
import re

def pick_movies(flight_length, movie_lengths):
    main, secondary = 0, 1
    times = 0
    while times < len(movie_lengths):
        total_length = movie_length[main]
        for movie_length in movie_lengths[secondary:]:
            if movie_length + total_length == flight_length:
                return True
        main += 1
        secondary += 1
        times += 1
            
        
    return False

def permutation_palindrome(s):
    # solution 1 - with python counter
    # counter = defaultdict(int)
    # count = 0
    # for c in s:
    #     counter[c] += 1
    # for key, value in counter.items():
    #     if value != 2:
    #         count += 1
    
    # if count <= 1:
    #     return True
    
    # solution 2 - with set
    unpaired_chars = set()

    for c in s:
        if c not in unpaired_chars:
            unpaired_chars.add(c)
        else:
            unpaired_chars.remove(c)

    return len(unpaired_chars) == 1


def build_word_cloud(s):
    from collections import OrderedDict
    s = s.lower()
    no_punctuation = re.sub(r'[^\w\s]', ' ', s)

    lst = no_punctuation.split(' ')
    c = Counter(lst)
    d = {key: val for key, val in dict(c).items() if key != ''}
    
    return OrderedDict(sorted(d.items()))


if __name__ == "__main__":
    # print(permutation_palindrome("civic"))
    # print(build_word_cloud('Add-milk and eggs, then add flour and sugar.'))
    # print(build_word_cloud("We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."))
    # print(build_word_cloud('The bill came to five dollars.'))
    # print(build_word_cloud('I like cake'))
    # print(build_word_cloud('Chocolate cake for dinner and pound cake for dessert'))
    # print(build_word_cloud('Strawberry short cake? Yum!'))
    # print(build_word_cloud('Dessert - mille-feuille cake'))
    # print(build_word_cloud('Mmm...mmm...decisions...decisions'))
    # print(build_word_cloud("Allie's Bakery: Sasha's Cakes"))
