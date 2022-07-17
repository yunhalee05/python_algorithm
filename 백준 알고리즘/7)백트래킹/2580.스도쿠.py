# from collections import deque
# board = [[] for _ in range(9)]

# location = deque()
# for i in range(9):
#     numbers = list(map(int, input().split()))
#     for j in range(9):
#         if numbers[j] == 0:
#             location.append((i, j))
#     board[i].extend(numbers)
# number = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# while location:
#     i, j = location.pop() 
#     # 가로열 검사 
#     r = number - set(board[i])
#     if len(r) == 1:
#         board[i][j] = list(r)[0]
#         continue

#     # 세로열 검사 
#     c = set()
#     for k in range(9):
#         c.add(board[k][j])
#     c = number - c
#     if len(c) == 1:
#         board[i][j] = list(c)[0]
#         continue

#     # 박스 검사 
#     box = set()
#     for a in range((i//3)*3, (i//3*3) + 3):
#         for b in range((j//3)*3, (j//3)*3 +3):
#             box.add(board[a][b])
#     box = number - box
#     if len(box) == 1:
#         board[i][j] = list(box)[0]
#         continue

#     # 공통 필요인자 검사해서 채워넣기 
#     possible = list(r & c & box)
#     if len(possible) == 1:
#         board[i][j] = possible[0]
#         continue

#     # 아직 정확한 필요인자 모르면 다시 추가 
#     location.appendleft((i, j))

# for i in range(9):
#     for j in range(9):
#         print(board[i][j], end=' ')
#     print()

# global board, isFinished
# board = []
# location = []
# for i in range(9):
#     board.append(list(map(int, input().split())))
#     for j in range(9):
#         if board[i][j] == 0:
#             location.append((i, j))

# def isPossible(i, j , num):
#     global board
#     for a in range(9):
#         # 가로열 검사 
#         if num == board[i][a]:
#             return False
#         # 세로열 검사 
#         if num == board[a][j]:
#             return False
#     # 박스 검사 
#     row = (i//3)*3
#     column = (j//3)*3
#     for a in range(row, row + 3):
#         for b in range(column, column +3):
#             if board[a][b] == num : 
#                 return False
#     return True

# def dfs(idx):
#     global isFinished
#     if idx == len(location):
#         isFinished = True
#         return 
#     i, j = location[idx]
#     for num in range(1, 10):
#         if isPossible(i, j, num):
#             board[i][j] = num 
#             dfs(idx + 1)
#             if isFinished:
#                 return 
#             board[i][j] = 0 
#     return 

# isFinished = False
# dfs(0)
# for i in range(9):
#     for j in range(9):
#         print(board[i][j], end=' ')
#     print()



# global board, isFinished
# board = []
# location = []
# for i in range(9):
#     board.append(list(map(int, input().split())))
#     for j in range(9):
#         if board[i][j] == 0:
#             location.append((i, j))

# def isPossible(i, j):
#     possible_num = [1,2,3,4,5,6,7,8,9]
#     global board
#     for a in range(9):
#         # 가로열 검사 
#         if board[i][a] in possible_num:
#             possible_num.remove(board[i][a])
#         # 세로열 검사 
#         if board[a][j] in possible_num:
#             possible_num.remove(board[a][j])
#     # 박스 검사 
#     row = (i//3)*3
#     column = (j//3)*3
#     for a in range(row, row + 3):
#         for b in range(column, column +3):
#             if board[a][b] in possible_num : 
#                 possible_num.remove(board[a][b])
#     return possible_num

# def dfs(idx):
#     global isFinished
#     if idx == len(location):
#         isFinished = True
#         return 
#     i, j = location[idx]
#     possible_num = isPossible(i, j)
#     for num in possible_num:
#         board[i][j] = num 
#         dfs(idx + 1)
#         board[i][j] = 0 
#     return 

# isFinished = False
# dfs(0)
# for i in range(9):
#     for j in range(9):
#         print(board[i][j], end=' ')
#     print()


# global board, isFinished
# board = []
# location = []
# for i in range(9):
#     board.append(list(map(int, input().split())))
#     for j in range(9):
#         if board[i][j] == 0:
#             location.append((i, j))

# def isPossible(i, j):
#     possible_num = [1,2,3,4,5,6,7,8,9]
#     global board
#     for a in range(9):
#         # 가로열 검사 
#         if board[i][a] in possible_num:
#             possible_num.remove(board[i][a])
#         # 세로열 검사 
#         if board[a][j] in possible_num:
#             possible_num.remove(board[a][j])
#     # 박스 검사 
#     row = (i//3)*3
#     column = (j//3)*3
#     for a in range(row, row + 3):
#         for b in range(column, column +3):
#             if board[a][b] in possible_num : 
#                 possible_num.remove(board[a][b])
#     return possible_num
    
# isFinished = False
# def dfs(idx):
#     global isFinished
#     if isFinished:
#         return 
#     if idx == len(location):
#         for i in board:
#             print(*i)
#         isFinished = True
#         exit() 
#     i, j = location[idx]
#     possible_num = isPossible(i, j)
#     for num in possible_num:
#         board[i][j] = num 
#         dfs(idx + 1)
#         if not isFinished:
#             board[i][j] = 0 
#     return 

# dfs(0)

global board
board = []
location = []
check_row = [[False]*10 for _ in range(9)]
check_col = [[False]*10 for _ in range(9)]
check_box = [[False]*10 for _ in range(9)]
for i in range(9):
    board.append(list(map(int, input().split())))
    for j in range(9):
        if board[i][j] == 0:
            location.append((i, j))
        else :
            check_row[i][board[i][j]] = True
            check_col[j][board[i][j]] = True
            check_box[(i//3)*3 + j//3][board[i][j]] = True

def fill_board(idx):
    if idx == len(location):
        for i in board:
            print(*i)
        return True
    i, j = location[idx]
    for a in range(1, 10):
        if check_row[i][a] == False and check_col[j][a]==False and check_box[(i//3)*3 + j//3][a] == False:
            check_row[i][a] = check_col[j][a] = check_box[(i//3)*3 + j//3][a] = True
            board[i][j] = a 
            if fill_board(idx + 1):
                return True
            board[i][j] = 0 
            check_row[i][a] = check_col[j][a] = check_box[(i//3)*3 + j//3][a] = False
    return False

fill_board(0)
