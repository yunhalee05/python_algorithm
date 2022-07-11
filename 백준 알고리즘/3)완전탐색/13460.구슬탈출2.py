n, m = map(int, input().split())
board = [0]*n
visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

y_b,x_b,x_r, y_r = 0, 0, 0, 0
q = []
for i in range(n):
    s = input() 
    board[i] = list(s)
    for j in range(m) : 
        if board[i][j] == 'B':
            y_b = i
            x_b = j
        elif board[i][j] == 'R':
            y_r = i
            x_r = j


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def move(board, x, y, dx, dy):
    cnt = 0 
    while board[y+dy][x + dx] != '#' and  board[y][x] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt 

def bfs(board, y_b, x_b, y_r, x_r, cnt):
    q.append([y_b, x_b, y_r, x_r, 0])
    visited[y_b][x_b][y_r][x_r] =1
    while q : 
        y_b, x_b, y_r, x_r, cnt = q.pop(0)
        if cnt > 10 : 
            return 
        for i in range(4):
            nx_b, ny_b, cnt_b = move(board, x_b, y_b, dx[i], dy[i])
            nx_r, ny_r, cnt_r = move(board, x_r, y_r, dx[i], dy[i])
            if board[ny_b][nx_b] == 'O':
                continue
            if board[ny_r][nx_r] == 'O':
                print(cnt+1)
                return 
            elif nx_b == nx_r and ny_b == ny_r : 
                if cnt_b> cnt_r : 
                    nx_b -= dx[i]
                    ny_b -= dy[i]
                else :
                    nx_r -= dx[i]
                    ny_r -= dy[i]
                if visited[ny_b][nx_b][ny_r][nx_r] == 0:
                    q.append([ny_b,nx_b, ny_r,nx_r, cnt + 1])
                    visited[ny_b][nx_b][ny_r][nx_r] =1
    print(-1) 

bfs(board, y_b, x_b, y_r,x_r, 0)

