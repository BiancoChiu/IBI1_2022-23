# What does this piece of code do?
# Answer:  get random integers and compare with the stored one, then keep the bigger one

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress = 0
stored_random_number = 0
# Run the loop for ten times.
while progress < 10:
    progress += 1
    n = randint(1, 100)
    # Each time get a random integer and compare it with the stored random number
    if n > stored_random_number:
        # Keep the greater one
        stored_random_number = n

print(stored_random_number)
