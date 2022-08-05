import math
def solution(a):
    answer = [False]*len(a)
    left, right = math.inf, math.inf
    # 여기서 중요한것은 알고자하는 지점 기준으로 왼쪽과 오른쪽 중에 한부분이라도 기준이 가장 작은 인자가 되는 부분이 있다면 최후까지 남는 것이 가능하다는 것 
    # 자기보다 작은 인자를 한번 없앨 수 있기 때문에 기준보다 작은 인자가 양쪽에 한군데에만 있다면 최후까지 살아남겨두고 마지막에 작은 점수를 없애면 되기 때문 
    # 탐색은 양방향에서 각각의 끝단으로 이동하며 계속해서 자신이 제일 작은 인자인지 확인한다. 
    # left와 right는 각각 각각의 왼쪽부분 오른쪽부분 에서 가장 작은 값을 나타내기 때문에 비교가 가능하다. 
    for i in range(len(a)):
        if a[i]<left:
            left = a[i]
            answer[i] = True 
        if a[len(a) - i-1]<right : 
            right = a[len(a) - i-1]
            answer[len(a) - i-1] = True
            
    return sum(answer)