c = int(input())

def reverse(s, idx):
    if s[idx] == 'w' or s[idx] =='b' :
        return s[idx]
    # x로 시작한다는 의미이므로 한칸 앞으로 
    idx +=1 
    upperLeft = reverse(s, idx)
    idx += len(upperLeft)
    upperRight = reverse(s, idx)
    idx += len(upperRight)
    lowerLeft = reverse(s, idx)
    idx += len(lowerLeft)
    lowerRight = reverse(s, idx)
    return  "x" + lowerLeft + lowerRight + upperLeft + upperRight

for case in range(c) :
    s = input() 
    print(reverse(s, 0))



