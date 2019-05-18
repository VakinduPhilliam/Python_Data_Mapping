# Python 'del' statement
# There is a way to remove an item from a list given its index instead 
# of its value: the del statement. 
# This differs from the pop() method which returns a value. 
# The del statement can also be used to remove slices from a list or clear 
# the entire list (which we did earlier by assignment of an empty list to the slice).

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
del a[2:4]
a
del a[:]
a
del a # Deletes entire variable
