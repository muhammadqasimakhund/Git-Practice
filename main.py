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

# Write a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))