def add(a, b):
    print(f'adding {a} + {b}')
    return a + b

def subtract(a, b):
    print(f'substracting {a} - {b}')
    return a - b

def multiply(a, b):
    print(f'multiplying {a} * {b}')
    return a * b

def divide(a, b):
    print(f'dividing {a} / {b}')
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
