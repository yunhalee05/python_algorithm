import heapq
from math import inf
import sys 
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
dist = [inf] * (n+1)
for _ in range(m) :
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

h = []
heapq.heappush(h, (0, 1))
dist[1] = 0

while h : 
    weight, node = heapq.heappop(h)

    if weight > dist[node] :
        continue

    for v, w in graph[node] :
        if w + weight < dist[v] :
            dist[v] = w + weight
            heapq.heappush(h, (w + weight, v))

print(dist)


