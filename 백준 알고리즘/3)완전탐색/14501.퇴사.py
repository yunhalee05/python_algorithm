# global answer, n, consulting
# n = int(input())
# consulting = []
# for i in range(n):
#     a, b = map(int, input().split())
#     if i+a >n : 
#         consulting.append((0, 0))
#         continue
#     consulting.append((a, b))
# answer = 0

# def dfs(idx, pay):
#     global n, answer
#     answer = max(answer, pay)
#     for i in range(idx, n):
#         if consulting[i] == (0, 0) :
#             continue
#         if consulting[i][0]+idx <= n :
#             dfs(i+consulting[i][0], pay + consulting[i][1])
# dfs(0, 0)
# print(answer)


global answer, n, consulting
n = int(input())
consulting = []
answer = [0]*n
for i in range(n):
    a, b = map(int, input().split())
    if i+a >n : 
        consulting.append((0, 0))
        continue
    consulting.append((a, b))
    answer[i] = b

for i in range(n-2, -1, -1):
    if i + consulting[i][0] == n : 
        continue
    answer[i] += max(answer[i+consulting[i][0]:])

print(max(answer))