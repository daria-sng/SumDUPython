ameba = 1
name = 'Амеба'
hour = 'Години'
print(f"{name:<15}{hour:>1}")
for i in range(12, 49, 2):
    ameba *= 3
    print(f"{ameba:<15}\t{i:>1}")