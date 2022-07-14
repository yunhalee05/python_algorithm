# from itertools import combinations
# from math import inf

# n = int(input())
# people = [i for i in range(n)]
# global power
# power = [[] for _ in range(n)]
# for i in range(n):
#     power[i].extend(list(map(int, input().split())))

# teams = list(combinations(people, n//2))

# min_sub = inf

# def getScore(pairs) :
#     global power
#     score = 0 
#     for pair in pairs : 
#         if pair[0] == pair[1] :
#             continue
#         score += (power[pair[0]][pair[1]] + power[pair[1]][pair[0]])
#     return score

# for i in range(len(teams)//2):
#     t_start = teams[i]
#     t_link = teams[len(teams)-1-i]

#     s_pairs = list(combinations(t_start, 2))
#     l_pairs = list(combinations(t_link, 2))

#     min_sub = min(min_sub, abs(getScore(s_pairs)- getScore(l_pairs)))


# print(min_sub)




from itertools import combinations
from math import inf
global n, power, visited, min_sub
n = int(input())
power = [[] for _ in range(n)]
for i in range(n):
    power[i].extend(list(map(int, input().split())))
visited = [False]*(n)
min_sub = inf

def dfs(depth, idx):
    global n, power, visited, min_sub
    if depth == n//2 : 
        t_start, t_link = 0, 0 
        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    t_start += (power[i][j] + power[j][i])
                elif not visited[i] and not visited[j]:
                    t_link += (power[i][j] + power[j][i])
        min_sub = min(min_sub, abs(t_start - t_link))

    else : 
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                dfs(depth + 1, i)
                visited[i] = False

dfs(0, 0)
print(min_sub)



