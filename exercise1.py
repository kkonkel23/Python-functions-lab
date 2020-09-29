# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# For example:

# sum_to(6)  # returns 21
# sum_to(10) # returns 55


def sum_to(n):
    sum = 0
    for n in range(1, n + 1):
        sum += n
    
    return sum


print(sum_to(6))

        