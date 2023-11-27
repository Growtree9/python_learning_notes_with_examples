# Sets are unordered collections of unique elements.
# Meaning there can only be one representative of the same object.

# Examples:

myset = set()

print(myset)
# set()


# 1. Methods:

# .add(data) - which adds the data inside the set if it is not there

myset.add(1)

print(myset)
# {1}

myset.add(2)

print(myset)
# {1, 2}


mylist = [1,1,1,1,2,2,2,3,3,3]

print(set(mylist))
# {1, 2, 3}

