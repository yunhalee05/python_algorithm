n = int(input())
grid = []
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
d_ = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
for i in range(n) :
    grid.append(list(map(int, input().split())))

dp =[[[0]*4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
result = [[1]*len(grid[0]) for _ in range(len(grid))]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        for k in range(4):
            max_length = 1
            nx = i
            ny = j 
            while True:
                nx += d[k][0]
                ny += d[k][1]
                if nx>=len(grid) or nx<0 or ny>=len(grid[0]) or ny<0 : 
                    break
                if grid[nx][ny] == grid[i][j] : 
                    max_length += 1
                else : 
                    break
            dp[i][j][k] = max_length

for i in range(len(grid)):
    for j in range(len(grid[0])) :
        for k in range(4) :
            nx = i 
            ny = j 
            if dp[i][j][k] > 1 :
                for l in range(2, dp[i][j][k]) :
                    nx += d_[k][0]
                    ny += d_[k][1]
                    if nx>=len(grid) or nx<0 or ny>=len(grid[0]) or ny<0 : 
                        break
                    
    
print(dp)


                






# 6
# 2 1 1 3 5 1 
# 1 1 3 3 5 5 
# 8 3 3 3 1 5 
# 3 3 3 4 4 4 
# 3 3 4 4 4 4 
# 1 4 4 4 4 4 

# 3 
# 10 20 30 
# 40 50 60 
# 70 80 90 

# 2
# 1 1 1 1 
# 1 1 1 1 