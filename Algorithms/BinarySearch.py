def recursiveBinarySearch(array, target):
    def helper(array, target, low, high):
        if low > high:
            return -1
        
        mid = (high + low) // 2
        if target == array[mid]:
            return mid
        
        elif target > array[mid]:
            return helper(array, target, mid+1, high)
        
        else:
            return helper(array, target, low, mid-1)
    
    return helper(array, target, 0, len(array)-1)
        
     
def iterativeBinarySearch(array, target):
    low = 0
    high = len(array) -1

    while low <= high:
        mid = (high - low) // 2

        if target == array[mid]:
            return mid
        
        elif target < array[mid]:
            high = mid -1

        else:
            low = mid + 1

    return -1 
