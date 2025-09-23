import math 
def expression(number):
    return math.sqrt(number)+10

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


m = float(input("Enter number for expression (number >=0!): "))
while m < 0:
    m = float(input("Number >=0! , try again: "))

print(f"z = √m + 10 = {expression(m):.4f}")

print("\nEnter range for the arithmetic mean of all even numbers: ")

value = True 
while value:
    try:
        x = int(input("Start with (x), integer! = "))
        y = int(input("Finish (y), integer! = "))
        value = False
    except ValueError: 
        print("Integers!")

print(f"The arithmetic mean of even numbers from {x} to {y}: {arithmetic(x, y):.2f}")