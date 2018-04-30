from box import *

while True:

    rows = int(input('How many rows tall (2 or more)? '))
    cols = int(input('How many columns wide (2 or more)? '))

    if rows < 2 or cols < 2:
        print('Invalid input. Must be 2 or more.')
        continue
    else:
        print_first_last_line(cols)
        if rows > 2:
            print_middle_lines(rows, cols)
        print_first_last_line(cols)
        break