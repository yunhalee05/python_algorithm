# from collections import deque

# n, m, v = map(int, input().split())

# graph = [[] for _ in range(n+1)]
# visit = [[1] for _ in range(n+1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#     graph[a].sort()
#     graph[b].sort()

# stack = []
# answer = []

# def dfs(stack, answer, visit):
#     if len(stack) == 0:
#         return answer
#     x = stack.pop()
#     answer.append(x)
#     for i in range(0, len(graph[x])):
#         y = graph[x][i]
#         if visit[y] != 0:
#             stack.append(y)
#             visit[y] = 0
#             return dfs(stack, answer, visit)
#     return answer

# def bfs(v):
#     queue = deque()
#     queue.append(v)
#     visit = [[1] for _ in range(n+1)]
#     visit[v] = 0
#     answer = []
#     while len(queue)>0 :
#         x = queue.popleft()
#         answer.append(x)
#         for i in range(0, len(graph[x])):
#             y = graph[x][i]
#             if visit[y]!=0:
#                 queue.append(y)
#                 visit[y] = 0
#     return answer

# stack.append(v)
# visit[v] = 0
# print(dfs(stack, answer, visit))
# print()
# print(bfs(v))


from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visit = [[1] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(v):
    print(v, end=' ')
    for i in range(0, len(graph[v])):
        y = graph[v][i]
        if visit[y] != 0:
            visit[y] = 0
            return dfs(y)
    return 

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue :
        x = queue.popleft()
        print(x, end=' ')
        for i in range(0, len(graph[x])):
            y = graph[x][i]
            if visit[y]!=0:
                queue.append(y)
                visit[y] = 0

visit[v] = 0
dfs(v)
print()
visit = [[1] for _ in range(n+1)]
visit[v] = 0
bfs(v)

