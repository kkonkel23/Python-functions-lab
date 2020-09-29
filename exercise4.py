# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

# For example:

# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0

def product(*args):
    sum = 1
    for a in args:
        sum *= a

    return sum

print(product(7,7,7))
