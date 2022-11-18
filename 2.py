import random


def random_numbers(limit=100, start=1, end=10):
    num = 0
    while num != limit:
        yield random.randint(start, end)
        num += 1


print(f"random_numbers is a {type(random_numbers()).__name__}")  # It's a generator
for number in random_numbers(limit=4, start=6, end=64):  # Iteration through it is also possible
    print(number)
