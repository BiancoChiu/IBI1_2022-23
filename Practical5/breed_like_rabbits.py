# Start with two rabbits in the first generation
# while rabbits less than 100
#   calculate numbers of next generation
#   increase the generation count
# print the result

n = 2
generation = 1
while n <= 100:
    n *= 2
    generation += 1
print('At %s generation, over 100 rabbits have been born' % generation)
# At 7 generation, over 100 rabbits have been born
