import random

def generate_random_number(n):
    if n <= 0:
        raise ValueError("The number of digits must be greater than 0")
    
    # Generate the first digit ensuring it's not zero
    first_digit = random.randint(1, 9)
    
    # Generate the remaining n-1 digits
    remaining_digits = [random.randint(0, 9) for _ in range(n - 1)]
    
    # Combine the first digit with the remaining digits
    random_number = str(first_digit) + ''.join(map(str, remaining_digits))
    
    return random_number

# Example usage
n = 10
random_number = generate_random_number(n)
print(random_number)
