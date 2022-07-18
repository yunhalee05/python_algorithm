global n, k, product, isUsed
n, k = map(int, input().split())
product = []
dp = [0] * (k+1)
for _ in range(n):
    w, v = map(int, input().split())
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j-w]+v, dp[j])
print(max(dp))

