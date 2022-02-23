import heapq
from sys import stdin

n = int(stdin.readline())
lt = []
rt = []

for _ in range(n):
    x = int(stdin.readline())
    if len(lt) == len(rt):
        heapq.heappush(lt, (-x, x))
    else :
        heapq.heappush(rt, (x,x))

    if rt and lt[0][1]>rt[0][1]:
        left_value = heapq.heappop(lt)[1]
        right_value = heapq.heappop(rt)[1]
        heapq.heappush(lt, (-right_value, right_value))
        heapq.heappush(rt, (left_value, left_value))

    print(lt[0][1])

