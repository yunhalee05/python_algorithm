k, n = map(int, input().split())
lines = []
for i in range(k):
    lines.append(int(input()))

def bisect(left, right):
    if left > right:
        return right
    mid = (left+right)//2
    cnt = sum([x//mid for x in lines])
    if cnt >= n :
        return bisect(mid+1, right)
    else :
        return bisect(left, mid-1)

print(bisect(1, max(lines)))

# 최소길이를 1로 해주어야 zeroDevisionError를 피할 수 있다. 