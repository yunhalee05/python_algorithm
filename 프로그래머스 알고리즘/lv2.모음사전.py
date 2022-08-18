from itertools import product

def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for i in range(1, 6) :
        for j in product(alpha, repeat=i) :
            dictionary.append(''.join(list(j)))
    dictionary.sort()
    return dictionary.index(word) + 1