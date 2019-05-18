# Python Data Structure Sets
# Python also includes a data type for sets. 
# A set is an unordered collection with no duplicate elements. 
# Basic uses include membership testing and eliminating duplicate entries. 
# Set objects also support mathematical operations like union, 
# intersection, difference, and symmetric difference.
# Curly braces or the set() function can be used to create sets. 
# Note: to create an empty set you have to use set(), not {}; the latter 
# creates an empty dictionary.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)                      # show that duplicates have been removed
                                   # Displays {'orange', 'banana', 'pear', 'apple'}

'orange' in basket                 # fast membership testing
'crabgrass' in basket

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
a - b                              # letters in a but not in b
a | b                              # letters in a or b or both
a & b                              # letters in both a and b
a ^ b                              # letters in a or b but not both
