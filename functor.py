from functools import cache

def debug(func):
    def modified(n):
        print("calling with", n)
        v = func(n)
        print("returning ", v)
        return v
    return modified

# A function can take an input and return an output.
#
# So far we have only use input that are values (int, string, pair).
#
# But a function can take another function. This is called a "functor"
# or sometimes "high order functions" (those names come from maths)

# The syntax '@' is canned a "decorator". It just means that the function
# will we transformed or "wrapped" into another function.
#
# Decorators are useful to "add" a behavior to a function.
# It allows composing things, and re-usingthings (like my cache)
@cache
@debug
def fibonaci(n):
    if n == 0 or n == 1:
        return 1
    return fibonaci(n-2) + fibonaci(n-1)

for i in range(1,10):
    print(fibonaci(i))


