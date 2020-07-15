my_name = 'Zed A. Shaw'
my_age=35#notalie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

inch_cm = 2.54
lbs_kg = 2.205

hight_cm = my_height * inch_cm
weight_kg = my_weight / lbs_kg

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f'He is {hight_cm} centimeters tall.')
print(f"He's {my_weight} pounds heavy.")
print(f'he sis {weight_kg} kilfo heavy')
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
