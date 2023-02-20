import itertools
from collections import Counter

fruits = ["apple", "banana", "cherry"]

# combine all fruits into a single string
fruit_string = "".join(fruits)

# convert the string to lowercase
fruit_string = fruit_string.lower()

# count the frequency of each letter in the string
letter_counts = Counter(fruit_string)

# find the most common letter
most_common_letter = max(letter_counts, key=letter_counts.get)

print("The most common letter in the list of fruits is: " + most_common_letter)
