##문제 잘 읽기! 회의실의 갯수 X 한 강의실에서 이루어지는 최대 회의의 갯수! 

n = int(input())
classes = []
for _ in range(n):
    x, y = map(int, input().split())
    classes.append((x,y))

classes.sort(key=lambda x: (x[1], x[0]))

answer = 1
end = classes[0][1]

for i in range(1, n):
    if classes[i][0]>= end:
        answer+=1
        end = classes[i][1]

print(answer)

# n = int(input())
# times = []
# for i in range(n):
#     a, b = map(int, input().split())
#     times.append((a, b))

# times.sort(key=lambda x:(x[1], x[0]))
# print(times)

# count = 1
# start = times[0]
# for i in range(1, n):
#     if times[i][0] >= start[1]:
#         count += 1
#         start = times[i]

# print(count)
