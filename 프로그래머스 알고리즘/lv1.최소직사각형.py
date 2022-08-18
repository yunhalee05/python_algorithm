import math
def solution(sizes):
    answer = 0
    h = 0
    w = 0
    for i, j in sizes : 
        if max(i, j) > h : 
            h = max(i, j)
        if min(i, j) > w : 
            w = min(i, j)        
    return h*w