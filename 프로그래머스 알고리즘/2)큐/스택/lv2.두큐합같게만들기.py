from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    cnt = sum1 + sum2
    
    if cnt % 2 != 0 :
        return -1
        
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    
    for _ in range((len(queue1)+len(queue2)) + 2):
        if sum1 == sum2 : 
            return answer
        elif sum1 < sum2 : 
            tmp = queue2.popleft()
            sum1 += tmp
            sum2 -= tmp
            queue1.append(tmp)
        elif sum2 < sum1 : 
            tmp = queue1.popleft()
            sum2 += tmp
            sum1 -= tmp
            queue2.append(tmp)
        answer += 1

    return -1