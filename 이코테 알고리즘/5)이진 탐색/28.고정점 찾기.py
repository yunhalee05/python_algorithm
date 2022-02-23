def find_fixed_point(array, start, end){
    if start>end : 
        return None

    mid = (start+end)//2

    if mid == array[mid] :
        return mid
    elif array[mid]<mid or array[mid]<0 :
        return find_fixed_point(array, mid+1, end)
    elif array[mid]>mid or array[mid]>n-1:
        return find_fixed_point(array, start, mid-1)

}
n = int(input())
array = list(map(int, input().split()))

print(find_fixed_point(array, 0, n-1))