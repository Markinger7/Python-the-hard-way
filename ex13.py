from sys import argv

script, income = argv

income = int(income)

x = int(input('months: '))

income_per_month = income / x

print(f'Your Income per month is {income_per_month}')
