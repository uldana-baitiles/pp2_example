#task1
#Write a Python program to subtract five days from current date
"""
from datetime import datetime,timedelta
today=datetime.now()
new=today-timedelta(days=5)
print(new)
"""


#task2
#Write a Python program to print yesterday, today, tomorrow.
"""
from datetime import datetime,timedelta
today=datetime.now()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

"""


