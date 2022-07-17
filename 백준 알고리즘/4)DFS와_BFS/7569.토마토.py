from collections import deque
global m, n, tomato, day
m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
answer = 0
d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def find_first_rotten_tomato(queue):
    global m, n, tomato
    for a in range(h):
        for b in range(n):
            for c in range(m):
                if tomato[a][b][c] == 1:
                    queue.append((a, b, c, 0))
    return queue

def check_all_rotten():
    global m, n, tomato
    for a in range(h):
        for b in range(n):
            for c in range(m):
                if tomato[a][b][c] == 0:
                    return False
    return True

def bfs():
    global m, n, tomato, answer
    queue = find_first_rotten_tomato(deque())
    if len(queue) == 0:
        answer = -1
        return 
    while queue:
        z, y, x, day = queue.popleft()
        answer = day
        for k in range(6):
            ny = y + d[k][0]
            nx = x + d[k][1]
            nz = z + d[k][2]
            if 0<=nz<h and 0<=ny<n and 0<=nx<m and tomato[nz][ny][nx]==0:
                tomato[nz][ny][nx] = 1
                queue.append((nz, ny,nx, day+1))
    if not check_all_rotten():
        answer = -1
        
bfs()     
print(answer)






