def solution(rows, columns, queries):
    answer = []
    board = [[(j*columns + i) for i in range(1, columns +1)] for j in range(rows)]
    for start_x, start_y, end_x, end_y in queries : 
        tmp = board[start_x-1][start_y-1]
        minimum = tmp
        x, y = start_x-1, start_y-1
        for col in range(start_x, end_x) : 
            board[x][y] = board[col][y]
            minimum = min(minimum, board[x][y])
            x = col
        for row in range(start_y, end_y) :
            board[x][y] = board[x][row]
            minimum = min(minimum, board[x][y])
            y = row
        for col in range(end_x-1, start_x-2, -1) :
            board[x][y] = board[col][y]
            minimum = min(minimum, board[x][y])
            x = col
        for row in range(end_y-1, start_y-2, -1) :
            board[x][y] = board[x][row]
            minimum = min(minimum, board[x][y])
            y = row
        board[start_x-1][start_y] = tmp
        answer.append(minimum)

    return answer