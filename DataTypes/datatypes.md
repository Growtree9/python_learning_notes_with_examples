## Datatypes in Python

- Python supports several built-in data types that allow you to represent and manipulate different kinds of data.
- These are your basic building blocks when constructing larger pieces of code.


|      Name      | Type  |                          Description                          |
|:--------------:|:-----:|:-------------------------------------------------------------:|
|    Integers    |  int  | Whole numbers, such as: 3  300 3000                           |
| Floating Point | float | Numbers with a decimal point: 2.3  4.6  100.0                 |
|    Strings     |  str  | Ordered sequence of characters: "hello" "sammy" "200" "#$*&"  |
|     Lists      | list  | Ordered sequence of objects: [10, "hello", 200.3]             |
|  Dictionaries  | dict  | Unordered Key:Value pairs: {"key1": "val1", "key": "val2"}    |
|     Tuples     |  tup  | Ordered immutable sequence of objects: (10, "hello" 200.3)    |
|      Sets      |  set  | Unordered collection of unique objects: ("a", "b")            |
|    Booleans    | bool  | Logical value indicating **True** or **False**                        |


- These data types serve as the building blocks for constructing more complex data structures and performing various operations in Python.
- Understanding these types is fundamental for effective programming in Python.
- Additionally, Python supports dynamic typing, meaning you don't need to explicitly declare the data type of a variable; it is determined at runtime.
- These data types provide flexibility and versatility for handling different kinds of data in Python programs.


### Variable Assignments
- We see that how to work with python datatypes.
- It would be nice to assign these data types a variable name to easily reference them later on in our code!
- For example,
  - my_dogs = 2
- **Rules for various names**
  - Name can not start with a number.
  - There can be no spaces in the same, use _instead.
  - Can't use any of these symbols :"',<>/?|\()!@#$%^&*-+
  - It's considered best practice (PEP8) that names are lowercase.
  - Avoid using words that have special meaning in Python like "list" and "str".
  - Python uses **Dynamic Typing**.
  - This means you can reassign variables to different data types.
  - This makes Python very flexible in assigning data types, this is different that other languages that are **Statically-Typed**.

- Pros of Dynamic Typing:
  - Very easy to work with
  - Faster development time
- Cons of Dynamic Typing:
  - May result in bugs for unexpected data types!
  - You need to be aware of **type()**