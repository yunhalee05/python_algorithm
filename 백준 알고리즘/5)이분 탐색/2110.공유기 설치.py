n, c = map(int,input().split())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

#갭의 최솟값과 최댓값을 기준으로 줄여나간다. (공유기를 m개 이상 설치 할 수 있는 최대의 갭을 찾아나간다.)
start = 1
end = array[-1] - array[0]

result=0

while (start <= end) :
    mid = (start+end)//2
    count = 1 #최소 하나는 설치하고 시작
    start_house = array[0] # 첫집을 기준으로 와이파이 갯수 카운팅

    for i in range(1, n):
        if array[i] >= (start_house+mid) :#갭을 더한 값보다 크거나 같으면 와이파이설치 가능
            count +=1
            start_house = array[i] #다음 설치 집과의 거리측정을 위해서 기준 재조정
    
    if count >= c: #설치를 했다면, 가능한 갭이니까 일단 결과값에 저장해놓고 범위 폭을 줄여나가면서 그 안의 최솟값(인접한 거리) 측정한다. 
        start = mid +1
        result = mid
    else : #만약 거리가 너무 넓어서 공유기 설치를 모두 못했다면, 범위 재조정(더 작게)
        end= mid -1


print(result)
