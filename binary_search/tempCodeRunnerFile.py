import datetime
import random
import time

birthdays = []
# So I will make a list with (x) random dates
for i in range(10):
    day = random.randint(1, 30)
    month = random.randint(1, 12)
    year = random.randint(1980, 2023)

    birthdays.append((datetime.date(year, month, day), f"Person {i}"))


Nina = (datetime.date(1988, 12, 27), "Nina")
birthdays.append(Nina)

print(birthdays)
for i in birthdays:
    print(i)
