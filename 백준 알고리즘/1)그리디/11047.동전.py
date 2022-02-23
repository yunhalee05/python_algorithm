n, k = map(int, input().split())
coins = []
result = 0

for i in range(n):
    coins.append(int(input()))

for i in reversed(range(n)):
    if k // coins[i] > 0:
        result += (k//coins[i])
        k = (k%coins[i])
    if k == 0 :
        break

print(result)

