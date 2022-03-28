n = int(input())
weight = []
for _ in range(n):
    weight.append(int(input()))

answer = 0
weight.sort()

for i in range(n):
    maxWeight = len(weight)* min(weight)
    if answer < maxWeight:
        answer = maxWeight
    weight.pop(0)

print(answer)

