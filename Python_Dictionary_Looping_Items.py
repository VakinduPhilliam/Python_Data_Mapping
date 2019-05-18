# Python Dictionary Looping Techniques (Items ()).
# When looping through dictionaries, the key and corresponding 
# value can be retrieved at the same time using the items() method.

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
     for k, v in knights.items():
        print(k, v)

# Displays 'gallahad the pure'
# Displays 'robin the brave'
