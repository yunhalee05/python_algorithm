# global n, answer , x, y, cnt, d,toward
# n = int(input())
# apple = int(input())
# board = [[0]*n for i in range(n)]

# for i in range(apple):
#     a, b = map(int, input().split())
#     board[a-1][b-1] = -1

# answer = 1
# y , x = 0, 0
# board[0][0] = 1
# toward = 0 
# cnt = 1
# d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# def search(time, direction) :
#     global answer, board, toward, n, x, y, cnt, d
#     time -= (answer-1) 
#     for _ in range(time) : 
#         ny = y + d[toward][0]
#         nx = x + d[toward][1]
#         answer += 1
#         if nx<0 or nx>=n or ny<0 or ny>=n or (board[ny][nx]>0 ) : 
#             return True 
#         elif board[ny][nx] == -1: 
#             board[ny][nx] = answer
#         else :
#             board[ny][nx] = answer
#             t_y, t_x = findTail(cnt)
#             board[t_y][t_x] = 0
#             cnt += 1
#         y = ny
#         x = nx
#     if direction == 'D':
#         toward = (toward+1) % 4
#     elif direction == 'L':
#         toward = (toward-1) % 4 
#     return False 

# def findTail(cnt):
#     global board
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == cnt : 
#                 return i, j 
#     return 0, 0 

# m = int(input())
# for i in range(m):
#     a, b = map(str,input().split())
#     isFinished = search(int(a), b)
#     if isFinished:
#         break
#     elif i == m-1 :
#         if d[toward][0] != 0 :
#             answer += (y+1)
#         elif d[toward][1] != 0 :
#             answer += (x+1)

# print(answer-1)

from collections import deque
n = int(input())
apple = int(input())
board = [[0]*n for i in range(n)]
directions = {}
for i in range(apple):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
m = int(input())
for i in range(m):
    a, b = map(str,input().split())
    directions[int(a)] =  b

answer = 0
queue = deque()
queue.append((0,0))
toward = 0 
x, y = 0, 0 
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def turn(direction) :
    global toward
    if direction == 'D':
        toward = (toward+1) % 4
    elif direction == 'L':
        toward = (toward-1) % 4 

while True : 
    y += d[toward][0]
    x += d[toward][1]
    answer += 1
    if x<0 or x>=n or y<0 or y>=n or (board[y][x]==2):
        break
    if board[y][x] != 1: 
        t_y, t_x = queue.popleft()
        board[t_y][t_x] = 0 
    board[y][x] = 2
    queue.append((y, x))
    if answer in directions.keys():
        turn(directions[answer])

print(answer)


        

        




