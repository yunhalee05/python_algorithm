# ****************************
 
 
n = int(input())
numbers = [1, 2, 3]

# 좋은 수열 판별 함수 
def check(num):
    for idx in range(1, len(num)//2 +1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    return True

# 만족하는 수열 찾기 백트래킹
def dfs(num):
    global n, numbers
    if len(num) == n:
        print(num)
        exit()
    for i in numbers:
        if check(num + str(i)):
            dfs(num + str(i))
    
dfs('1')