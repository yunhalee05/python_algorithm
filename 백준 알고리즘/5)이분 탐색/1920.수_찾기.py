n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
findNumbers = list(map(int, input().split()))

numbers.sort()

def binarySearch(left, right, x, numbers):
    if left > right :
        return 0
    mid = (left + right)//2
    if numbers[mid] == x :
        return 1
    if x < numbers[mid] :
        right = mid-1
    elif x > numbers[mid]:
        left = mid+1
    return binarySearch(left, right, x, numbers)

for i in findNumbers:
    left = 0
    right = len(numbers)-1
    print(binarySearch(left, right, i, numbers))


# n = int(input())
# numbers = list(map(int, input().split()))
# m = int(input())
# findNumbers = list(map(int, input().split()))

# for i in findNumbers:
#     if i in numbers:
#         print(1)
#     else :
#         print(0)