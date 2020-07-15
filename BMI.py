# Calculate BMI
print('Welcome to BMI calculator')
print('please input your data!')


height = float(input('How tall are you? (in m) '))
weight = float(input('How much do you weigh? (in kg) '))

BMI = weight / (height * height)

print(f'You have a BMI of {round(BMI)}')

if BMI <= 18.5:
    print(f'With a BMI of {round(BMI)} you are Underweight')
elif BMI <= 24.9:
    print(f'With a BMI of {round(BMI)} you are Normal to healthy weight')
elif BMI <= 29.9:
    print(f'With a BMI of {round(BMI)} you are Overweight')
else:
    print(f'With a BMI of {round(BMI)} you are Obese')
