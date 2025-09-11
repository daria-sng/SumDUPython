N = int(input("Enter number (1;9): "))
while N < 1 or N > 9:
    N = int(input("Attention! Enter another number: "))

symbol = '*'
for i in range(1, N+1):
    for j in range(N, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(symbol, end=" ")
    print("")