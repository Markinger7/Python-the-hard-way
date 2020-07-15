from sys import argv

script, filename = argv

print('creatinf file...')
file = open(filename, 'w')

line = input('> ')

file.write(line)

file.close()
