from collections import deque

for t in range(int(input())):
    n= int(input())
    indegree = [0]*(n+1)
    graph = [[False]*(n+1) for _ in range(n+1)]
    score = list(map(int, input().split))
    for i in range(n):
        for j in range(n):
            graph[score[i][score[j]]] = True
            indegree[score[j]] +=1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -=1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[b] +=1
            indegree[a] -=1
    
    result = []

    q = deque()

    for i in range(n+1):
        if indegree[i] ==0:
            q.append(i)
    
    certain = True
    cycle = False

    for i in range(n):
        if len(q) ==0:
            cycle = True
            break
        if len(q)>= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j]:
                indegree-=1
                if indegree[j] ==0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end = ' ')
        print()