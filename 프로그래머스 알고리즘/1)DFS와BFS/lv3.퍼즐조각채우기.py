import copy
def solution(game_board, table):
    def dfs(graph, x, y, position, n, num) :
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = [position]
        for i, j in directions:
            nx, ny = x+i, y+j
            if 0<= nx <n and 0<=ny<n and graph[nx][ny] == num : 
                graph[nx][ny] = 2
                result += dfs(graph, nx, ny, [position[0]+i, position[1]+j], n, num)
        return result 
    
    def rotate(graph) :
        n = len(graph)
        result = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n) :
                result[j][n-1-i] = graph[i][j]
        return result            
            
    answer = 0
    game_board_copy = copy.deepcopy(game_board)
    n = len(game_board)
    blocks = []
    
    for i in range(n) :
        for j in range(n) :
            if game_board_copy[i][j] == 0 :
                game_board_copy[i][j] = 2
                blocks.append(dfs(game_board_copy, i, j, [0,0], n, 0))
    for k in range(4) :
        table = rotate(table)
        table_rotate_copy = copy.deepcopy(table)
        for i in range(n) :
            for j in range(n) :
                if table_rotate_copy[i][j] == 1 :
                    table_rotate_copy[i][j] = 2
                    block = dfs(table_rotate_copy, i, j, [0, 0], n, 1)
                    if block in blocks:
                        blocks.pop(blocks.index(block))
                        answer += len(block)
                        table = copy.deepcopy(table_rotate_copy)
                    else : 
                        table_rotate_copy = copy.deepcopy(table)
    return answer