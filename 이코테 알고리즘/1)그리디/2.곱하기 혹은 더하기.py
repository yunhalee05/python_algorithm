s = input()
result = 0

for i in s:
    n = int(i)
    if result ==1 or result == 0 or n == 0 or n == 1:
        result += n
    else :
        result = (result * n)
print(result)


# 답안
# data = input()

# result = int(data[0])
# for i in range(1, len(data)):
#     #두 수중에서 하나라도 '0'혹은'1'인 경우, 곱하기보다 더하기 실행
#     num = int(data[i])
#     if num <=1 or result <=1:
#         result += num
#     else:
#         result *=num

# print(result)
