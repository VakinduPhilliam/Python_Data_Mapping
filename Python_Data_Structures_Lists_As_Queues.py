# Python Data Structures Lists as Queues.
# It is also possible to use a list as a queue, where the first 
# element added is the first element retrieved (“first-in, first-out”).
# But the above is NOT efficient
# To implement a queue efficiently, use 'collections.deque' which was designed 
# to have fast appends and pops from both ends

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
queue                           # Remaining queue in order of arrival
