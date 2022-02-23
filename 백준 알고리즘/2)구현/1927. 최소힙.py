import heapq
from sys import stdin

heap= []
n = int(stdin.readline())

for _ in range(n):
    x = int(stdin.readline())
    if x!= 0:
        heapq.heappush(heap, x)
    else :
        if heap :
            print(heapq.heappop(heap))
        else:
            print("0")


