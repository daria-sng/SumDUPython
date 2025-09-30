def operations():
    list = [2.1, 34, -12 , True, 2.1, 3, -12, False, True, 0.1, 0.1]
    list2 = []
    i = 0
    while i < len(list):
        if list.count(list[i]) != 1:
            if list[i] not in list2:
                list2.append(list[i])
        i+=1
    print("List without repetitions:", list2)


operations()