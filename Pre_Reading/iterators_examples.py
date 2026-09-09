# =========================================================
# PRE-READING: Iterators & Generators
# =========================================================
# Read this before tomorrow's session. Run the file, then
# uncomment the experiments as you go. Nothing here needs
# anything beyond plain Python.


# ---------------------------------------------------------
# 1. ITERABLE vs ITERATOR - two different jobs
# ---------------------------------------------------------
# An ITERABLE is anything you can loop over: lists, strings,
# dicts, files. Think of it as the BOOK.
# An ITERATOR is the object that keeps track of where you are
# in the loop. Think of it as the BOOKMARK.

names = ["Alice", "Bob", "Cara"]   # a list is an ITERABLE

# A for loop quietly asks the iterable for an iterator,
# then pulls items from it one at a time:
for name in names:
    print(name)


# ---------------------------------------------------------
# 2. WHAT THE FOR LOOP DOES UNDER THE HOOD
# ---------------------------------------------------------
# iter(x) asks the iterable for its iterator.
# next(it) pulls one item; when there is nothing left,
# Python raises StopIteration (the loop catches it for you).

it = iter(names)      # get the bookmark
print(next(it))       # Alice
print(next(it))       # Bob
print(next(it))       # Cara
# print(next(it))     # uncomment: raises StopIteration - the book is finished

# The iterator REMEMBERS its position - and it is one-shot.
# Once exhausted you need a fresh one from iter().


# ---------------------------------------------------------
# 3. THE SAME LOOP, WRITTEN BY HAND
# ---------------------------------------------------------
# This is literally what "for name in names" expands to:

it = iter(names)
while True:
    try:
        name = next(it)
    except StopIteration:
        break
    print(name)


# ---------------------------------------------------------
# 4. A CUSTOM ITERABLE - the two dunder methods
# ---------------------------------------------------------
# A class becomes iterable by defining __iter__ (return an
# iterator). An iterator defines __next__ (return the next
# item, or raise StopIteration). Here one class plays both
# roles - common and perfectly fine.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # "I am my own bookmark"
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration        # signals: no more items
        self.current -= 1
        return self.current + 1

for n in Countdown(3):
    print(n)          # 3, 2, 1


# ---------------------------------------------------------
# 5. GENERATORS - iterators without the boilerplate
# ---------------------------------------------------------
# A function containing 'yield' returns a GENERATOR: an
# iterator Python builds for you. Each 'yield' hands out a
# value and PAUSES the function; next() resumes it exactly
# where it left off. Think of yield as a pause button.

def countdown(start):
    while start > 0:
        yield start    # pause here, hand back a value
        start -= 1     # resumes from this line on the next next()

for n in countdown(3):
    print(n)          # 3, 2, 1 - same as the class, far less code


# ---------------------------------------------------------
# 6. WHY BOTHER? LAZINESS = MEMORY
# ---------------------------------------------------------
# A generator produces values ON DEMAND - it never builds the
# whole sequence in memory. This one can count forever; a list
# of "all numbers" could not exist.

def evens():
    n = 0
    while True:       # infinite - and that is fine
        yield n
        n += 2

gen = evens()
print(next(gen), next(gen), next(gen))   # 0 2 4 - only 3 values ever existed


# ---------------------------------------------------------
# 7. GENERATOR EXPRESSIONS - one-line generators
# ---------------------------------------------------------
# Same syntax as a list comprehension, but with ( ) instead
# of [ ]. The list builds everything NOW; the generator
# expression builds each value only when asked.

squares_list = [n * n for n in range(1_000_000)]   # ~1M values in memory now
squares_gen  = (n * n for n in range(1_000_000))   # nothing computed yet

print(sum(squares_gen))   # values stream through sum() one at a time

# Rule of thumb: if you only loop over it once, a generator
# expression is usually the better choice.


# ---------------------------------------------------------
# TOMORROW
# ---------------------------------------------------------
# We build a custom iterable class together, write generators,
# and look at where they shine (large files, data pipelines).
# Bring questions on anything above that felt odd - especially
# section 4, it is the one people find strangest.
