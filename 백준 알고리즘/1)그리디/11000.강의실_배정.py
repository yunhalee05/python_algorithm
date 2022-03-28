import heapq


n = int(input())
times = []
for _ in range(n):
    x, y = map(int, input().split())
    times.append((x,y))

answer = []

times.sort(key = lambda element : (element[0], element[1]- element[0]))
heapq.heappush(answer, times[0][1])

for i in range(1, n):
    if answer[0] > times[i][0]:
        heapq.heappush(answer, times[i][1])
    else :
        heapq.heappop(answer)
        heapq.heappush(answer, times[i][1])

print(len(answer))
