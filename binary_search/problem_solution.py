import datetime
import random
import time


def find_nina(target, birthdays):
    left = 0
    right = len(birthdays) - 1

    while left <= right:
        mid = int((left + right) // 2)

        if birthdays[mid][0].day == target.day and birthdays[mid][0].month == target.month:
            return mid
        elif target.day < birthdays[mid][0].day and target.month <= birthdays[mid][0].month:
            right = mid - 1
        else:
            left = mid + 1


birthdays = []

# So I will make a list with (x) random dates
for i in range(1000000):
    day = random.randint(1, 26)
    month = random.randint(1, 11)
    year = random.randint(1989, 2023)

    birthdays.append((datetime.date(year, month, day), f"Person {i}"))

# Add Nina
Nina = datetime.date(1988, 12, 27)
birthdays.append((Nina, "Nina"))

# Sort the list
time_a = time.time()
birthdays = sorted(birthdays, key=lambda p: (p[0].day, p[0].month))
time_b = time.time()

target = Nina

index = find_nina(target, birthdays)
time_c = time.time()

# Now I should print the result:
print(f"Person before Nina is: {birthdays[index-1]}")
print(f"Nina is: {birthdays[index][1]}")
print(f"Person after Nina is: {birthdays[(index + 1)  % len(birthdays)]}")

print(f"Sort time: {time_b - time_a:.6f} seconds")
print(f"Find time: {time_c - time_b:.6f} seconds")
