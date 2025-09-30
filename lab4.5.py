x = set(range(8,22))
z = x

def check(number):
    for i in range(2, number):
        if number % i == 0:
            return False 
    return True 


y = set(filter(check, x))
print("Plural x :", x)
print("Plural y :", y)
print("Plural z :", z)