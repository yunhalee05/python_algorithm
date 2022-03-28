#  *****
t = int(input())
answer = []

while t >0:
    t-= 1
    n = int(input())
    scores = []
    for _ in range(n):
        x, y = map(int, input().split())
        scores.append((x, y))

    cnt = 1
    scores.sort(key = lambda x : x[0])
    min = scores[0][1]
    for i in range(1,n):
        if scores[i][1]< min:
            min = scores[i][1]
            cnt +=1

    answer.append(cnt)

for i in answer:
    print(i)

