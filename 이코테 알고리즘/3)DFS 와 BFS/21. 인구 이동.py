from collections import deque

n, l, r = map(int, input().split())
s = []

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def process(x, y, index){
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = A[x][y]
    cnt = 1
    
    while q:
        x, y = q.popleft()
            
        for i in range(4):
            nx = x+ dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                if  l<=abs(A[x][y]- A[nx][ny]) and abs(A[x][y]- A[nx][ny])<=r:
                    q.append((nx, ny))
                    union[x][y] = index
                    summary += A[nx][ny]
                    cnt +=1
                    united.append((nx, ny))
        for i, j in united:
            A[i][j] = summary//count
        return cnt 
}

total_cnt = 0

while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] ==-1:
                process(i, j , index)
                index +=1

    if index ==n*n:
        break
    total_cnt +=1



print(total_cnt))
