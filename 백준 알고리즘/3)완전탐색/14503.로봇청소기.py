import sys 
global n, m, board, d, y, x, answer
answer = 0 
n, m = map(int, sys.stdin.readline().split())
board = [[] for _ in range(n)]
d = [ (-1, 0), (0, -1), (1, 0), (0, 1)]

y, x, direction = map(int, sys.stdin.readline().split())

if direction == 1 : 
    direction = 3
elif direction == 3:
    direction = 1


for i in range(n):
    board[i].extend(list(map(int, sys.stdin.readline().split())))

def cleaning(direction):
    global n, m , board, d, y, x, answer
    if board[y][x] == 0 : 
            board[y][x] = 2
            answer +=1
    while True : 
        isDirty = False
        for _ in range(4) :
            direction = (direction+1) %4
            ny = y + d[direction][0] 
            nx = x + d[direction][1]
            if ny<=0 or ny>=n-1 or nx<=0 or nx>=m-1 or board[ny][nx] == 1 or board[ny][nx] == 2: 
                continue
            y = ny
            x = nx
            answer += 1
            board[y][x] = 2
            isDirty = True 
            break

        if not isDirty : 
            if board[y + d[(direction + 2)%4][0]][x + d[(direction + 2)%4][1]] == 1:
                break
            else :
                y += d[(direction + 2)%4][0]
                x += d[(direction + 2)%4][1]

cleaning(direction)
print(answer)