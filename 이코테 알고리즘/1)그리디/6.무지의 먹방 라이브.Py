data = list(map(int,  input().split()))
k = int(input())
time = 0
i = 0
while time<k:
    if i > len(data):
        i -= len(data)
    if data[i] >0:
        data[i] -=1
        time +=1
    i +=1

print(i+1)



# food_times = list(map(int, input().split()))
# k = int(input())
# cnt = 0
# now = 0

# while(True):
#     if food_times[now] !== 0:
#         food_times[now] -=1
#         cnt+=1
#     now +=1
#     if len(food_times)-1<now:
#         now = 0
    
#     if cnt==k:
#         break

# for i in range(now, len(food_times)):
#     if food_times[i]!== 0:
#         print(i+1)
#         break


# import heapq
# def solution(food_times, k):
#     #전체음식을 먹는 시간보다 k가 크거나 같다면 -1
#     if sum(food_times)<=k:
#         return -1
#     #시간이 작은 음식부터 빼야하므로 우선순위 큐 이용
#     q=[]
#     for i in range(len(food_times)):
#         #(음식시간, 음식번호)순대로 우선순위 큐에 삽입
#         heapq.heappush(q, (food_times[i], i+1))

#     sum_value = 0 #먹기위해 사용한 시간
#     previous = 0 #직전에 다 먹은 음식 시간
#     length = len(food_times) #남은 음식의 갯수

#     #sum_value + (현재음식시간-이전음식시간)*현재음식갯수와 k 비교
#     while sum_value+ ((q[0][0]-previous)*length)<=k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now-previous)*length
#         length-=1#다먹은 음식 제외
#         previous = now #이전음식의 시간 재설정

#     #남은 음식중에서 몇 번째 음식인지 확인하여 출력
#     result = sorted(q, key =lambda x:x[1])#음식의 번호 기준 정렬
#     return result([k-sum_value]%length[1])