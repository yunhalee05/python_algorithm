import math

n, m = map(int, input().split())
box = []
for i in range(0, n):
    box.append(input())

count = []

for i in range(n-7):
    for j in range(m-7):
        res = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if k == i and j == l :
                     temp = box[i][j]
                else :
                    if temp != box[k][l]:
                        res += 1
                if l == j+7:
                    continue
                if temp == 'B':
                    temp = 'W'
                else :
                    temp = 'B'
        count.append(min(res, 64-res))

print(min(count))


