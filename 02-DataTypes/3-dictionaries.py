# Dictionaries are unordered mappings for storing objects.
# Dictionaries use a key-value pairing instead.
# This key-value pair allows users to quickly grab objects without needing to know an index location.
# Dictionaries use curly braces and colons to signify the keys and their associated values.
# Example:
my_dict = { "key1": "value1", "key2": "value1" }
# Objects retrived by key name.
# They are unordered in nature and can not be sorted.



print(my_dict)
# {'key1': 'value1', 'key2': 'value2'}

print(my_dict['key2'])
# value2

print(type(my_dict['key1'])) # type checks datatype of value
# String


price_lookup = {'apple': 30.55, 'oranges': 40, 'milk': 22.43}

print(price_lookup['milk'])
# 22.43


complex_dict = {'k1': 125, 'k2': [1,2,3], 'k3': {'k4': 100}}

print(complex_dict['k2'])
# [1, 2, 3]

print(complex_dict['k3']['k4'])
# 100

print(complex_dict.keys())
# dict_keys(['k1', 'k2', 'k3'])

print(complex_dict.values())
# dict_values([123, [1, 2, 3], {'k4': 100}])

print(complex_dict.items())
# dict_items([('k1', 125), ('k2', [1, 2, 3]), ('k3', {'k4': 100})])




# 1. Methods:

d = {'key1': ['a', 'b', 'c']}

print(d['key1'][1].upper())
# B

