# ******************

n, E, W, S, N = map(int, input().split())
percentage = [E, W, S, N]
graph = [[0]*(n*2+1) for _ in range(n*2+1)]
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt, percent):
    global answer
    if cnt == n:
        answer += percent
        return 
    for i in range(4):
        if percentage[i] == 0:
            continue
        nx = x+dx[i]
        ny = y+dy[i]
        if graph[nx][ny] ==0 :
            graph[nx][ny] = 1
            dfs(nx, ny, cnt+1, percent * (percentage[i]*0.01))
            graph[nx][ny] = 0

graph[n][n] = 1
dfs(n, n , 0, 1)

print(answer)
