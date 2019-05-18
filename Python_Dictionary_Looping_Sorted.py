# Python Dictionary Looping Techniques (sorted())
# To loop over a sequence in sorted order, use the sorted() 
# function which returns a new sorted list while leaving the source unaltered.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f)

# Displays 'apple'
# Displays 'banana'
# Displays 'orange'
# Displays 'pear'
