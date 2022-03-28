n, m = map(int, input().split())
trees = list(map(int, input().split()))

right = max(trees)
left = 1

while left<=right :
    mid = (left + right)//2
    cnt = sum([x> mid and x-mid for x in trees])
    if cnt >= m :
        left = mid +1
    else : 
        right = mid -1

print(right)
