#This code sill be used to determine if a word is a palindrome.

word = "radar"
reverse_word = word [::-1]

if(word == reverse_word):
    print("This string is a palindrome..."  f'"{word}"')

if(word != reverse_word):
    print("This string is not a palindrome..."  f'"{word}"')