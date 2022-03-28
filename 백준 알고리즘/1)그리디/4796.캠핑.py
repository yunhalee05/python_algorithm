cnt = 0
while True:
    cnt +=1
    L, P, V = map(int, input().split())
    if L+P+V ==0:
        break
    answer = 0
    answer += (V//P)*L
    if V%P >0:
        V %= P
        if L<V:
            answer += L
        else :
            answer += V
    print("Case " + str(cnt) + ": " + str(answer))
        


