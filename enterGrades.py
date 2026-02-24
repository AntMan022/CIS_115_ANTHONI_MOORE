#this program will allow a user to enter up to 10 grades

numOfGrades = int(input("How many grades would you like to enter?   "))
count = 0

while count < numOfGrades : 
    count = count + 1 
    grade = input("Enter your grade:   ")

if(count >= numOfGrades):
        print(f"The user enters {numOfGrades} and is now done.")