from itertools import combinations


def dfs(idx, cnt):
    if cnt == 6:
        for i in range(k):
            if visited[i] == 1:
                print(s[i], end=' ')
        print()
        return 
    for i in range(idx, k):
        visited[i] = 1
        dfs(i+1, cnt+1)
        visited[i] = 0

while True :
    str = input()
    if str == '0' :
        break
    s = list(map(int, str.split()))
    k = s.pop(0)
    visited = [0]*(max(s)+1)
    dfs(0, 0)
    print()



# combinations
while True :
    str = input()
    if str == '0' :
        break
    s = list(map(int, str.split()))
    k = s.pop(0)
    answer = list(combinations(s, 6))
    for i in answer:
        for j in i:
            print(j, end=' ')
        print()

    print()








   




