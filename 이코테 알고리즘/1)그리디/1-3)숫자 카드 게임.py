n, m = map(int, input().split())
result = 0

for i in range (n):
    numbers = list(map(int, input().split()))
    minimum = min(numbers)
    result = max(minimum, result)

print(result)

