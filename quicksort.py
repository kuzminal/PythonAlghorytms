data = [9,5,7,4,2,8,1,10,6,3,0]

def partition(data, left, right):
    pivot = data[left]
    lIndex = left + 1
    rIndex = right

    while True:
        while lIndex <= rIndex and data[lIndex] <= pivot:
            lIndex += 1
        while rIndex >= lIndex and data[rIndex] >= pivot:
            rIndex -= 1
        if rIndex <= lIndex:
            break
        data[lIndex], data[rIndex] = data[rIndex], data[lIndex]

    data[left], data[rIndex] = data[rIndex], data[left]
    print(data)
    return rIndex

def quickSort(data, left, right):
    if right <= left:
        return
    else:
        pivot = partition(data, left, right)
        quickSort(data, left, pivot - 1)
        quickSort(data, pivot + 1, right)
    return data
print(data)
quickSort(data, 0, len(data) - 1)