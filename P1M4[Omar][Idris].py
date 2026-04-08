def str_analysis(str_Arg):
    if str_Arg.isdigit():
        num = int(str_Arg)
        if num > 99:
            return str_Arg + " Is a pretty big number "
        else:
            return str_Arg + " Is a smaller number than expected "
    else:
        if str_Arg.isalpha():
            return "" + str_Arg + " Is all alphabetical charcaters! "
        else:
            return "" + str_Arg + " has mutiple chacracter types "
        
user_input = ""

while user_input == "":
    user_input = input("Omar Idris, Enter word or integer: ")

    result = str_analysis(user_input) 
    print(result) 
