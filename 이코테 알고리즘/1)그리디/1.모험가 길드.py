n = int(input())
members = list(map(int, input().split()))

result = 0
members.sort()
cnt = 0
for i in members:
    cnt += 1
    if cnt >= i :
        result +=1
        cnt = 0

print(result)