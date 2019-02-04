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
    """
    basic hash function using folding hash algorithm
    :param to_hash: the number whose hash is to be computed
    :return: the location of the information
    """
    to_hash = str(to_hash)
    length = len(to_hash)
    total = 0
    # if the length of the function isn't even
    if length % 2 != 0:
        flag = -1
    else:
        flag = 0

    for i in range(0, length + flag, 2):
        total += int(to_hash[i: i + 2])
    if flag == -1:
        total += int(to_hash[length])
    return total % size


def add(key, item):
    """
    adds an item to the hash table
    :param key: the key of the item
    :param item: the item to be added
    :return: nothing, as the global object is affected
    """
    hash_key = hash_function(key)
    hash_table[hash_key - 1] = item


def get(key):
    """
    gets the item/contents of the hash table at the key location
    :param key: the location of the item to be fetched
    :return: the associated item
    """
    hash_key = hash_function(key)
    return hash_table[hash_key - 1]

def mid_square():
    print("lmao")


add(9921, "ABC")
add(7932, "DEF")
add(54, "test")
print(get(7932))
print(hash_table)

