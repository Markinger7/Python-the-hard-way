ten_things = 'There are not 10 things in this list'

print(ten_things)

more_stuff = ['Day', 'Night', 'Good day fine sir', 'Dodge', 'Party']

stuff = ten_things.split(' ')




while len(stuff) != 10:
    next_item = more_stuff.pop()
    print('Adding: ', next_item)
    stuff.append(next_item)
    print(f'ther are now {len(stuff)} items in the list')


print(f'here is the final list: {stuff}')

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('-'.join(stuff[3:5]))
