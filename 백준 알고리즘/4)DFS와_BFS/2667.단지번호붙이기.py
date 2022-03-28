from collections import deque


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    graph[i][j] += 1
    cnt = 1
    while len(queue)>0 :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=n or ny >=n or nx<0 or ny<0:
                continue
            if graph[nx][ny] == 1 :
                queue.append([nx, ny])
                graph[nx][ny] +=1
                cnt += 1
    return cnt 

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)
        
