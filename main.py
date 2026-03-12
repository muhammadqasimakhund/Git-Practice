print(1+2)
print(3+4)

# Write function to add two numbers
def add(a, b):
    return a + b
print(add(1, 2))
print(add(3, 4))

# Write a function to create a febonacci sequencedef fibonacci(n):
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(10))