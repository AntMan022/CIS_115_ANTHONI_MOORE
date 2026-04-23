#This code will find the max value by accepting ttwo integer values and finding the greater value.

x = int(input("Give value: "))
y = int(input("Give value: "))

def max(x,y):
    if(x<y):
        print(f"The greater number is: {y}")
    elif x > y: 
        print(f"The greater number is: {x}")
    else: 
        print("inputs are equal")

max(x,y)
