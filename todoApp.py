
import sys

# VARS
items = []

# FUNCTIONS
def view_all():
    print('')
    for i, v in enumerate(items):
        print(f'{i}. {v}')
    print('')

# COMMAND LOOP
running = True
while running:
    command = input('What would you like to do? ')

    if command == 'ee': # EXIT COMMAND
        sys.exit()
    elif command == 'view':
        view_all()

    tokens = command.split(' ') # GENERATE TOKENS

    if tokens[0] == 'add': # ADD COMMAND
        tokens.pop(0)
        item = ' '.join(tokens)
        items.append(item)
        print('oki')
    if tokens[0] == 'remove': # REMOVE COMMAND
        index = int(tokens[1])
        items.pop(index)
        print('oki')
