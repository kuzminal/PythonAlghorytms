data = [9,5,7,4,2,8,1,10,6,3,0]

def mergesort(list):
    # Првоеряем разбит ли список на отедльные части
    if len(list) < 2:
        return list
    
    #находим середину
    middle = len(list)//2

    # разбиваем список на две части
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    #Объединяем отсортированные части в одну
    print("Левая часть: ", left)
    print("Правая часть: ", right)
    merged = merge(left, right)
    print("Оъединены в ", merged)
    return merged

def merge(left, right):
    if not len(left):
        return left
    if not len(right):
        return right
    
    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    #объединяем все элементы
    while (len(result) < totalLen):

        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

        if leftIndex == len(left) or rightIndex == len(right):
            result.extend(left[leftIndex:] or right[rightIndex:])
            break
    return result

mergesort(data)