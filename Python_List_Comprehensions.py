# Python Data Structures List Comprehensions
# List comprehensions provide a concise way to create lists. 
# Common applications are to make new lists where each element is the result 
# of some operations applied to each member of another sequence or iterable, 
# or to create a subsequence of those elements that satisfy a certain condition.
# For Example;

squares = list(map(lambda x: x**2, range(10)))
squares

# Or Equivalently

squares1 = [x**2 for x in range(10)]
squares1
