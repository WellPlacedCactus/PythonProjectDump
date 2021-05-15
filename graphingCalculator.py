
# ENTER THE SLOPE AND Y-INTERCEPT OF THE EQUATION

slope = 1
yint = 0

# SETTING UP THE DISPLAY

graph = [] # 2D ARRAY
width = 11
height = 11

blank = '.' # DETERMINES WHICH CHARACTERS ARE GOING TO SHOW UP ON SCREEN
line = '@'

# SETTING UP THE 2D ARRAY

for _ in range(height):
    row = []
    for __ in range(width):
        row.append(blank)
    graph.append(row)

# APPLYING THE EQUATION

for x in range(width):
    f_of_x = slope * x + yint
    for yy in range(height):
        if yy == f_of_x:
            graph[yy][x] = line

# DISPLAYING THE GRAPH

for row in reversed(graph):
    row_string = ''
    for ele in row:
        row_string += ele
        row_string += ' '
    print(row_string)
