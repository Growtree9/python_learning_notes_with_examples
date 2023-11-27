# Strings are sequence of characters, using the syntax of either single quotes or double quotes:
# Example: "hello", 'hello', "I don't know that!"


print('hello world')
# hello world

print('hello \tworld') # gives more space between words
# hello     world

print('hello \nworld') # it takes new line to the word
# hello
# world

print(len('hello')) # prints length of the string
# 5


# Because strings are ordered sequences it means we can using indexing and slicing to grab sub-sections of the string.



# 1. Indexing:

# Indexing notation uses [] notation after the string (or variable assigned the string).
# Indexing allows you to grab a single character from the string.
# These actions use [] square brackets and a numbers index to indicate positions of what you wish to grab.
    # characters    : h  e  l  l  o
    # index         : 0  1  2  3  4
    # reverse index : 0 -4 -3 -2 -1

mystring = 'hello world'
# indexing: 012345678910
print(mystring[3])
# l
print(mystring[-3])
# r


# 2. Slicing:

# Slicing allows you to grab a subsection of multiple characters, a "slice" of the string.
# This has the following syntax:
   # [start:stop:step]  -> default => [0:len(str):1]
# start is a numerical index for the slice part.
# stop is the index you will go up to (but not include)
# step is the size of the "jump" you take.


print(mystring[::]) # prints whole string
# hello world
print(mystring[2:]) # from two onwards
# llo world
print(mystring[:3]) # upto 3 but not including 3rd letter
# hel
print(mystring[2:7]) # starts from 2, upto 7 but not 7th letter
# hello w
print(mystring[::2]) # gap of 2
# hlowrd
print(mystring[3:9:3]) # starts from 3, end to 9, with 3 steps
# lwl
print(mystring[::-1]) # reverse the whole string
# dlrow olleh



# 3. Immutability:

name = 'Sam'

# name[0] = 'P'

# The line `name[0] = 'P'` is trying to change the first character of the string `name` to 'P'.
# However, strings in Python are immutable, which means that once a string is created, its characters cannot be changed. Therefore, trying to assign a new value to a specific index of a string will result in an error.



# the solution for the above problem is below

# 4. Concatenation:

# We add two string together using + sign operator.

new_name = 'P' + name[1:]
print(new_name)
# Pam



# 5. String Methods:

# .lower() - it lowers each and every letter of the string
# .upper() - it capitalize each and every letter of the string
# .capitalize() - it capitalize only first letter of teh string
# .split() - it splits the words and put into the list
# there are lots of methods are available, you can just give the string name and after write '.', then all the methods are visible.

str_meth = 'welcome to python programming!'

print(new_name.lower())
# welcome to python programming!
print(new_name.upper())
# WELCOME TO PYTHON PROGRAMMING!
print(new_name.capitalize())
# Welcome to python programming!
print(new_name.split())
# ['welcome', 'to', 'python', 'programming!']



# 6. Print Formatting with String:

# Often you will want to "inject" a variable into your string for printing.
# for example:

my_name = "Jose"
print("Hello " + my_name)

# There are multiple ways to format strings for printing variable in them.
# This is known as string interpolation.
# There are two methods for this:
# .format() method
# f-strings (formatted string literals)

print('Hello {}! Welcome to Python3.'.format(my_name))
# Hello Jose! Welcome to Python3.

print('The {} {} {}.'.format('fox','brown','quick'))
# The fox brown quick.

print('The {b} {q} {f}.'.format(f='fox', b='brown', q='quick'))
# The brown quick fox.


# other way

print(f'Hello, my name is {my_name}.')
# Hello, my name is Jose.

age = 30

print(f'{my_name} is {age} years old!')
# Jose is 30 years old!

