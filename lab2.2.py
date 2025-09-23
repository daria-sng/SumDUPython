import mymodule

value = True 
while value:
    try:
        x = int(input("Start with (x), integer! = "))
        y = int(input("Finish (y), integer! = "))
        value = False
    except ValueError: 
        print("Integers!")

print(f"The arithmetic mean of even numbers from {x} to {y}: {mymodule.arithmetic(x, y):.2f}")
