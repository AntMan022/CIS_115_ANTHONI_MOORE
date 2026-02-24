#use list and for-loops to loop over the list and print it out.

def getmylist():
    list = [10,20,30,40,50,60]
    
    length = len(list)

    for item in list:
        
        print(item)

        return length
   
    total = getmylist()
    print(f"The total count is: {total}")