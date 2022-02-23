n = int(input())
s_score = []

for _ in range(n):
    s_score.append(input().split())

s_score.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in s_score:
    print(student[0])
