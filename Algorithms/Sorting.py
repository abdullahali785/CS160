import math

def selectionSort(arr):
    for i in range(len(arr)):
        # print(arr)
        min = arr[i]
        min_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_index = j
        
        if i != min_index:
            swap_elements(arr, i, min_index)
    return arr 

def insertionSort(arr):
    for i in range(1, len(arr)):
        element = arr[i]
        j = i 

        while j > 0 and arr[j - 1] > element:
            arr[j] = arr[j - 1]
            j = j - 1

        arr[j] = element 
    return arr

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        # print(arr)
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                swap_elements(arr, j, j+1)
    return arr 

def heapSort(arr):
    build_heap(arr)

    n = len(arr) -1
    while n > 0:
        swap_elements(arr, 0, n)
        n = n-1
        downheap(arr, 0, n)
    return arr 

def build_heap(arr):
    last = len(arr) - 1
    next = last

    while next > 0:
        downheap(arr, math.floor((next-1) / 2), last)
        next = next - 2

def downheap(arr, i, last):
    property = False
    while not property:
        max_index = index_of_max(arr, i, last)
        if max_index != i:
            swap_elements(arr, max_index, i)
            i = max_index
        else:
            property = True

def index_of_max(arr, r, last):
    largest = r
    left = r*2 + 1
    right = r*2 + 2

    if left <= last and arr[left] > arr[largest]:
        largest = left
    if right <= last and arr[right] > arr[largest]:
        largest = right
    
    return largest

def segmentSort(arr, gap):
    for i in range(gap, len(arr)): 
        insertElem = arr[i]
        j = i

        while j >= gap and arr[j - gap] > insertElem:
            arr[j] = arr[j - gap]
            j -= gap

        arr[j] = insertElem 

def shellSort1(arr):
    n = len(arr)
    gaps = [5, 3, 1]

    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i 
            while j >= gap and temp < arr[j-gap]:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp 
    return arr 

def shellSort2(arr):
    maxgap = math.floor((len(arr)-1) / 3)
    h = 1

    while h <= maxgap:
        h = h*3 + 1
    
    while h > 0:
        segmentSort(arr, h)
        h = (h-1) // 3

    return arr

def mergeSort(arr): 
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:]) 
    result.extend(right[j:])

    return result

def quickSort(arr):
    if len(arr) > 1:
        L, E, G  = partition(arr) 
        L = quickSort(L)
        G = quickSort(G)
        arr = L + E + G
    return arr 

def partition(arr):
    L, E, G = [], [], []
    p = arr[(len(arr)//2)] #middle element 
    
    for y in arr:
        if y < p:
            L.append(y)
        elif y == p:
            E.append(y)
        else:
            G.append(y)
    return L, E, G 

def inplaceQuickSort(arr, low, high): 
    if low < high:
        p = inplacePartition(arr, low, high)
        inplaceQuickSort(arr, low, p-1)
        inplaceQuickSort(arr, p+1, high)
    return arr

def inplacePartition(arr, low, high):
    p = (high + low) // 2
    swap_elements(arr, low, p)
    pivot = arr[low]
    j = low + 1
    k = high 

    while j <= k:
        while j <= k and arr[j] < pivot:
            j = j+1
        while k >= j and arr[k] >= pivot:
            k = k-1

        if j < k:
            swap_elements(arr, j, k)
            j = j+1
            k = k-1

    swap_elements(arr, low, k)
    return k 

def swap_elements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# print(inplaceQuickSort([3, 6, 2, 5, 9, 1, 0, 7, 8], 0, 8))
# print(selectionSort([64, 25, 12, 22, 11]))
# print(bubbleSort([5, 1, 4, 2, 8]))
print(shellSort1([23, 12, 1, 8, 34, 54, 2, 3]))