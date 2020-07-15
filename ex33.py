numbers = []

def while_func(range, list):
    i = 0

    while i < range:
        list.append(i)
        i += 1

        print('Numbers now: ', list)
        print(f'At the bottom i is {i}')

while_func(6, numbers)



'''
while  i < 6:
    print(f'At the top i is {i}')
    numbers.append(i)

    i += 1

    print('Numbers now: ', numbers)
    print(f'At the bottom i is {i}')

print('The numbers: ')
for num in numbers:
    print(num)
'''
