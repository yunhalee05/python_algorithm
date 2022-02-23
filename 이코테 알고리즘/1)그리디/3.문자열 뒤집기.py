numbers = input()

zero = 0
one = 0
temp = numbers[0]
if temp == '0':
    zero += 1
else :
    one += 1

for i in numbers:
    if temp != i:
        if i == '0':
            zero += 1
            temp = i
        else :
            one += 1
            temp = i

result = min(zero, one)
print(result)




















