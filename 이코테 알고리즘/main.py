n, m , k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()


first = data[n-1]
secont = data[n-2]

result = 0


while True:
    for i in range(k):
        if m == 0:
            break
        
