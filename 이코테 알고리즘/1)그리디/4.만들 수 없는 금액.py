n = int(input())
coins = list(map(int, input()))

coins.sort()
target = 1
for i in coins:
    if target < i :
        break
    else :
        target += i

print(target)



