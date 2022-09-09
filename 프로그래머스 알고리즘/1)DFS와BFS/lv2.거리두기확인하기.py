from collections import deque
def solution(places):
    answer = []
    
    def is_in_distance(place, i, j) : 
        q = deque([(i, j, 0)])
        visited = [[False]*5 for _ in range(5)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited[i][j] = True
        while q : 
            x, y, d = q.popleft()
            if d == 2 : 
                continue
            for i in range(4) :
                nx = x + directions[i][0]
                ny = y + directions[i][1]
                if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] :
                    if place[nx][ny] == 'P' :
                        return True
                    elif place[nx][ny] == 'O':
                        q.append((nx, ny, d + 1))
                        visited[nx][ny] = True
        return False 
        
    for place in places : 
        ans = 1
        for i in range(5) :
            isBreak = False
            for j in range(5) :
                if place[i][j] == 'P' :
                    if is_in_distance(place, i, j) :
                        ans = 0 
                        isBreak = True
                        break
            if isBreak : 
                break
                
        answer.append(ans)
    return answer
