from itertools import combinations

l, c = map(int, input().split())
str = list(input().split())
answer= []
vowels = []
constants = []

for i in str:
    if i =='a' or i =='e' or i=='i' or i=='o' or i=='u':
        vowels.append(i)
    else :
        constants.append(i)

for i in range(2, l):
    for a in list(combinations(constants, i)):
        for b in list(combinations(vowels, l-i)):
            stri = (''.join(a))+(''.join(b))
            answer.append(sorted(stri))

answer.sort()
for i in answer:
    print(''.join(i))


    



        




