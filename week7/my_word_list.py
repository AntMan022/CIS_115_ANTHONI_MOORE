#this code will be used to implement user defined functions

def printWordList():
    word = ["Apples", "Bananas", "Pears", "Carrots"]

    length = len(word)

    for item in word:
        
        print(item)

    return length

total = printWordList()
print(f"The total count is: {total}")