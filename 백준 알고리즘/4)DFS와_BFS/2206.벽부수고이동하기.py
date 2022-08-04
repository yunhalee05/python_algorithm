# from math import inf
# import sys 
# from collections import deque
# global n, m, graph, visited, answer, d
# n, m = map(int, sys.stdin.readline().split())
# graph = []
# visited = [[False]*m for _ in range(n)]
# answer = inf
# d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# for i in range(n) : 
#     graph.append(sys.stdin.readline())

# def bfs ():
#     global n, m, graph, visited, answer, d
#     q = deque()
#     visited[0][0] = True
#     if graph[0][0] == '1' : 
#         q.append((0, 0, 1, True, [(0, 0)]))
#     else : 
#         q.append((0, 0, 1, False, [(0, 0)]))
#     while q : 
#         x, y, cnt, isBroke, l = q.popleft()
#         if x == n-1 and y == m-1 :
#             if answer> cnt :
#                 answer = cnt 
#         for k in range(4):
#             nx, ny = x + d[k][0], y + d[k][1]
#             if 0>nx or 0>ny or nx>=n or ny>=m : 
#                 continue
#             if not visited[nx][ny]:
#                 print(l, nx, ny, q, visited)
#                 if graph[nx][ny] == '1' and not isBroke : 
#                     visited[nx][ny] = True 
#                     q.append((nx, ny, cnt +1, not isBroke, l +[(nx, ny)]))
#                 elif graph[nx][ny] == '0' :
#                     visited[nx][ny] = True 
#                     q.append((nx, ny, cnt+1, isBroke, l +[(nx, ny)]))

# bfs()
# if answer == inf : 
#     print(-1)
# else : 
#     print(answer)

# 0 0 0 0
# 0 1 0 0
# 0 0 0 0
# 1 1 1 1
# 0 0 0 0



from math import inf
import sys 
from collections import deque
global n, m, graph, visited, answer, d
n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
answer = inf
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n) : 
    graph.append(sys.stdin.readline())

def bfs ():
    global n, m, graph, visited, answer, d
    q = deque()
    if graph[0][0] == '1' :
        visited[0][0][1] = 1
        q.append((0, 0, True))
    else : 
        visited[0][0][0] = 1 
        q.append((0, 0, False))
    while q : 
        x, y, isBroke= q.popleft()
        if x == n-1 and y == m-1 :
            if answer > visited[x][y][isBroke] :
                answer = visited[x][y][isBroke]
        for k in range(4):
            nx, ny = x + d[k][0], y + d[k][1]
            if 0>nx or 0>ny or nx>=n or ny>=m : 
                continue
            if visited[nx][ny][isBroke] == 0:
                if graph[nx][ny] == '1' and not isBroke : 
                    visited[nx][ny][1] = visited[x][y][isBroke] + 1 
                    q.append((nx, ny, True))
                elif graph[nx][ny] == '0' :
                    visited[nx][ny][isBroke] = visited[x][y][isBroke] +  1 
                    q.append((nx, ny, isBroke))
bfs()
if answer == inf : 
    print(-1)
else : 
    print(answer)