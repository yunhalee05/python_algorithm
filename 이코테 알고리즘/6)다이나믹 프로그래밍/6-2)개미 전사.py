n = int(input())
k  = list(map(int, input().split())

dp  = [0]*101
dp[0] = k[0]
dp[1] = k[1]
dp[2] = k[0]+ k[2]

for i in range(3, n):
    dp[2] = max(dp[i-2]+k[i], dp[i-1]))

print(dp[n-1])
