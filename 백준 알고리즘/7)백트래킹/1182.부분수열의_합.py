from itertools import combinations


n, s = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

# for i in range(1, n+1):
#     for j in list(combinations(numbers, i)):
#         if sum(j) == s:
#             answer +=1

# print(answer)


def dfs(node, sum):
    global answer
    if node >= n:
        return 
    if sum == s:
        answer += 1
        return
    dfs(node+1, sum)
    dfs(node+1, sum+numbers[node])

dfs(0, 0)
print(answer)


    
