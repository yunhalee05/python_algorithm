n, m = map(int, input().split())
strs= []
for _ in range(n):
    strs.append(input())


min = 0 
answer = ''

for i in range(m):
    maximum = 0
    cha = strs[0][0]
    cntT,cntA, cntC, cntG = 0, 0, 0, 0 
    for j in strs:
        if j[i] =='T':
            cntT+=1
        elif j[i] =='A':
            cntA += 1
        elif j[i] =='C':
            cntC+=1
        elif j[i] =='G':
            cntG +=1
    maximum = max(cntT,cntA, cntC, cntG)
    if maximum == cntA:
        answer += 'A'
        min += (cntT+ cntC+ cntG)
        continue
    elif maximum == cntC:
        answer += 'C'
        min += (cntT+ cntA+ cntG)
        continue
    elif maximum == cntG:
        answer += 'G'
        min += (cntA+ cntC+ cntT)
        continue
    elif maximum == cntT:
        answer += 'T'
        min += (cntA+ cntC+ cntG)
        continue

print(answer)
print(min)

    

