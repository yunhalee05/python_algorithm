n, m = map(int, input().split())
graph = [[int(1e9)]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c<graph[a][b]:
        graph[a][b] =c


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[b][k])


for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == int(1e9):
            print(0, end=" ")
        else:
            print(graph[a][b], end = " ")
    print()