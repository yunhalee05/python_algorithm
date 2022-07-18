n = int(input())
numbers = list(map(int, input().split()))
reversed_numbers = numbers[::-1]
dp1 = [1]*n
dp2 = [1]*n

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
        if reversed_numbers[i] > reversed_numbers[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

result = [(dp1[i]+dp2[n-1-i]-1) for i in range(n)]
    
print(max(result))
