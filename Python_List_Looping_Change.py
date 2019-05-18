# Python List looping Change
# It is sometimes tempting to change a list while you are looping over it; 
# however, it is often simpler and safer to create a new list instead.

import math
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filtered_data = []
     for value in raw_data:
         if not math.isnan(value):
            filtered_data.append(value)

filtered_data        # Displays [56.2, 51.7, 55.3, 52.5, 47.8]
