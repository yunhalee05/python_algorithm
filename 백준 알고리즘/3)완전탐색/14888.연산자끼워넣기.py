from math import inf
import sys 

global n, numbers, operators, maximum, minimum
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))

maximum = -inf 
minimum = inf

def dfs(depth, result) :
    global n, operators, maximum, minimum 
    if depth == n:
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return 
    
    if operators[0] :
        operators[0] -= 1
        dfs(depth + 1, result + numbers[depth]) 
        operators[0] += 1
    if operators[1] :
        operators[1] -= 1
        dfs(depth + 1, result - numbers[depth]) 
        operators[1] += 1
    if operators[2] :
        operators[2] -= 1
        dfs(depth + 1, result * numbers[depth]) 
        operators[2] += 1
    if operators[3] :
        operators[3] -= 1
        dfs(depth + 1, int(result / numbers[depth])) 
        operators[3] += 1

dfs(1, numbers[0])
print(maximum)
print(minimum)