# [] create list-o-matic as a function and call it
# [] be sure to include your spelled-out name in the welcome prompt
# [] you are welcome to use any list you like for list-o-matic, does not have to be animals 

# List-o-Matic Program

def list_o_matic(string, lst):
    # If empty string, pop the last item
    if string == "":
        if len(lst) > 0:
            popped = lst.pop()
            return popped + " popped from list"
    elif string in lst:
        lst.remove(string)
        return "1 instance of " + string + " removed from list"
    else:
        lst.append(string)
        return "1 instance of " + string + " appended to list"


animals = ['cat', 'goat', 'cat']


while True:
    # Print welcome and current list
    print("Welcome, Alex Johnson. Look at all the animals", animals)
    
    # Get input from user
    user_input = input("enter the name of an animal: ")
    
    # Check if user wants to quit
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    message = list_o_matic(user_input, animals)
    print(message)
    print()
    
    # Check if list is empty
    if len(animals) == 0:
        print("Goodbye!")
        break