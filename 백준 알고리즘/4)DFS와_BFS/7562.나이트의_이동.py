from collections import deque

t = int(input())
dx = [ 1, 2, 2, 1, -1, -2, -2, -1]
dy = [ -2, -1, 1, 2, 2, 1, -1, -2]
answer = []
for i in range(t):
    l = int(input())
    nowX, nowY = map(int, input().split())
    destX, destY = map(int, input().split())
    graph = [[0]*l for _ in range(l)]

    def bfs(x, y):
        if x == destX and y == destY:
            return 
        queue = deque()
        queue.append([x, y])

        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx>=l or ny>=l or nx<0 or ny<0 :
                    continue
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])
    bfs(nowX, nowY)
    answer.append(graph[destX][destY])

for i in answer:
    print(i)



