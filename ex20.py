from sys import argv

script, input_file = argv = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end='') # end='' avaid double spaces between text

current_file = open(input_file)

print('First lets print the whole file :\n')

print_all(current_file)

print('Now lets rewind, kind like a tape.')

rewind(current_file)

print('lets print three lines:')

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
