from collections import deque


m, n = map(int, input().split())
tomato = []
for i in range(n):
    tomato.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(tomato) :
    queue = deque()
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                queue.append([i, j])

    while len(queue)>0:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=n or ny>=m or nx<0 or ny<0:
                continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y]+1
                queue.append([nx, ny])
    for i in range(n):
        if 0 in tomato[i]:
            return -1
    return max(map(max, tomato))-1

print(bfs(tomato))



