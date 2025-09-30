N = int(input("Enter the number of elements in the array: "))
print(f"Enter {N} negative elements: ")

value = True
while value:
    try:
        array = [float(input()) for i in range(N)]
        value = False
    except ValueError:
        print("Enter only numbers!")

print("Your array: ", array)

negative = [element for element in array if element < 0]
if negative:
    print("Maximum negative element:", max(negative))
else:
    print("All numbers are positive! Try again")