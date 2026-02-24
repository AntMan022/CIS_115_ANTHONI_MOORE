#This code will be used to find the paththeorem

y = float(input("Enter Y: "))
x = float(input("Enter X: "))


def hypoteneuse(y,x):

    c=(((y**2)+(x**2))**(1/2))

    print((f"hypotenuse: {c}"))

    hypoteneuse(y,x)