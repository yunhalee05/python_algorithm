from queue import PriorityQueue
import sys 
inf = 100000000

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

graph = [[] for _ in range(v+1)]
dist = [inf]*(v+1)

for _ in range(e) :
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

q = PriorityQueue()

dist[k] = 0
q.put((0, k))

while not q.empty()  : 
    weight, cur = q.get()

    if weight > dist[cur]:
        continue

    for i in graph[cur] :
        if weight + i[1] < dist[i[0]]:
            dist[i[0]] = weight + i[1]
            q.put((dist[i[0]], i[0]))
        
for i in range(1, v+1) :
    if dist[i] == inf:
        print('INF')
    else :
        print(dist[i])
        

# from heapq import heappush, heappop
# import sys 
# inf = 100000000
# n, e = map(int, sys.stdin.readline().split())
# k = int(sys.stdin.readline())
# graph = [[] for _ in range(n+1)]
# dist = [inf]*(n+1)

# for _ in range(e) :
#     a, b, c = map(int, sys.stdin.readline().split())
#     graph[a].append((b, c))

# h = []
# dist[k] = 0
# heappush(h, (0, k))

# while h  : 
#     w, v = heappop(h)

#     if w > dist[v]:
#         continue

#     for node, weight in graph[v] :
#         if w + weight < dist[node]:
#             dist[node] = w + weight
#             heappush(h, (w + weight, node))
        
# for i in range(1, n+1) :
#     if dist[i] == inf:
#         print('INF')
#     else :
#         print(dist[i])