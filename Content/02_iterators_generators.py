# PYP2 live demo - 02 iterators & generators
# What we covered: iterable vs iterator, iter()/next(), the for loop
# under the hood, custom iterables, generators, and lazy evaluation.


# ---------------------------------------------------------------------
# Iterable vs iterator
# ---------------------------------------------------------------------
# An ITERABLE is something you can loop over (the book).
# An ITERATOR is the object tracking your position (the bookmark).

my_str = "string"          # a string is an ITERABLE - it produces new iterators
my_iter = iter(my_str)     # iter() calls __iter__, which returns an iterator
print(next(my_iter))       # next() calls __next__ - returns the next item: 's'

# Q1: Iterable vs Iterator?
#     The iterable PRODUCES iterators (a fresh one per loop).
#     The iterator returns ITSELF from __iter__ and moves forward via next -
#     it remembers where it is, and it is one-shot.

# Q2: The built-ins: A) iterator-from-iterable -> iter()
#                    B) next item             -> next()

# Q3: Rewrite the for loop in its iter/next/exception form
#     ("reinvent the wheel" - this is exactly what 'for' does for you):
seq = [1, 2, 3]
it = iter(seq)
while True:
    try:
        i = next(it)
    except StopIteration:   # the iterator's way of saying "no more items"
        print("no more items")
        break
    print(i)


# ---------------------------------------------------------------------
# A custom iterable - implement __iter__ and __next__ yourself
# ---------------------------------------------------------------------
# Typical use case: we want to count something.
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        # "I am my own bookmark" - one class playing both roles.
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration      # NOT return - raise. The loop catches it.
        value = self.current
        self.current += 1
        return value


c = Counter(1, 5)
for number in c:
    print(number)            # 1 2 3 4 5


# Same pattern, more interesting sequence: 0 1 1 2 3 5 8 13 21 34 55 89
class Fibonacci:
    def __init__(self, max):
        self.max = max
        self.a, self.b = 0, 1

    def __iter__(self):
        return self          # this object IS its own iterator

    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        value = self.a
        # tuple assignment steps both numbers forward in one line
        self.a, self.b = self.b, self.a + self.b
        return value


for n in Fibonacci(100):
    print(n)


# ---------------------------------------------------------------------
# Generators - iterators without the class boilerplate
# ---------------------------------------------------------------------
# 'yield' hands a value out and PAUSES the function; next() resumes it
# exactly where it left off. Watch the "resume" prints interleave:

def simple_gen():
    yield 1
    print("resume")          # runs when the SECOND value is requested
    yield 2
    print("resume")
    yield 3


for n in simple_gen():
    print(n)


# Exercise: a generator giving the multiples of 6 up to a max.
def multi_of_six(max):
    n = 6
    while n <= max:
        yield n              # hand the multiple over, then pause here
        n += 6               # on resume, step to the next multiple


print(list(multi_of_six(100)))

# range() is itself a lazy iterable - it never builds the full list:
for i in range(1, 11):
    print(i)
