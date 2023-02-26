# We learn about standard python library.
from collections import defaultdict


# We learn about 'context' and automatically close the file.
with open('words.txt', 'r') as file:
    words = [w.strip() for w in file.readlines()]

# We learn about default values in dictionary
anagrams = defaultdict(list)

# We learn how to reuse code by making a function
def make_key(word):
    return "".join(sorted(word))

for word in words:
    key = make_key(word)
    anagrams[key].append(word)

example = input("give an English word:")
# We learn to be careful about bugs and to check
# that it makes sense to use some data.
if not example in words:
    print("I don't know", example)
else:
    # We learn to not ABUSE least comprehensions when it's too complicated.
    # We learn about python builtins (like enumerate)
    # (https://docs.python.org/3/library/functions.html)
    for n, word in enumerate(anagrams[make_key(example)]):
        print("%2d %s" % (n, word))

