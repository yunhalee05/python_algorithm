# *********
n, k = map(int, input().split())
electronic = list(map(int, input().split()))
answer = 0
uses = []

while electronic:
    electro = electronic[0]
    if electro in uses:
        del electronic[0]
        continue
    if len(uses)<n:
        uses.append(electro)
        del electronic[0]
        continue 
    change = 0
    maxIndex = 0
    for i in uses:
        if i not in electronic:
            change = i
            break
        if electronic.index(i) > maxIndex:
            maxIndex = electronic.index(i)
            change = i
    uses[uses.index(change)] = electro
    del electronic[0]
    answer+=1

print(answer)


