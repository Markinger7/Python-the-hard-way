# we import zhe model sys with the sys class
from sys import argv

# definde the imput from the terminal
script, filename = argv

# use open() to access the file
txt = open(filename)

# simple print statement
print(f'Here\'s your file {filename}:')
# use the read() function to access the infromation in the file
print(txt.read())

txt.close()



'''
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
'''
