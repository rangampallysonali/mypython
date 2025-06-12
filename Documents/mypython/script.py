import random

# Generate a random float between 0 and 1
random_float = random.random()
print(f"Random float: {random_float}")

# Generate a random integer within a specified range
random_int = random.randint(1, 10)  # Inclusive range
print(f"Random integer: {random_int}")

# Generate a random integer within a specified range, exclusive of the upper bound
random_int_exclusive = random.randrange(1, 10)  # 1 to 9
print(f"Random integer (exclusive): {random_int_exclusive}")

# Generate a random number from a list
my_list = [1, 2, 3, 4, 5]
random_choice = random.choice(my_list)
print(f"Random choice from list: {random_choice}")

# Generate a list of random numbers
random_numbers = random.sample(range(1, 100), 5)  # 5 unique random numbers between 1 and 100
print(f"List of random numbers: {random_numbers}")

# Set the seed for reproducibility
random.seed(42)
random_float_seeded = random.random()
print(f"Seeded random float: {random_float_seeded}")
