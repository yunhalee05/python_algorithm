n, k = map(int, input().split())

graph = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        graph[i][j] = int(input())

s, x, y = map(int, input().split())

count = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(number, graph, x, y):
    if count ==s:
        return graph

    # 범위 안이라면 퍼져나간다.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<n :
            if graph[nx][ny] ==0:
                graph[nx][ny] = number
                count+= 1
                dfs(number, graph, nx, ny)
                graph[nx][ny] =0
                count-=1
    

for number in range(1, k+1):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == number:
                graph = dfs(number, graph, i, j)

print(graph)

#답안
# from collections import deque

# n, k = map(int, input().split())

# graph = []
# data = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#     for j in range(n):
#         if graph[i][j] != 0 :
#             data.append((graph[i][j], 0, i, j))

# target_s, target_x, target_y = map(int, input().split())

# data.sort()
# q= deque(data)

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]


# while q:
#     virus, s, x, y = q.popleft()
#         if s ==target_s:
#             break

#     # 범위 안이라면 퍼져나간다.
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if nx>=0 and nx<n and ny>=0 and ny<n :
#             if graph[nx][ny] ==0:
#                 graph[nx][ny] = virus
#                 q.append((virus, s+1, nx, ny))

# print(graph[target_x-1][target_y-1])







    




