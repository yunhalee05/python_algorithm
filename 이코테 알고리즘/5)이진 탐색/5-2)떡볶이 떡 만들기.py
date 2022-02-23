result = 0
def binary_search (arr, target, lt, rt){
    while(lt<=rt){
        mid = (lt+rt)//2
        total = 0
        for i in arr:
            if arr[i]> mid :
                total += (arr[i]-mid)
        if total <target :
            rt = mid-1
        else :
            lt = mid +1
            result = mid
    }
    return result
}

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

print(binary_search(array, m, 0, array[array.length-1]))
