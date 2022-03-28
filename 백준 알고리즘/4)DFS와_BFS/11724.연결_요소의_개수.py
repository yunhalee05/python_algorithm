from collections import deque

n, m = map(int, input().split())
graph = [[i] for i in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0]*(n+1)

def bfs(node):
    queue = deque()
    queue.append(node)
    while len(queue)>0:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
cnt = 0
for i in range(1, n+1) :
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)








