c = int(input())
def countPair():
    cnt = 0 
    first = -1
    for i in range(n):
        if not visited[i]:
            first = i 
            break
    if first == -1 :  return 1
    for i in range(first, n):
        if not visited[i] and isFriends[i][first]:
            visited[i] = visited[first] = True
            cnt += countPair()
            visited[i] = visited[first] = False
    return cnt 

for case in range(c) :
    n, m = map(int, input().split())
    isFriends = [[False]*n for _ in range(n)]  
    visited = [False]*n  
    pair = list(map(int, input().split()))
    for i in range(0, len(pair), 2):
        isFriends[pair[i]][pair[i+1]] = isFriends[pair[i+1]][pair[i]] = True
    print(countPair())



