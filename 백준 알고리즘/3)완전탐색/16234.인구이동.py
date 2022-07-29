from collections import deque
import sys 

def bfs(x, y, open):
    queue = deque()
    queue.append((x, y))
    check[x][y] = 1
    open.add((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if l <= abs(data[nx][ny] - data[x][y]) <= r and not check[nx][ny]:
                queue.append((nx, ny))
                check[nx][ny] = 1
                open.add((nx, ny))
    if len(open) >1 :
        temp = sum([data[y][x] for y, x in open]) //len(open)
        for y, x in open:
            data[y][x] = temp
        return True

    else:
        return False

data = []
n, l, r = map(int, sys.stdin.readline().split())
data = [list(map(int, input().split())) for _ in range(n)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result, flag = 0, True
while flag:
    check = [[0]*n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not check[i][j] and bfs(i, j, set()):
                flag = True
    if flag:
        result += 1
print(result)