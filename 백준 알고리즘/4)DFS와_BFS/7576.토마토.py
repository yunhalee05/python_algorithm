# from collections import deque


# m, n = map(int, input().split())
# tomato = []
# for i in range(n):
#     tomato.append(list(map(int, input().split())))

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# def bfs(tomato) :
#     queue = deque()
#     for i in range(n):
#         for j in range(m):
#             if tomato[i][j] == 1:
#                 queue.append([i, j])

#     while len(queue)>0:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx>=n or ny>=m or nx<0 or ny<0:
#                 continue
#             if tomato[nx][ny] == 0:
#                 tomato[nx][ny] = tomato[x][y]+1
#                 queue.append([nx, ny])
#     for i in range(n):
#         if 0 in tomato[i]:
#             return -1
#     return max(map(max, tomato))-1

# print(bfs(tomato))

from collections import deque
global m, n, tomato, day
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
answer = 0
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def find_first_rotten_tomato(queue):
    global m, n, tomato
    for a in range(n):
        for b in range(m):
            if tomato[a][b] == 1:
                queue.append((a, b, 0))
    return queue

def check_all_rotten():
    global m, n, tomato
    for a in range(n):
        for b in range(m):
            if tomato[a][b] == 0:
                return False
    return True

def bfs():
    global m, n, tomato, answer
    queue = find_first_rotten_tomato(deque())
    if len(queue) == 0:
        answer = -1
        return 
    while queue:
        y, x, day = queue.popleft()
        answer = day
        for k in range(4):
            ny = y + d[k][0]
            nx = x + d[k][1]
            if 0<=ny<n and 0<=nx<m and tomato[ny][nx]==0:
                tomato[ny][nx] = 1
                queue.append((ny,nx, day+1))
    if not check_all_rotten():
        answer = -1
        
bfs()     
print(answer)






