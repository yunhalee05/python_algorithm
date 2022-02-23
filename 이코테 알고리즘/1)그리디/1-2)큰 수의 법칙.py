n, m ,k = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0

numbers.sort()
t = k
while m>0 :
    if t>0 :
        result += numbers[n-1]
        t -=1
    else :
        result += numbers[n-2]
        t = k
    m -=1

print(result)


