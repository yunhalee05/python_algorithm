n = int(input())
times = list(map(int, input().split()))
result = []

times.sort()

for i in range(1, n):
    times[i] += times[i-1]

print(sum(times))
