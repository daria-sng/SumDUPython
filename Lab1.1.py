a = int(input("Enter number a (1;100): "))
b = int(input("Enter number b (1;100): "))
while a < 1 or a > 100:
    a = int(input("Attention! Enter another number a: "))
while b < 1 or b > 100:
    b = int(input("Attention! Enter another number b: "))

if a < b:
    X = b/a-1
elif a == b:
    X = -295
else:
    X = (a-235)/b

print(f"Result: {X:.2f}")