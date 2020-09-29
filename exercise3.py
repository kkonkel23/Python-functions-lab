# Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# For example:

# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0

def occurances(str1, str2):
    instances = str1.count(str2)
    return instances

print(occurances('scout', 'ou'))