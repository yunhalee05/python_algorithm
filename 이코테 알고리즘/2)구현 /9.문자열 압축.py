s = input()
result = len(s)

for k in range(1, len(s)//2+1):
    compressed = ""
    prev = s[0:k]
    cnt = 1
    for i in range(k,len(s),k):
        if s[i:i+k]== prev :
            cnt+=1
        else :
            compressed += str(cnt) + prev if cnt>=2 else prev
            prev = s[i:i+k]
            cnt = 1
    
    compressed += str(cnt) + prev if cnt>=2 else prev
    result = min(result, len(compressed))

print(result)

    