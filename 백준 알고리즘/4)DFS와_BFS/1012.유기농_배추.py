from collections import deque


t = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(land, x, y):
    queue = deque()
    queue.append([x,y])
    while len(queue) >0 :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or ny >= n or nx<0 or ny<0 :
                continue
            if land[nx][ny] == 1:
                queue.append([nx,ny])
                land[nx][ny] =2
answer = []
for _ in range(t):
    m, n, k = map(int,input().split())
    land = [[0] * n for _ in range(m)]
    for i in range(k):
        x, y = map(int,input().split())
        land[x][y] = 1
    cnt = 0 
    for i in range(m):
        for j in range(n):
            if land[i][j] == 1:
                bfs(land, i, j)
                cnt += 1
    answer.append(cnt)
    
for i in answer:
    print(i)


