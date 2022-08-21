from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[0]*101 for _ in range(101)]
    visited = [[False]*101 for _ in range(101)]
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    for rec in rectangle :
        left_x, left_y, right_x, right_y = map(lambda x : x*2, rec)
        for i in range(left_x, right_x + 1) :
            for j in range(left_y, right_y + 1):
                if left_x < i <right_x and left_y < j < right_y :
                    board[i][j] = -1
                elif board[i][j] != -1 :
                    board[i][j] = 1
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append((characterX, characterY))
    visited[characterX][characterY] = True
    
    while q :
        x, y = q.popleft()
        if (x, y) == (itemX, itemY):
            answer = (board[x][y] -1)//2
            break
        for direction in directions : 
            nx = x + direction[0]
            ny = y + direction[1]
            if 0<= nx <101 and 0<= ny < 101 and board[nx][ny] == 1 and not visited[nx][ny] : 
                board[nx][ny] = board[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))
    return answer