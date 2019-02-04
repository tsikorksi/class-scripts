# Objective: Produce a Hash table which stores the house of students in this division. Use the trials number as a key.

# Task 1 - Complete the hash function using the folding method hash:
# http://interactivepython.org/courselib/static/pythonds/SortSearch/Hashing.html

# Task 2 - Complete the add function so that it adds the House name to the hash_table using the hash of the key.
# Invoke this function to test it out.

# Task 3 - Complete the get function to retrieve an item using the key

# Task 4 - Experiment with different hash table sizes, how does changing the size affect the number of collisions?
# Are there any with this data set?

#

# Task 5 - Add another hash function 'mid-square' method. How does this affect performance?
# What makes a good hash function?

#

# Task 6 - Attempt the 'open addressing' approach to collision resolution. Add a function to handle this.

# Extension 1 - Create a 2nd hash table that uses the CalStyle name as the key.
# You will need to create a new hash function using a combination of the folding method
# and ordinal numbers of characters. How does this perform?

# Extension 2 - Explore collision reduction using chaining or quadratic probing:
# http://interactivepython.org/courselib/static/pythonds/SortSearch/Hashing.html

size = 15
hash_table = [None] * size


def hash_function(to_hash):
    to_hash = str(to_hash)
    length = len(to_hash)
    total = 0
    if length % 2 != 0:
        flag = -1
    else:
        flag = 0

    for i in range(0, length - 2 + flag, 2):
        total += int(to_hash[i: i + 2])

    return total % size


def add(key, item):
    print("todo")


def get(key):
    print("todo")


add(9921, "ABC")
add(7932, "DEF")
print(get(7932))
print(hash_table)

