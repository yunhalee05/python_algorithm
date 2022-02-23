# s = input()

# stringarray = []
# intarray = 0
# result =''

# for i in s:
#     if int(i) <=9 and 0<int(i):
#         intarray+=int(i)
#     else: stringarray+=i

# stringarray.sort()

# for i in stringarray:
#     result+=(str(i))

# print(result)


s = input()
result = []
value = 0
for i in s:
    if i.isalpha():
        result.append(i)
    else :
        value+= int(i)

result.sort()
if value != 0:
    result.append(str(value))


# 리스트를 문자열로 변환하여 출력
print(''.join(result))