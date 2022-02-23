n = int(input())
number = map(int, input(), split())

number.sorted(number, reverse=True)

for i in range(n):
    print(i, end='')