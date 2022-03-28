from bisect import bisect_left, bisect_right


n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
findNumbers = list(map(int, input().split()))
answer = []

numbers.sort()

for i in findNumbers:
    left = bisect_left(numbers, i)
    right = bisect_right(numbers, i)
    print(right-left, end=' ')
    