


















# n, m = int(input().split())

# weight = list(map(int, input().split()))
# count =0

# for i in len(1, weight):
#     for j in (2, weight):
#         if weight[i] != weight[j]:
#             count +=1


# print(count)




# n, m = map(int, input().split)

# weight = list(map(int, input().split()))

# cnt = 0

# for i in range(weight):
#     for j in range(i, weight):
#         if weight[i] == weight[j]:
#             cnt +=1


# print((n*(n-1)/2 - cnt)


# 답안
# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# #1부터 10까지 무게를 담을 수 있는 리스트
# array = [0]*11

# for x in data:
#     #각 무게에 해당하는 볼링공의 개수 카운트
#     array[x] +=1

# result = 0
# #1부터 m까지의 각 무게에 대하여 처리
# for i in range(1,m+1):
#     n-=array[i] #무게가 i인 볼링공의 갯수(A가 선택하는 개수)제외
#     result += array[i]*n #B가 선택하는 경우의 수와 곱하기

# print(result)