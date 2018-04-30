star = '* '
space = '  '

def print_first_last_line(width):
    col_counter = 0

    while col_counter < width:
        print (star, end='')
        col_counter += 1
    print()

def print_middle_lines(height, width):
 
    row_counter = 2
    col_counter = 2

    while row_counter < height:
        print(star, end='')

        if width == 2:
            print(star)
            row_counter += 1
            col_counter = 0
            continue

        while col_counter < width:
            print(space, end='')
            col_counter += 1
        print(star)
        col_counter = 2
        row_counter += 1


