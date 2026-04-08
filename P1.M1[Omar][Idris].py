# Create name check code
input_test = input('Enter list of people met in the last 24hrs:')

# [ ] get input for input_test variable
print('Names Entered:', input_test)
input_test = input_test.lower()

# [ ] print "True" message if "John" is in the input or False message if not
print('Is John in the list?', "john" in input_test)

# [ ] print True message if your name is in'MARY' in input_test)
print('Is MARY in the list?', 'mary' in input_test)
# [ ] Challenge: Check if a fourth person's name is in the input - print message
print('Is Omar in the list?', 'omar' in input_test)
print('Is Alex in the list?', 'alex' in input_test)


