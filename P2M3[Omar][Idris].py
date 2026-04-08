# [] create poem mixer function, call the function with the provided test string
# [] test string: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  

def word_mixer(word_list):
    word_list.sort()
    
    new_list = []
    
    while len(word_list) > 5:
        word_list.pop(4)          
        new_list.append(word_list.pop(0))   
        new_list.append(word_list.pop(-1))  
    
    return new_list


poem = input("Welcome, Omar Idris Enter a saying or a poem: ")


word_list = poem.split()

poem_length = len(word_list)

for i in range(poem_length):
    if len(word_list[i]) <= 3:
        word_list[i] = word_list[i].lower()   
    elif len(word_list[i]) >= 7:
        word_list[i] = word_list[i].upper()   


mixed = word_mixer(word_list)
print(" ".join(mixed))