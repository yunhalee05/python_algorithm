from cmath import inf
from collections import deque


n, m, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def checkbox(lbx, lby, rtx, rty):
    lx = n-lby-1 
    ly = lbx
    rx = n-rty
    ry = rtx-1
    for i in range(rx, lx+1):
        for j in range(ly, ry+1):
            graph[i][j] = inf
for _ in range(k):
    lbx, lby, rtx, rty = map(int, input().split())
    checkbox(lbx, lby, rtx, rty)
    
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 1
    cnt = 1
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=n or ny>=m or nx<0 or ny<0:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append([nx, ny])
                cnt +=1
    return cnt 
answer = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 :
            answer.append(bfs(i, j))
print(len(answer))
answer.sort()
for i in answer:
    print(i, end=' ')
    
  

