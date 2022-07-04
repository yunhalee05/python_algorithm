c = int(input())

def max_sqare(left, right, fence):
    # 기저 사레 : 같은 값이면 가로 1 * 높이가 최대 직사각형 
    if left == right : 
        return fence[left]

    # 가운데를 중심으로 나아간다
    mid = (left + right)//2

    # 기준점 양쪽 각각 직사각형 최댓값 중에 최댓값 선택 (가운데 걸치지 않는 경우의 수)
    result = max(max_sqare(left, mid, fence), max_sqare(mid+1, right, fence))

    # 가운데를 걸치면서 넓이가 2일때의 경우의 수 
    l = mid
    r = mid + 1
    h = min(fence[l], fence[r])
    result = max(result, h * 2)

    # 가운데를 걸치는 사각형 경우의 수 (각각 양쪽끝 중에 높이가 높은 곳으로 뻗어나간다)
    while left<l or r<right :
        if r<right and (l == left or fence[l-1]<fence[r+1]):
            r += 1
            h = min(h, fence[r])
        else : 
            l -= 1
            h = min(h, fence[l])
        result = max(result, (r-l+1)*h)

    return result
 

for case in range(c) :
    n = input() 
    fence = list(map(int, input().split()))
    print(max_sqare(0, len(fence)-1, fence))


