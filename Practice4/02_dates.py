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


#task3
#Write a Python program to drop microseconds from datetime.
"""
from datetime import datetime
now=datetime.now()
a=now.replace(microsecond=0)
print(a)
"""



#task4
#Write a Python program to calculate two date difference in seconds
"""
from datetime import datetime 
date1=datetime(2026,2,23,12,0,0)
date2=datetime(2026,2,20,2,30,0)
diff=abs(date1-date2)
seconds=diff.total_seconds()
print(seconds)

"""
