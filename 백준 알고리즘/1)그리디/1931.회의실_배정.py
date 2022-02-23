n = int(input())
times = []
for i in range(n):
    a, b = map(int, input().split())
    times.append((a, b))

times.sort(key=lambda x:(x[1], x[0]))

count = 1
start = times[0]
for i in range(1, n):
    if times[i][0] >= start[1]:
        count += 1
        start = times[i]

print(count)
