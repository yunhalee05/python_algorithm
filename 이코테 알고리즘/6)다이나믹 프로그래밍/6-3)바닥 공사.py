n = int(input())

dp = [0]*10001
dp[1] = 1
dp[2] = 3

for i in range (3, n):
    dp[i] = (dp[i-1]+d[i-2]*2)%796796

print(dp[n])
