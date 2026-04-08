# [ ] create, call and test the adding_report() function

def adding_reports(report="T"):
    total = 0
    item = ""
    print('Input an integer to add to the total or "Q" to quit')
    while True:
        user_input = input('Enter an integer or Q to quit')
        if user_input.isdigit():
            num = int(user_input)
            total = total + num 
            if report == 'A':
                item = item + user_input + '\n'
        elif user_input.upper().startswith('Q'):
            if report == 'A':
                print('\nItems')
                print(item)
            print('\nTotal')
            print(" ", total) 
            print("Calculated by: Omar Idris")
            break 
        else:
            print(user_input, 'is an invalid input')

adding_reports("A")
adding_reports("T") 