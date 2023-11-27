# 1. Answer these 3 questions without typing code. Then type code to check your answer.

# What is the value of the expression 4 * (6 + 5)
print(4 * (6 + 5))
# Ans. 44

# What is the value of the expression 4 * 6 + 5 
print(4 * 6 + 5)
# Ans. 29

# What is the value of the expression 4 + 6 * 5
print(4 + 6 * 5)
# Ans. 34



# 2. What is the type of the result of the expression 3 + 1.5 + 4?
print(type(3 + 1.5 + 4))
# Ans. float



# 3. What would you use to find a number’s square root, as well as its square?
num = 16

# square root
print(num**0.5)
# 4

# square
print(num**2)
# 256



s = 'hello'
# 4. Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

print(s[1])
# e



# 5. Reverse the string 'hello' using slicing:
print(s[::-1])



# 6. Given the string hello, give two methods of producing the letter 'o' using indexing.

print(s[4])
# o

print(s[-1])
# o



# 7. Build this list [0,0,0] two separate ways.

print([0, 0, 0])
# [0, 0, 0]

print([0]*3)
# [0, 0, 0]



# 8. Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'
print(list3)
# [1,2,[3,4,'goodbye']]



# 9. Sort the list below:

list4 = [5,3,4,6,1]

list4.sort()
print(list4)
# [1, 3, 4, 5, 6]



# 10. Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
print(d['simple_key'])
# hello


d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
# hello


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
# hello


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])
# hello



# 11. Can you sort the dictionary ? Why or why not ?
# Ans. No, because normal dictionaries are mappings not a sequence.



# 12. What is the major difference between tuples and lists ?
# Ans. Tuples are immutable!



# 13. What is unique about a set ?
# Ans. They don’t allow for duplicate items !



# 14. Use a set to find the unique values of the list below
mylist = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(mylist))
# { 1, 2, 3, 4, 11, 22 }



# 15. What is the boolean output of the cell block below ?

list1 = [1, 2, [3, 4]]
list2  = [1, 2, {'k1': 4}]
# True or False
print(list1[2][0] >= list2[2]['k1'])
# False




# Great Job on your first assessment!