import datetime
import random
import time

# Uncomment the next line to always generate the same random list.
#
# random.seed(123)

birthdays = []

for i in range(1000000):
    y = random.randint(1975, 2006)
    m = random.randint(1, 12)
    d = random.randint(1, 28)
    birthdays.append((datetime.date(y, m, d), "P %d" % i))

Nina = (datetime.date(1988, 12, 27), "Nina")
birthdays.append(Nina)

moment_a = time.time()
birthdays = sorted(birthdays,
                   key=lambda p: (p[0].month, p[0].day))
moment_b = time.time()

# Homework: use binary search to find `index` faster.
index = birthdays.index(Nina)
moment_c = time.time()

print("before ", birthdays[index-1])
print("Nina is", birthdays[index])
print("after  ", birthdays[(index+1) % len(birthdays)])

print("Time to sort", moment_b - moment_a)
print("Time to find", moment_c - moment_b)
