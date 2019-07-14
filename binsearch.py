def search(searchList, key):
    mid = int(len(searchList) / 2)
    print("Средняя точка - ", str(searchList[mid]))

    if mid == 0:
        print("Ключ не найден!")
        return key
    
    elif key == searchList[mid]:
        print("Ключ найден!")
        return searchList[mid]

    elif key > searchList[mid]:
        print("Сейчас searchList содержит ",
        searchList[mid:len(searchList)])
        search(searchList[mid:len(searchList)], key)
    
    else:
        print("Сейчас searchList содержит ",
        searchList[0:mid])
        search(searchList[0:mid], key)

aList = list(range(1,21))
search(aList, 5)