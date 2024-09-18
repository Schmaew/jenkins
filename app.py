def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"Addition: {add(3, 5)}")
    print(f"Subtraction: {subtract(10, 3)}")
    print(f"Multiplication: {multiply(4, 6)}")
    print(f"Division: {divide(8, 2)}")