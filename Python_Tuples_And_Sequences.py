# Python Tuples and Sequences
# We saw that lists and strings have many common properties, 
# such as indexing and slicing operations. 
# They are two examples of sequence data types (lists, strings, range). 
# Since Python is an evolving language, other sequence data types may be added. 
# There is also another standard sequence data type: the tuple. 
# A tuple consists of a number of values separated by commas, for instance:
# Though tuples may seem similar to lists, they are often used in different 
# situations and for different purposes. 
# Tuples are immutable, and usually contain a heterogeneous sequence of 
# elements that are accessed via unpacking or 
# indexing (or even by attribute in the case of namedtuples).

t = 12345, 54321, 'hello!'
t[0] # Displays 12345
t # Displays (12345, 54321, 'hello!')

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u # Displays ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
# but they can contain mutable objects:

v = ([1, 2, 3], [3, 2, 1])
v # Displays ([1, 2, 3], [3, 2, 1])
