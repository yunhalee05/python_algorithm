n = int(input())
cnt1, cnt2, cnt3 = 0, 0, 0 
paper = [[] for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    paper[i].extend(a)

def checkFull(start_x, start_y, end_x, end_y):
    initial = paper[start_y][start_x]
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            if paper[i][j] != initial : 
                return False
    return True 

def cut (start_y, end_y, start_x, end_x) :
    global cnt1, cnt2, cnt3
    if checkFull(start_x, start_y, end_x, end_y) or  (end_y-start_y)//3==0 or (end_x-start_x)//3 == 0: 
        if paper[start_y][start_x] == -1 : 
            cnt1 += 1
        elif paper[start_y][start_x] == 0:
            cnt2 +=1
        else : cnt3 += 1
        return 
    for i in range(start_y, end_y, (end_y-start_y)//3):
        for j in range(start_x, end_x, (end_x-start_x)//3):
            cut(i, i+ (end_y-start_y)//3, j, j+(end_x-start_x)//3) 
    return 
    
cut(0, n, 0, n)
print(cnt1)
print(cnt2)
print(cnt3)
    
    