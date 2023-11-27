# Lists are ordered sequences that can hold a variety of object types.
# They use [] brackets  and commas to separate objects in the list.
# Ex. [1, 2, 3, 4, 5]
# Lists support indexing and slicing.
# Lists can be nested and also have a variety of useful methods that can be called off of them.


my_list = [1, 2, 3, 4, 5]

my_list = ['Strings', 100.23, 203, 20.302, 39, 78, 'Lists']

print(my_list)
# ['Strings', 100.23, 203]

print(len(my_list)) # it prints the numbers of items in the list
# 3



# 1. Indexing:

print(my_list[3]) # because of indexing count starts from 0, it prints 4th numbers of items
# 20.302



# 2. Concatenation:

mylist1 = ['one', 'two', 'three']
mylist2 = ['four', 'five']

mylist3 = mylist1 + mylist2
print(mylist3)

# ['one', 'two', 'three', 'four', 'five']



# 3. Mutability:

mylist3[0] = 'zero'
print(mylist3) # it replace the 'one' by 'zero'
# ['zero', 'two', 'three', 'four', 'five']




# 4. Methods:

# .append(data) - it adds the 'data' at the last place in the list
# .pop() - removes the last value from the list
# .sort() - it sorts the list in ascending order
# .reverse() - it reverse the whole list

mylist3.append('six')
print(mylist3)
# ['zero', 'two', 'three', 'four', 'five', 'six']

mylist3.pop()
print(mylist3)
# 'six'

mylist3.pop(0) # it can also takes the index and remove that index value from the list
print(mylist3)
# 'zero'


letters = ['i', 'o', 'a', 'u', 'e']
letters.sort()
print(letters)
# ['a', 'e', 'i', 'o', 'u']

letters.reverse()
print(letters)
# ['u', 'o', 'i', 'e', 'a']



