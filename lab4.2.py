N = 7
matrix = [[ j-i for j in range(N)] for i in range(N)]
for i in matrix:
        print(' '.join(f"{number:2}" for number in i))