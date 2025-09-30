def operations():
    words1 = list(input("Enter first list: ").split())
    words2 = list(input("Enter second list: ").split())
    
    i = 0
    while i < len(words2):
        if i % 2 == 0:
            words1.append(words2[i])
        i+=1
    print(*words1)


operations()