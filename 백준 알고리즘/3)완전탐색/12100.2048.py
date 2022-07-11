global n, answer
n = int(input())
board = [[] for _ in range(n)]
for i in range(n):
    numbers = list(map(int, input().split()))
    board[i].extend(numbers)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
answer = 0 
def calc(board, y, x, dy, dx):
    global n
    if dy==0 and dx == 1:
        nx = n-1
        idx = n-1
        while nx > 0 :
            next_x = nx-1
            while next_x>-1 : 
                if board[y][next_x] != 0:
                    break
                next_x -=1
            if next_x< 0 : 
                nx = 0
                break
            if board[y][nx] !=0 and board[y][nx] == board[y][next_x] :
                num = board[y][nx]
                board[y][next_x] = 0 
                board[y][nx] = 0 
                board[y][idx] = num*2
                while board[y][idx] != 0 : 
                    idx -= 1
            elif board[y][nx] != 0 and idx != nx: 
                board[y][idx] = board[y][nx]
                board[y][nx] = 0
                idx -= 1
            elif board[y][nx]!= 0 : 
                idx -= 1
            nx = next_x
        if board[y][nx] != 0 : 
            board[y][idx] = board[y][nx]
            board[y][nx] = 0 
    elif dy==1 and dx == 0:
        ny = n-1
        idx = n-1
        while ny > 0 :
            next_y = ny-1
            while next_y>-1 :
                if board[next_y][x] != 0:
                    break
                next_y -=1
            if next_y< 0 : 
                ny = 0
                break
            if board[ny][x] != 0 and board[ny][x] == board[next_y][x] :
                num = board[ny][x]
                board[next_y][x] = 0 
                board[ny][x] = 0
                board[idx][x] = 2*num
                while board[idx][x] != 0 : 
                    idx -=1
            elif board[ny][x] != 0 and idx != ny: 
                board[idx][x] = board[ny][x]
                board[ny][x] = 0
                idx -= 1
            elif board[ny][x]!= 0 : 
                idx -= 1
            ny = next_y
        if board[ny][x] != 0 : 
            board[idx][x] = board[ny][x]
            board[ny][x] = 0 
    elif dy==0 and dx == -1:
        nx = 0
        idx = 0
        while nx < n :
            next_x = nx+1
            while next_x < n: 
                if board[y][next_x] != 0:
                    break
                next_x +=1
            if next_x>= n : 
                break
            if board[y][nx] != 0 and nx == n-1 : 
                board[y][idx] = board[y][nx]
                board[y][nx] = 0 
            elif board[y][nx] != 0 and board[y][nx] == board[y][next_x] :
                num = board[y][nx]
                board[y][nx] =0
                board[y][next_x] = 0 
                board[y][idx] = num*2
                while board[y][idx] != 0 :
                    idx += 1
            elif board[y][nx] != 0 and idx != nx: 
                board[y][idx] = board[y][nx]
                board[y][nx] = 0
                idx += 1
            elif board[y][nx]!= 0 : 
                idx += 1
            nx == next_x
    elif dy==-1 and dx == 0:
        ny = 0
        idx = 0
        while ny < n :
            next_y = ny+1
            while next_y<n : 
                if board[next_y][x] != 0:
                    break
                next_y +=1
            if next_y>= n : 
                break
            if board[ny][x] != 0 and ny == n-1 : 
                board[idx][x] = board[ny][x]
                board[ny][x] = 0 
            elif board[ny][x] != 0 and board[ny][x] == board[next_y][x] :
                num = board[ny][x]
                board[next_y][x] = 0 
                board[ny][x] = 0
                board[idx][x] = 2*num
                while board[idx][x] != 0 : 
                    idx +=1
            elif board[ny][x] != 0 and idx != ny: 
                board[idx][x] = board[ny][x]
                board[ny][x] = 0
                idx += 1
            elif board[ny][x] != 0:
                idx += 1
            ny = next_y
    return board

def find_max(board):
    max_num = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]> max_num:
                max_num = board[i][j]
    return max_num

def dfs(board, cnt) :
    global n, answer
    if cnt == 5:
        answer = max(answer, find_max(board))
        return 
    for i in range(4):
        b = [x[:] for x in board]
        if i == 0 or i == 2 : 
            for j in range(n):
                n_b = calc(b, j, n, dy[i], dx[i])
            dfs(n_b, cnt +1)
        else : 
            for j in range(n):
                n_b = calc(b, n, j, dy[i], dx[i])
            dfs(n_b, cnt +1)
    
# dfs(board, 0)
print(calc(board, 0, 0, 0, 1))
print(answer)