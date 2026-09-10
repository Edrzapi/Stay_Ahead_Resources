# PYP2 live demo - 03 comprehensions
# What we covered: list/set/dict comprehensions, filtering vs expressions,
# zip, map, flattening, and generator expressions.


# Aside from class: a one-element tuple is made by the COMMA, not brackets.
my_tup = 1,
print(type(my_tup))          # <class 'tuple'>


# ---------------------------------------------------------------------
# List comprehensions - [expression for item in iterable if condition]
# ---------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# Trailing 'if' FILTERS which items get through:
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]
print(squared_evens)         # [4, 16]

# An 'if/else' at the FRONT is part of the expression - it transforms
# every item rather than filtering any out:
str_results = ["even" if n % 2 == 0 else "odd"
               for n in numbers]
print(str_results)           # ['odd', 'even', 'odd', 'even', 'odd']


# ---------------------------------------------------------------------
# The books transforms (mini in-class dataset - the full one is in
# Tasks/Instruction/Task_Comprehensive_books.py)
# ---------------------------------------------------------------------
books = [
    {'id': 1, 'title': 'The Gruffalo', 'author': 'Donaldson', 'Genre': 'Childrens', 'ratings': [4, 5, 5]},
    {'id': 2, 'title': 'Python 101', 'author': 'Reynolds', 'Genre': 'Comp_Sci', 'ratings': [5, 5, 5]},
]

# Titles only - the leading expression projects one field:
titles = [b['title'] for b in books]

# Childrens books only - trailing 'if' filters whole books:
childrens = [b for b in books if b['Genre'] == 'Childrens']

# Combine both - project the title AND filter the genre:
childrens_titles = [b['title'] for b in books if b['Genre'] == 'Childrens']

# 'in' keeps a multi-genre condition readable:
educational = [b for b in books if b['Genre'] in ('Educational', 'Military', 'War', 'Science')]

# Project a (title, author) tuple while filtering:
classics = [(b['title'], b['author']) for b in books if b['Genre'] == 'Classics']

# Any expression can sit in the condition - here, the average rating:
top = [b for b in books
       if sum(b['ratings']) / len(b['ratings']) > 4]

# Conditions chain with 'and'; projection stays in the expression:
top_childrens = [(b['title'], b['author']) for b in books
                 if b['Genre'] == 'Childrens'
                 and sum(b['ratings']) / len(b['ratings']) > 4]
print(top_childrens)


# ---------------------------------------------------------------------
# Set comprehensions - { } and duplicates disappear
# ---------------------------------------------------------------------
duplication_numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 1, 123, 45, 5, 6]
names = ['Ed', 'Jeaneth', 'Alicia', 'Alicia']

# Transform AND dedupe in one go (plain set(names) can't do the .lower()):
unique_names = {name.lower() for name in names}
print(unique_names)

unique_numbers = {n for n in duplication_numbers}
print(unique_numbers)        # order not guaranteed - sets are unordered


# ---------------------------------------------------------------------
# Dict comprehensions - {key_expression: value_expression for item in iterable}
# ---------------------------------------------------------------------
squared_dict = {n: n ** 2 for n in numbers}
print(squared_dict)          # {1: 1, 2: 4, ...}

len_names = {name: len(name) for name in names}
print(len_names)             # duplicate keys simply overwrite - 'Alicia' appears once


# ---------------------------------------------------------------------
# zip - pair up two parallel lists element-wise
# ---------------------------------------------------------------------
students = ['bob', 'mary', 'tim', 'tim']
test_scores = [80, 65, 78, 78]

results = set(zip(students, test_scores))   # set drops the duplicate ('tim', 78)
print(results)


# ---------------------------------------------------------------------
# map - apply a function to every item: map(func, iterable)
# ---------------------------------------------------------------------
def square(num):
    return num ** 2


mapped_res = set(map(square, duplication_numbers))
print(mapped_res)

# Same with a lambda - map is lazy, so nothing runs until it's consumed:
lambda_squared_res = map(lambda x: x ** 2, numbers)
print(list(lambda_squared_res))


# ---------------------------------------------------------------------
# Nesting a lookup - give each book a full author dict
# ---------------------------------------------------------------------
authors = [
    {'first_name': 'Julia', 'last_name': 'Donaldson'},
    {'first_name': 'Ed', 'last_name': 'Reynolds'},
]

# Index the authors by last name once, then join in O(1) per book:
by_last = {a['last_name']: a for a in authors}
# {**b, ...} copies the book dict, then replaces its 'author' key:
result = [{**b, 'author': by_last[b['author']]} for b in books]
print(result)


# ---------------------------------------------------------------------
# Flattening - two 'for' clauses walk nested lists
# ---------------------------------------------------------------------
recipes = [{'name': 'spag bowl', 'ingredients': ['pasta', 'bolognese sauce']}]

ingredients = {
    item                        # one expression
    for r in recipes            # iterate the recipes
    for item in r['ingredients']  # then every ingredient of that recipe
}                               # curly braces -> a set, so it also dedupes
print(ingredients)


# ---------------------------------------------------------------------
# Generator expressions - a lazy comprehension, ( ) instead of [ ]
# ---------------------------------------------------------------------
mad_list_numbers = range(1, 1_000_000)

# Nothing is computed here - values are yielded one at a time on demand:
mad_squares = (x ** 2 for x in mad_list_numbers)
print(sum(mad_squares))      # values stream through sum(), never all in memory

mad_even_filter = (x for x in mad_list_numbers if x % 2 == 0)

# The list version below computes ALL million squares up front -
# same answer, ~8MB+ of memory the generator never needed:
# list_squares = [x ** 2 for x in range(1, 1_000_000)]
# print(sum(list_squares))
