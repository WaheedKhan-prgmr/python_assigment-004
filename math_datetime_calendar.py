# Math module
import math
print("Factorial of 5:", math.factorial(5))

# DateTime module
from datetime import datetime, timedelta
now = datetime.now()
print("Current time:", now)
print("Tomorrow:", now + timedelta(days=1))

# Calendar module
import calendar
print(calendar.month(2025, 5))
