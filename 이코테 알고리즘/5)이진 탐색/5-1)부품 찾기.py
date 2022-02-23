def binary_search(arr, target, lt, rt){
    while(lt<=rt){
        mid = (lt+rt)//2
        if arr[mid]==target :
            return mid
        elif arr[mid]<target:
            lt = mid+1
        else {
            rt = mid-1
        }
    }
    return None
}
n = int(input())
array = list(map(int,input().split()))
array.sort()

m = int(input())
looking = list(map(int, input().split()))

for( j in looking){
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else print('no', end=' ')
}

