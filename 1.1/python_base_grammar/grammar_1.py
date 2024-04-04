
# 1.1. about keywords in Python
# keywords are reserved words in Python that have special meanings
# they cannot be used as variable names, function names, or any other identifier names

# Keywords in Python:
# and, as, assert, break, class, continue, def, del, elif, else, except,
# False, finally, for, from, global, if, import, in, is, lambda, None,
# nonlocal, not, or, pass, raise, return, True, try, while, with, yield
# this list is not exhaustive, there are many more keywords in Python
# but these are the most commonly used ones
# you can find the complete list of keywords in the official Python documentation or by using the following example

# Example:
# import keyword
# print("keywords in Python:\n",keyword.kwlist)
# Output:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
# 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 2.about indentation in Python
# indentation is used to indicate the scope of a block of code

# example:

# this code block will give an error:
# if 10 > 5:
# print("10 is greater than 5")
# the error is:
# IndentationError: expected an indented block
# this is because the print statement is not indented under the if statement

# to fix this error, you need to indent the print statement under the if statement:


# if 10 > 5:
#     print("10 is greater than 5")

# the correct indentation is 4 spaces or 1.1 tab, but it is recommended to use 4 spaces for better readability


# 3.output and input in Python
# you can use the print() function to output data to the console
# and the input() function to get input from the user


# example:


# output:
# print("Hello, World!")


# input:
# name = input("What is your name? ")
# print("Hello, " + name + "!")


# 4.escape characters in Python
# escape characters are used to represent special characters in strings


# \n is used to represent a new line
# \t is used to represent a tab
# \\ is used to represent a backslash
# \" is used to represent a double quote
# \' is used to represent a single quote
# \r is used to represent a carriage return
# \b is used to represent a backspace


# example:


# string1 = "This is a string\nwith a new line"
# string2 = "This is a string\twith a tab"
# string3 = "This is a string\\with a backslash"
# string4 = "This is a string\"with a double quote"
# string5 = "This is a string\'with a single quote"
# string6 = "This is a string\rwith a carriage return"
# string7 = "This is a string\bwith a backspace"
# string8 = r"this is a string with a \n"


# print(string1)
# print(string2)
# print(string3)
# print(string4)
# print(string5)
# print(string6)
# print(string7)
# print(string8)


# Output:
# This is a string
# with a new line
# This is a string	with a tab
# This is a string\with a backslash
# This is a string"with a double quote
# This is a string'with a single quote
# with a carriage return
# This is a strinwith a backspace


# 5.variables in Python
# variables are used to store data values
# you can create a new variable by assigning a value to it
# you can also update the value of an existing variable
# variables can include letters(Aa-Zz), numbers(0-9), and underscores(_)
# but they cannot start with a number


# example:

# create a new variable
# variable1_ = 10
# print(variable1_)
# Output: 10
# _variable2 = "Hello, World!"
# print(_variable2)
# Output: Hello, World!

# 6.data types in Python
# data types are used to define the kind of data that can be stored in a variable
# in Python, there are several built-in data types:
# - Numbers
# - Strings
# - Lists
# - Tuples
# - Sets
# - Dictionaries


# 7.numbers in Python
# numbers are used to represent values that are quantitative
# in Python, there are two types of numbers:
# - Integers
# - Floats


# example:


# integers
# variable1 = 10
# variable2 = -5
# variable3 = 0
# print(variable1)
# print(variable2)
# print(variable3)
# Output: 10 -5 0


# floats
# variable1 = 3.14
# variable2 = -2.5
# variable3 = 0.0
# print(variable1)
# print(variable2)
# print(variable3)
# Output: 3.14 -2.5 0.0


# 8.strings in Python
# strings are used to represent textual data
# in Python, strings are enclosed in either single quotes or double quotes
# you can use escape characters to represent special characters in strings


# example:


# create a string
# variable1 = "Hello, World!"
# variable2 = 'Hello, World!'
# print(variable1)
# print(variable2)
# Output: Hello, World! Hello, World!


# 9.lists in Python
# lists are used to store a collection of items
# in Python, lists are enclosed in square brackets []
# you can use the append() method to add items to a list
# you can use the len() function to get the number of items in a list


# example:


# create a list
# variable1 = [1, 2, 3, 4, 5]
# variable2 = ["apple", "banana", "cherry"]
# print(variable1)
# print(variable2)
# Output: [1, 2, 3, 4, 5] ['apple', 'banana', 'cherry']


