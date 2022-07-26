import sys 
global gear
gear = [[] for _ in range(4)]

for i in range(4):
    gear[i].extend([sys.stdin.readline(), 0])

k = int(sys.stdin.readline())

d = []

for _ in range(k):
    num, direction = map(int, sys.stdin.readline().split())
    d.append((num-1, direction))

def rotation(num, direction) :
    global gear 
    isCirculable = [0] * 4
    tmp1, tmp2 = num-1, num+1
    c1, c2 = direction*-1, direction * -1
    isCirculable[num] = direction

    while tmp1>-1 :
        if gear[tmp1][0][(gear[tmp1][1] + 2)%8] == gear[tmp1+1][0][(gear[tmp1+1][1] + 6)%8]:
            break
        isCirculable[tmp1] = c1
        c1 *= -1
        tmp1 -= 1
    
    while tmp2<4 :
        if gear[tmp2-1][0][(gear[tmp2-1][1] + 2)%8] == gear[tmp2][0][(gear[tmp2][1] + 6)%8]:
            break
        isCirculable[tmp2] = c2
        c2 *= -1
        tmp2 += 1
    
    for index, c in enumerate(isCirculable) :
        if c == 0 : 
            continue
        elif c == 1 : 
            gear[index][1] = (gear[index][1]-1 + 8)%8
        elif c == -1 : 
            gear[index][1] = (gear[index][1]+1)%8
    

for di in d:
    rotation(di[0], di[1])

answer = 0
for i in range(4) : 
    answer += (pow(2, i) * (gear[i][0][gear[i][1]]=='1'))

print(answer)