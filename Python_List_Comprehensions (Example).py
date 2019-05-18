# Python Data Structures List Comprehensions
# List comprehensions provide a concise way to create lists. 
# Common applications are to make new lists where each element is the result 
# of some operations applied to each member of another sequence or iterable, 
# or to create a subsequence of those elements that satisfy a certain condition.
# A list comprehension consists of brackets containing an expression followed by 
# a for clause, then zero or more for or if clauses. 
# The result will be a new list resulting from evaluating the expression in the 
# context of the for and if clauses which follow it. 
# For example, this listcomp combines the elements of two lists if they are not equal:

combs = []
    for x in [1,2,3]:
        for y in [3,1,4]:
            if x != y:
                combs.append((x, y))

combs
