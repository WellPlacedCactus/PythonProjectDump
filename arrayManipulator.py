
import sys

# VARS
arrays = []

# FUNCTIONS

# COMMAND LOOP
running = True
while running:
    command = input('am:')
    tokens = command.split(' ')

    if command == 'exit':
        sys.exit()

    if tokens[0] == 'new': # CREATE NEW ARRAY COMMAND
        tokens.pop(0)
        arrays.append([int(x) for x in tokens])
    elif tokens[0] == 'view': # VIEW AN ARRAY COMMAND
        if tokens[1] == 'all':
            for array in arrays:
                print(array)
        else:
            index = int(tokens[1])
            print(arrays[index])
        
