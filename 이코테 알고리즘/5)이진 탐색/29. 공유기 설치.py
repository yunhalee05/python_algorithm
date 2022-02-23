
n , c= map(int, input().split())
houses = list(map(int, input().split()))
houses.sort()
end = houses[-1] - houses[0]
start = houses[1]-houses[0]

result = 0

while (start<=end):
    mid = (start+end)//2
    value = array[0]
    count = 1

    for i in range(1,n):
        if array[i]>= value+mid:
            value = array[i]
            count += 1
    if count >=c:
        start = mid+1
        result = mid
    else :
        end = mid-1


print(result)