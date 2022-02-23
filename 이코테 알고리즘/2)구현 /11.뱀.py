n, k = map(int,input().split())
snake = [[0]*(n+1) for i in range(n+1)]

for i in range(k):
    a, b = map(int, input().split())
    snake[a][b] = 1

L = int(input())
direction = []

for j in range(L):
    x,c = input().split()
    direction.append((int(x), c))

dx = [ 1, 0, -1, 0]
dy = [ 0, -1, 0, 1]

def turn(direction, c):
    if c=="L":
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

def simulate():
    x, y = 1, 1
    snake[1][1] = 2 #뱀존재는 2로 표시
    d = 0
    time = 0
    index = 0 #다음에 회전할 정보
    q = [(x, y)] #뱀 위치정보 

    while(True):
        # 게임종료

        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx<=n or ny<=n or nx>=1 or ny>=1 or snake[nx][ny]!=2:
            if snake[nx][ny]== 0:
                snake[x][y] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                snake[px][py] = 0
            if snake[nx][ny] ==1:
                snake[nx][ny] = 2
                q.append((nx, ny))
        else:
            time+=1
            break
            
        x, y = nx, ny
        time+=1

        if index<1  and time ==direction[index][0]:
            d = turn(d, direction[index][1])
            index+=1
    return time

print(simulate)








    








