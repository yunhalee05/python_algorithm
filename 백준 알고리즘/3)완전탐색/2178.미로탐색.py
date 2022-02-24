from collections import deque
import math

n, m = map(int, input().split())
maze = []
min = math.inf
for i in range(n):
    maze.append(list(map(int, list(input()))))


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx >=n or ny<0 or ny>=m:
                continue 
            if  maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1
                queue.append((nx, ny))
    
    return maze[n-1][m-1]

print(bfs(0,0))