# add items to a list
# variable1.append(6)
# print(variable1)
# Output: [1, 2, 3, 4, 5, 6]


# get the number of items in a list
# print(len(variable1))
# Output: 6


# 10.tuples in Python
# tuples are used to store a collection of items
# in Python, tuples are enclosed in parentheses ()
# you cannot modify the items in a tuple
# you can use the len() function to get the number of items in a tuple


# example:


# create a tuple
# variable1 = (1, 2, 3, 4, 5)
# variable2 = ("apple", "banana", "cherry")
# print(variable1)
# print(variable2)
# Output: (1, 2, 3, 4, 5) ('apple', 'banana', 'cherry')


# get the number of items in a tuple
# print(len(variable1))
# Output: 5


# 11.sets in Python
# sets are used to store a collection of unique items
# in Python, sets are enclosed in curly braces {}
# you can use the add() method to add items to a set
# you can use the len() function to get the number of items in a set


# example:


# create a set
# variable1 = {1, 2, 3, 4, 5}
# variable2 = {"apple", "banana", "cherry"}
# print(variable1)
# print(variable2)
# Output: {1, 2, 3, 4, 5} {'apple', 'banana', 'cherry'}


# add items to a set
# variable1.add(6)
# print(variable1)
# Output: {1, 2, 3, 4, 5, 6}


# get the number of items in a set
# print(len(variable1))
# Output: 6


# 12.dictionaries in Python
# dictionaries are used to store a collection of key-value pairs
# in Python, dictionaries are enclosed in curly braces {}
# you can use the key to access the value associated with that key
# you can use the items() method to get a list of key-value pairs in a dictionary
# you can use the len() function to get the number of key-value pairs in a dictionary


# example:


# create a dictionary
# variable1 = {"name": "John", "age": 30, "city": "New York"}
# variable2 = {1: "apple", 2: "banana", 3: "cherry"}
# print(variable1)
# print(variable2)
# Output: {'name': 'John', 'age': 30, 'city': 'New York'} {1: 'apple', 2: 'banana', 3: 'cherry'}


# access the value associated with a key
# print(variable1["name"])
# Output: John


# get a list of key-value pairs in a dictionary
# print(variable1.items())
# Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])


# 13.operators in Python
# operators are used to perform operations on variables and values
# in Python, there are several types of operators:
# - Arithmetic operators(+, -, *, /, //, %, **)
# - Comparison operators(==, !=, <, >, <=, >=)
# - Logical operators(and, or, not)
# - Assignment operators(=, +=, -=, *=, /=, //=, %=, **=)
# - Bitwise operators(&, |, ^, ~, <<, >>)
# - Membership operators(in, not in)
# - Identity operators(is, is not)


# 14.none in Python
# None is a special keyword in Python
# it represents the absence of a value
# you can use None to indicate that a variable has not been assigned a value
# None is a data type in Python


# example:


# create a variable with no value
# variable1 = None
# print(variable1)
# Output: None


# 15.comments in Python
# comments are used to add explanatory notes to the code
# in Python, comments are enclosed in either # or """ """
# they are ignored by the interpreter and are not executed


# example:


# this is a comment
# print("This code will not be executed")


# """
# This is a multi-line
# comment
# """
# print("This code will not be executed")


# 16.string formatting in Python
# string formatting is used to insert values into a string
# in Python, you can use the format() method to format a string
# you can use positional arguments or keyword arguments to insert values into the string


# example:


# format a string with positional arguments
# variable1 = "Hello, {}!"
# variable2 = "John"
# print(variable1.format(variable2))
# Output: Hello, John!


# format a string with keyword arguments
# variable1 = "Hello, {name}!"
# variable2 = {"name": "John"}
# print(variable1.format(**variable2))

# Output: Hello, John!


# 17.string methods in Python
# string methods are used to manipulate strings
# in Python, there are several string methods:

# - capitalize() -- capitalize the first letter of the string
# string = "dsc".capitalize()
# print(string)

# - casefold() -- convert the string to lowercase
# string = "DSC".casefold()
# print(string)

# - center() -- center the string in a field of a given width
# string = "hello".center(11, "*")
# print(string)

# - count() -- count the number of occurrences of a substring
# string = "hello world".count("l")
# print(string)

# - encode() -- encode the string
# - endswith() -- check if the string ends with a given substring
# - expandtabs() -- replace tabs with spaces

# - find() -- find the index of a substring
# string = "hello world".find("l")
# print(string)

# - format() -- format the string
# string = "Hello, {name}!".format(name="John")
# print(string)

