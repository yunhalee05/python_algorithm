import sys 
global n, d, board
n = int(sys.stdin.readline())
students = [[] for _ in range(n*n+1)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
students_order = []
board = [[0]*n for _ in range(n)]

for i in range(n*n) :
    s = list(map(int, sys.stdin.readline().split()))
    students[s[0]].extend(s[1:])
    students_order.append(s[0])
    
def find_first_empty_board():
    global board 
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 :
                return i, j 

def find_location(num, numbers) :
    global board, n, d
    max_like = 0
    max_empty = 0
    x,y = find_first_empty_board()
    for i in range(n) :
        for j in range(n) :
            if board[i][j] != 0 :
                continue
            like = 0 
            empty =0 
            for k in range(4):
                nx = i + d[k][0]
                ny = j + d[k][1]
                if nx<0 or ny<0 or nx>=n or ny>=n : 
                    continue
                if board[nx][ny] == 0 : 
                    empty += 1
                if board[nx][ny] in numbers:
                    like += 1
            if like > max_like :
                max_like = like 
                max_empty = empty
                x = i
                y = j 
            elif like == max_like and max_empty<empty :
                max_empty = empty 
                x = i 
                y = j 
    board[x][y] = num 


def calculate_happiness(students) :
    global board, n, d
    total = 0 
    for i in range(n):
        for j in range(n):
            cnt = 0 
            for k in range(4):
                nx = i + d[k][0]
                ny = j + d[k][1]
                if nx<0 or ny<0 or nx>=n or ny>=n : 
                    continue
                if board[nx][ny] in students[board[i][j]]:
                    cnt += 1  
            if cnt == 0 : 
                total += cnt  
            else :
                total += (10**(cnt-1)) 
    return total 

for o in students_order : 
    find_location(o, students[o])

print(calculate_happiness(students))
