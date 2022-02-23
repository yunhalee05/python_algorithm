s = input()

numbers = s.split('-')
result = 0

for i in range(0, len(numbers)):
    temp = 0
    for j in numbers[i].split('+'):
        temp += int(j)
    if i == 0:
        result = temp
    else :
        result -= temp

print(result)