# - format_map() -- format the string using a mapping

# - index() -- find the index of a substring
# string = "hello world".index("l")
# print(string)

# - isalnum() -- check if the string is alphanumeric
# - isalpha() -- check if the string is alphabetic
# - isascii() -- check if the string is ASCII
# - isdecimal() -- check if the string is decimal
# - isdigit() -- check if the string is a digit
# - isidentifier() -- check if the string is a valid identifier
# - islower() -- check if the string is lowercase
# - isnumeric() -- check if the string is numeric
# - isprintable() -- check if the string is printable
# - isspace() -- check if the string is a whitespace character
# - istitle() -- check if the string is titlecase
# - isupper() -- check if the string is uppercase

# - join() -- join the elements of a list into a string
# string = " , ".join(["apple", "banana", "cherry"])
# print(string)

# - ljust() -- left-justify the string in a field of a given width

# - lower() -- convert the string to lowercase
# string = "DSC".lower()
# print(string)

# - lstrip() -- remove leading whitespace
# - maketrans() -- create a translation table
# - partition() -- partition the string into three parts

# - replace() -- replace a substring with a given string
# string = "hello world".replace("l", "L")
# print(string)

# - rfind() -- find the index of a substring starting from the end of the string
# - rindex() -- find the index of a substring starting from the end of the string
# - rjust() -- right-justify the string in a field of a given width
# - rpartition() -- partition the string into three parts starting from the end of the string
# - rsplit() -- split the string into a list of substrings starting from the end of the string
# - rstrip() -- remove trailing whitespace

# - split() -- split the string into a list of substrings
# string = "hello,world".split(",")
# print(string)

# - splitlines() -- split the string into a list of lines
# string = "hello\nworld".splitlines()
# print(string)

# - startswith() -- check if the string starts with a given substring

# - strip() -- remove leading and trailing whitespace
# string = "   hello world   ".strip()
# print(string)

# - swapcase() -- swap case
# - title() -- convert the string to titlecase
# - translate() -- translate the string

# - upper() -- convert the string to uppercase
# string = "sss".upper()
# print(string)

# - zfill() -- fill the string with zeros on the left
# string = "123".zfill(5)
# print(string)

# 18.list methods in Python
# list methods are used to manipulate lists
# in Python, there are several list methods:
# - append() -- add an item to the end of the list
# - clear() -- remove all items from the list
# - copy() -- create a shallow copy of the list
# - count() -- count the number of occurrences of an item
# - extend() -- add items from another list
# - index() -- find the index of an item
# - insert() -- insert an item at a given index
# - pop() -- remove and return an item at a given index
# - remove() -- remove an item from the list
# - reverse() -- reverse the order of the items in the list
# - sort() -- sort the items in the list


# 19.tuple methods in Python
# tuple methods are used to manipulate tuples
# in Python, there are several tuple methods:
# - count() -- count the number of occurrences of an item
# - index() -- find the index of an item


# 20.set methods in Python
# set methods are used to manipulate sets
# in Python, there are several set methods:
# - add() -- add an item to the set
# - clear() -- remove all items from the set
# - copy() -- create a shallow copy of the set
# - difference() -- return the difference of two sets
# - difference_update() -- remove all items from the set that are also in another set
# - discard() -- remove an item from the set if it is a member
# - intersection() -- return the intersection of two sets
# - intersection_update() -- update the set with the intersection of itself and another
# - isdisjoint() -- check if two sets have a null intersection
# - issubset() -- check if another set contains this set
# - issuperset() -- check if this set contains another set
# - pop() -- remove and return an arbitrary item from the set
# - remove() -- remove an item from the set
# - symmetric_difference() -- return the symmetric difference of two sets
# - symmetric_difference_update() -- update the set with the symmetric difference of itself and another
# - union() -- return the union of two sets
# - update() -- update the set with the union of itself and another


# 21.dictionary methods in Python
# dictionary methods are used to manipulate dictionaries
# in Python, there are several dictionary methods:
# - clear() -- remove all items from the dictionary
# - copy() -- create a shallow copy of the dictionary
# - fromkeys() -- create a new dictionary with the specified keys and values
# - get() -- get the value of a key
# - items() -- get a list of key-value pairs
# - keys() -- get a list of keys
# - popitem() -- remove and return an arbitrary key-value pair
# - setdefault() -- get the value of a key, or add a key with a default value
# - update() -- update the dictionary with the key-value pairs from another dictionary
# - values() -- get a list of values
