# import sys 
# from collections import deque
# n, m  = map(int, sys.stdin.readline().split())
# board = []
# directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# for _ in range(n) :
#     board.append(list(map(int, sys.stdin.readline().split())))

# def move(x, y, direction, cnt) :
#     nx = (x + directions[direction][0]*(cnt%n) + n) % n 
#     ny = (y + directions[direction][1]*(cnt%n) + n) % n
#     return nx, ny

# def count_diagonal_water(x, y) :
#     for i in [1, 3, 5, 7] :
#         nx = x + directions[i][0]
#         ny = y + directions[i][1]
#         if nx<0 or ny<0 or nx>=n or ny>=n or board[nx][ny]<1:
#             continue
#         board[x][y] += 1

# q = deque()
# q.extend([(n-2, 0), (n-2, 1), (n-1, 0), (n-1, 1)])

# for _ in range(m) :
#     direction, cnt = map(int, sys.stdin.readline().split())
#     l = len(q)
#     for _ in range(l) :
#         x, y = q.popleft()
#         q.append((move(x, y, direction-1, cnt)))
#     nq = []

#     while q : 
#         x, y = q.popleft()
#         board[x][y] += 1
#         nq.append((x, y))

#     for x, y in nq : 
#         count_diagonal_water(x, y)

#     for i in range(n):
#         for j in range(n) :
#             if not (i,j) in nq and board[i][j] >=2:
#                 q.append((i, j))
#                 board[i][j] -= 2

# answer = 0 
# for b in board : 
#     answer += sum(b)
# print(answer)
    

    


import sys 
from collections import deque
n, m  = map(int, sys.stdin.readline().split())
board = []
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

for _ in range(n) :
    board.append(list(map(int, sys.stdin.readline().split())))

def move(x, y, direction, cnt) :
    nx = (x + directions[direction][0]*(cnt%n) + n) % n 
    ny = (y + directions[direction][1]*(cnt%n) + n) % n
    return nx, ny

def count_diagonal_water(x, y) :
    for i in [1, 3, 5, 7] :
        nx = x + directions[i][0]
        ny = y + directions[i][1]
        if nx<0 or ny<0 or nx>=n or ny>=n or board[nx][ny]<1:
            continue
        board[x][y] += 1

q = deque()
q.extend([(n-2, 0), (n-2, 1), (n-1, 0), (n-1, 1)])

for _ in range(m) :
    visited=[[False]*n for _ in range(n)]
    direction, cnt = map(int, sys.stdin.readline().split())
    l = len(q)
    for _ in range(l) :
        x, y = q.popleft()
        q.append((move(x, y, direction-1, cnt)))
    nq = []

    while q : 
        x, y = q.popleft()
        board[x][y] += 1
        nq.append((x, y))
        visited[x][y] = True

    for x, y in nq : 
        count_diagonal_water(x, y)

    for i in range(n):
        for j in range(n) :
            if not visited[i][j] and board[i][j] >=2:
                q.append((i, j))
                board[i][j] -= 2

answer = 0 
for b in board : 
    answer += sum(b)
print(answer)