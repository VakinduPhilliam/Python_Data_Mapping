# Python Dictionary Looping Techniques (zip())
# To loop over two or more sequences at the same time, the 
# entries can be paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))

# Displays 'What is your name?  It is lancelot.'
# Displays 'What is your quest?  It is the holy grail.'
# Displays 'What is your favorite color?  It is blue'
