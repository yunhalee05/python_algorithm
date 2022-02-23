n = int(input())

result = 0

for i in range(1, n):
    sum = i
    temp = i
    while temp > 0:
        sum += (temp%10)
        temp //= 10 
    if sum == n:
        result = i
        break
    
print(result)
