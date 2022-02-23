dp = [0]* 300001

for i in range(2, 30000) :
    dp[i] = d[i-1]+1
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%5==0:
        dp[i] = min(dp[i], dp[i//5]+1)


x = int(input())
print(dp[x])



