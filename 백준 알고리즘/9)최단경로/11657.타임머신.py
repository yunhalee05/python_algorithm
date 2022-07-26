from math import inf
import sys 
n, m = map(int, sys.stdin.readline().split())
graph = []
dist = [inf] * (n+1)
for _ in range(m) :
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))

h = []
dist[1] = 0
isNegativeCycle = False
for i in range(n):
    for j in range(m):
        cur = graph[j][0]
        next = graph[j][1]
        cost = graph[j][2]

        if dist[cur] != inf and dist[next]> dist[cur] + cost:
            dist[next]= dist[cur] + cost
            if i == n-1:
                isNegativeCycle = True


if isNegativeCycle:
    print(-1)
else : 
    for i in range(2, n+1):
        if dist[i] == inf:
            print(-1)
        else :
            print(dist[i])


