from math import inf
import sys 

global answer, n, m, house, chicken, q
n, m = map(int, sys.stdin.readline().split())
chicken = []
house = []
answer = inf
q = []

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if line[j] == 1 : 
            house.append((i, j))
        elif line[j] == 2 :
            chicken.append((i, j))

def calculateDistance(h, chicken) :
    distance = inf
    for c in chicken : 
        distance = min(distance, abs(h[0]-c[0]) + abs(h[1] - c[1]))
    return distance

def calculateTotalDistance(house, chicken) :
    total = 0 
    for h in house : 
        total += calculateDistance(h, chicken)
    return total 

def dfs(depth, index) :
    global answer, n, m, house, chicken, q
    if depth == m : 
        answer = min(answer, calculateTotalDistance(house, q))
        return 
    for i in range(index, len(chicken)) :
        q.append(chicken[i])
        dfs(depth + 1, i + 1)
        q.pop()


if len(chicken) == m : 
    print(calculateTotalDistance(house, chicken))
else : 
    dfs(0, 0)
    print(answer)


    