# Tuples are very similar to lists. However they have one key difference - immutability.
# Once an element is inside a tuple, it can not be reassigned.
# Tuples use parenthesis: (1,2,3)


t = (1, 2, 3)

print(len(t))
# 3



# 1. Indexing:

my_tuple = ('one', 2, 3)

print(my_tuple[0])
# one

print(my_tuple[-1])
# 3



# 2. Methods:

# .count(value) - it counts how many time the value comes in the tuple

tup_meth = ('a', 'a', 'a', 'b', 'c')

print(tup_meth.count('a'))
# 3

print(tup_meth.index('b'))
# 3



# 3. Immutability:

# tup_meth[0] = 'e'
# it gives an error, because tuples are immutable.

