import datetime
import random
import time


def find_nina(birthdays, index, low, high):

    for i in birthdays:
        if high >= low:
            mid = low + (high - low) / 2

            if birthdays[mid] == index:
                return mid
            if birthdays[low] > index:
                return find_nina(birthdays, index, low, mid - 1)
            return find_nina(birthdays, index, mid + 1, high)


birthdays = []

# So I will make a list with (x) random dates
for i in range(15):
    day = random.randint(1, 30)
    month = random.randint(1, 12)
    year = random.randint(1980, 2023)

    birthdays.append((datetime.date(year, month, day), f"Person {i}"))

# Add Nina
Nina = (datetime.date(1988, 12, 27), "Nina")
birthdays.append(Nina)

# Sort the list
birthdays = sorted(birthdays, key=lambda p: (p[0].day, p[0].month))


low = mid = 0
high = len(birthdays)
target = "maybe day and month"
print(target)
