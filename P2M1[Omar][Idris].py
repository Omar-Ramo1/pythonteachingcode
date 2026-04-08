# [] create words after "G" following the Assignment requirements use of functions, methods and keyowrds
# Author: Omar Idris

def words_after_g(quote):
    word = ""  # placeholder to build each word
    for char in quote:
        if char.isalpha():               # if character is a letter
            word += char
        else:                            
            if word:                     
                if word[0].lower() > "g":  
                    print(word.upper())
                word = ""                # reset for next word
    # Check last word in case string ends with a letter
    if word and word[0].lower() > "g":
        print(word.upper())



full_name = input("Welcome, Omar Idris. Enter a 1 sentence quote, non-alpha separate words:\n")
words_after_g(full_name)