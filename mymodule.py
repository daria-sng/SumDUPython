def arithmetic(start, finish):
    counter = 0
    sum = 0
    for i in range(start, finish+1, 1):
        if i % 2 == 0:
            print(i, end=" ")
            sum += i
            counter +=1
    print("Number of even numbers: ", counter)
    return sum/counter
