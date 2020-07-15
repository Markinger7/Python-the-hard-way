from sys import argv

script, filename = argv

file = open(filename, 'r')

print(file.readline())

file.close()
