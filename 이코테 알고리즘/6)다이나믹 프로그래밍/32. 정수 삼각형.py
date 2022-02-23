n = int(input())

array = list(map(int, input().split()))

dp = []
index =0

for i in range(n):
    dp.append(array[index]:array[index+i])
    index += i

for i in range(1, n):
    for j in range(i+1):
        if j==0:
            left_up = 0
        else :
            left_up = dp[i-1][j-1]
        if j==i:
            right_up = 0
        else:
            right_up = dp[i-1][j]
        dp[i][j]= dp[i][j]+ max(left_up, right_up)
    
result = 0
for i in range(n):
    result = max(result, dp[n-1][i])

# print(max(dp[n-1]))
print(result)
        

