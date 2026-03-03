

m = int(input("what's the mass in kilograms?: "))
v = int(input("What's the velocity in  meters per set?: "))

def kinetic_energy(m,v):
    
    k = 1/2*(m*v**2)

    print(k)

kinetic_energy(m,v)