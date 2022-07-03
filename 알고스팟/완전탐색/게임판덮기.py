c = int(input())
coverType = [
    [[0,0], [0,1], [1, 0]], 
    [[0,0], [0, 1], [1, 1]],
    [[0,0], [1, 0], [1,1]],
    [[0,0], [1,0], [1,-1]]
]

def isCoverable(x, y, type, board):
    for dy, dx in type:
        nx = x + dx
        ny = y + dy
        if 0>nx or nx>=w or ny<0 or h<=ny :
            return False 
        elif board[ny][nx] == "#" :
            return False 
    return True 

def coverBoard(x, y, type, board, str):
    for dy, dx in type : 
        board[y + dy][x + dx] = str


def cover() :
    x, y = -1, -1

    #맨 윗칸부터 비워져있는 칸을 찾는다 
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "." : 
                y = i
                x = j
                break
        if y != -1 : break
    
    # 모두 순환한 경우 (보드가 모두 채워진 경우 )
    if (x == -1 or y == -1) : return 1
    result = 0 
    for type in coverType:
        if isCoverable(x, y, type, board) :
            coverBoard(x, y, type, board, "#")
            result += cover()
            coverBoard(x, y, type, board, ".")

    return result


for case in range(c) :
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    print(cover())
