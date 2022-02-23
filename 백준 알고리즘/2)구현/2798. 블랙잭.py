n, m = map(int, input().split())
a = list(map(int, input().split()))
sum = 0

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if a[i] + a[j] + a[k] > m:
                continue
            else:
                sum = max(sum, a[i] + a[j] + a[k])

print(sum)