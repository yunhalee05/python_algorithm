import math


n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
cost = math.inf
result = 0

for i in range(0, n-1):
    if cost > prices[i]:
        cost = prices[i]
    result += (cost*distances[i])

print(result)
    
