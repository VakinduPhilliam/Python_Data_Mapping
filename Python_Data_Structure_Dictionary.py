# Python Data Structure Dictionaries
# Unlike sequences (Lists, Strings etc.), which are indexed by a range of numbers, 
# dictionaries are indexed by keys, which can be any immutable type; 
# strings and numbers can always be keys. 

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel                       # Displays {'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']               # Displays 4098
del tel['sape']
tel['irv'] = 4127
tel                       # Displays {'jack': 4098, 'guido': 4127, 'irv': 4127}

list(tel)                 # Displays ['jack', 'guido', 'irv']
sorted(tel)               # Displays ['guido', 'irv', 'jack']
'guido' in tel            # Displays True
'jack' not in tel         # Displays False
