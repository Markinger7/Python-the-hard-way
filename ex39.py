# understand dicts


states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CL',
        'New York': 'NY',
        'Michigan': 'MI'
}

cities = {
        'CL': 'San Francisco',
        'MI': 'Detoit',
        'FL': 'Jachsonvill'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])


print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print(list(states.items()))

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')
    print(f'and has city {cities[abbrev]}')
