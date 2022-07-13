# from collections import deque
# n, m, y, x, k = map(int, input().split())
# board = [[] for _ in range(n)]
# for i in range(n):
#     num = list(map(int, input().split()))
#     board[i].extend(num)
# directions = list(map(int, input().split()))
# # 동서북남 방향 
# d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# global dice_row, dice_column
# dice_row = deque([0, 0, 0])
# dice_column = deque([0, 0, 0, 0])

# def roll_dice(direction, num):
#     global dice_row, dice_column
#     if direction == 1 : 
#         upper = dice_column.pop()
#         dice_column.append(dice_row.popleft())
#         dice_row.append(upper)
#         dice_column[1] = dice_row[1]
#     elif direction == 2:
#         upper = dice_column.pop()
#         dice_column.append(dice_row.pop())
#         dice_row.appendleft(upper)
#         dice_column[1] = dice_row[1]
#     elif direction == 3:
#         dice_column.appendleft(dice_column.pop())
#         dice_row[1] = dice_column[1]
#     elif direction == 4 : 
#         dice_column.append(dice_column.popleft())
#         dice_row[1] = dice_column[1]
#     bottom = dice_column[1]
#     if num != 0  : 
#         dice_column[1] = num
#         dice_row[1] = num 
#     return bottom 

# for direction in directions:
#     ny = y + d[direction-1][0]
#     nx = x + d[direction-1][1]
#     if nx<0 or m<=nx or ny<0 or n<=ny :
#         continue 
#     y, x = ny, nx 
#     if board[y][x] == 0 :
#         board[y][x] = roll_dice(direction, board[y][x])
#     else : 
#         roll_dice(direction, board[y][x])
#         board[y][x] = 0
#     print(dice_column[3])



n, m, y, x, k = map(int, input().split())
board = [[] for _ in range(n)]
for i in range(n):
    num = list(map(int, input().split()))
    board[i].extend(num)
directions = list(map(int, input().split()))
# 동서북남 방향 
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
global dice
# 왼, 오, 앞, 뒤, 상, 하 
dice = [0, 0, 0, 0, 0, 0]

def roll_dice(direction, num):
    global dice
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 동 
    if direction == 1 : 
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, f, c, d, b, a
    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = f, e, c, d, a, b
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = a, b, e, f, d, c
    elif direction == 4 : 
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = a, b, f, e, c, d
    bottom = dice[4]
    if num != 0  : 
        dice[4] = num 
    return bottom 

for direction in directions:
    ny = y + d[direction-1][0]
    nx = x + d[direction-1][1]
    if nx<0 or m<=nx or ny<0 or n<=ny :
        continue 
    y, x = ny, nx 
    if board[y][x] == 0 :
        board[y][x] = roll_dice(direction, board[y][x])
    else : 
        roll_dice(direction, board[y][x])
        board[y][x] = 0
    print(dice[5])



