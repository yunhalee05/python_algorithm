n = input()

cnt1= 0
cnt2 = 0
for i in range(n):
    if i<=(len(n)//2):
        cnt1+=int(n[i])
    else :
        cnt2 += int(n[i])

if cnt1==cnt2:
    print('LUCKY')
else:
    print('READY')
