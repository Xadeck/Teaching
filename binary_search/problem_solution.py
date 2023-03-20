import datetime
import random
import time


def find_nina(target, birtdays):
    left = 0
    right = len(birtdays) - 1

    while left <= right:
        mid = int((left + right) / 2)

        if birtdays[mid] == target:
            return mid
        elif target < birtdays[mid]:
            right = mid - 1
        else:
            left = mid + 1


birthdays = []

# So I will make a list with (x) random dates
for i in range(3):
    day = random.randint(1, 30)
    month = random.randint(1, 12)
    year = random.randint(1980, 2023)

    birthdays.append((datetime.date(year, month, day), f"Person {i}"))

# Add Nina
Nina = (datetime.date(1988, 12, 27), "Nina")
birthdays.append(Nina)

# Sort the list
birthdays = sorted(birthdays, key=lambda p: (p[0].day))


#target = int(Nina[0].day)
#print(find_nina(target, birthdays))
