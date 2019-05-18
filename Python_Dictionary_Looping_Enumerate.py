# Python Dictionary Looping Techniques (Enumerate)
# When looping through a sequence, the position index and corresponding 
# value can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

# Displays '0 tic'
# Displays '1 tac'
# Displays '2 toe'
