global n, board, check_row, check_col, check_right_diag, check_left_diag, answer
n = int(input())
answer = 0
board = [[False]*n for _ in range(n)]

check_row = [False]*n
check_col = [False]*n
check_right_diag = [False]*(2*n-1)
check_left_diag = [False]*(2*n-1)


def isPossiblePosition(i, j) :
    global n, board, check_row, check_col, check_right_diag, check_left_diag
    if board[i][j] == True:
        return False
    if check_col[j] == True:
        return False
    if check_row[i] == True:
        return False
    if check_right_diag[i+j] == True:
        return False
    if check_left_diag[n-(i-j)-1] == True:
        return False
    return True

def play_queen(i, j, isPut):
    global n, board, check_row, check_col, check_right_diag, check_left_diag
    board[i][j] = isPut
    check_row[i] = isPut
    check_col[j] = isPut
    check_right_diag[i+j] = isPut
    check_left_diag[n-(i-j)-1] = isPut

def find_case(depth):
    global answer, board, n, check_row, check_col, check_right_diag, check_left_diag
    if depth == n:
        answer += 1
        return 
    for col in range(n):
        if isPossiblePosition(depth, col):
            play_queen(depth, col, True)
            find_case(depth+1)
            play_queen(depth, col, False)
    return 

find_case(0)

print(answer)

# global n, board, check_row, answer
# n = int(input())
# answer = 0
# board = [0]*n
# visited = [False]*n

# def isPossiblePosition(depth) :
#     global n, board
#     for row in range(depth):
#         if abs(depth-row) == abs(board[depth]- board[row]):
#             return False
#     return True

# def find_case(depth):
#     global answer, board, n
#     if depth == n:
#         answer += 1
#         return 
#     for col in range(n):
#         if visited[col] == False:
#             board[depth] = col
#             if isPossiblePosition(depth) :
#                 visited[col] = True
#                 find_case(depth+1)
#                 visited[col] = False
#     return 
    
# find_case(0)

# print(answer)