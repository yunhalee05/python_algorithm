# n = int(input())
# rope = []
# dp = [[0]*n for _ in range(n)]
# answer = 0
# for _ in range(n):
#     a, b = map(int, input().split())
#     rope.append((a, b))

# for i in range(n-1):
#     for j in range(i+1, n):
#         a, b = rope[i]
#         c, d = rope[j]
#         if a>c and b<d or a<c and b>d:
#             dp[i][j] = 1

# for i in range(n):
#     if max(dp[i])>0:
#         answer+=1
# print(answer)


n = int(input())
rope = []
dp = [1]*n
for _ in range(n):
    a, b = map(int, input().split())
    rope.append((a, b))
rope.sort()

for i in range(1, n):
    for j in range(i):
        if rope[i][1] > rope[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n- max(dp))