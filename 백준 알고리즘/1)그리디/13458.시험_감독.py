n = int(input())
students  = list(map(int, input().split()))
director, subdirector = map(int, input().split())

def get_count(student):
    student -= director
    if student>0:
        cnt = (student//subdirector)+1
        if student%subdirector != 0:
            cnt +=1
    else :
        cnt = 1
    return cnt

answer = 0
for i in students:
    answer += get_count(i)

print(answer)


