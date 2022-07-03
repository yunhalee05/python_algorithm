import math
c = int(input())
answer = 0 
def find(path, visited, currentLength) :
    if len(path) == n : 
        print(path)
        return currentLength + distances[path[0]][path[-1]]

    result = math.inf
    for i in range(n):
        if not visited[i] :            
            cur = path[-1]
            path.append(i)
            visited[i] =True
            cand = find(path, visited, currentLength + distances[cur][i])
            result = min(result, cand)
            path.pop()
            visited[i] =False

    return result


for case in range(c) :
    n = int(input())
    distances = [list(map(float, input().split())) for _ in range(n)]
    visited = [False] * n
    path = [0]
    visited[0] = True
    answer = find(path, visited, 0)
        
    print(answer)
