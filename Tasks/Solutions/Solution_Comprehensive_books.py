books = [
    {"id": 1, "title": "The Gruffalo", "author": "Donaldson", "genre": "Childrens", "ratings": [5, 4, 5, 5, 5, 3, 5]},
    {"id": 2, "title": "Java How to Program", "author": "Dietel", "genre": "Educational", "ratings": [3, 4, 3, 3, 5, 3, 4]},
    {"id": 3, "title": "Harry Potter and the Philosopher's Stone", "author": "Rowling", "genre": "Fiction", "ratings": [5, 5, 5, 5, 3, 4, 5, 5, 5]},
    {"id": 4, "title": "The Great War", "author": "Carlyon", "genre": "Military/War", "ratings": [4, 3, 4, 5, 5, 4, 1, 4]},
    {"id": 5, "title": "Mr Strong", "author": "Hargreaves", "genre": "Childrens", "ratings": [3, 3, 2, 4, 5, 3, 4]},
    {"id": 6, "title": "The Greatest Show on Earth", "author": "Dawkins", "genre": "Non-fiction", "ratings": [3, 3, 4, 3, 2, 4, 5, 3, 3, 2, 5, 4, 4, 4]},
    {"id": 7, "title": "Wind in the Willows", "author": "Grahame", "genre": "Childrens", "ratings": [4, 5, 5, 4, 4, 3, 5, 5, 5, 4]},
    {"id": 8, "title": "The Churchill Factor", "author": "Johnson", "genre": "Military/War", "ratings": [3, 1, 4, 2, 2, 3, 1, 5, 3, 4, 3, 2]},
    {"id": 9, "title": "On Liberty", "author": "Mill", "genre": "Classics", "ratings": [4, 5, 3, 4, 2]},
    {"id": 10, "title": "Macbeth", "author": "Shakespeare", "genre": "Classics", "ratings": [5, 5, 4, 5, 5, 5]},
]

# Titles only - the leading expression PROJECTS just the field we want.
titles = [b["title"] for b in books]
print(titles)

# Childrens books only - a trailing 'if' FILTERS whole books.
childrens = [b for b in books if b["genre"] == "Childrens"]
print(childrens)

# Titles of childrens books - project AND filter in one comprehension.
childrens_titles = [b["title"] for b in books if b["genre"] == "Childrens"]
print(childrens_titles)

# Educational and military/war books - 'in' keeps the condition readable
# (clearer than two == checks joined with 'or').
edu_military = [b for b in books if b["genre"] in ("Educational", "Military/War")]
print(edu_military)

# Title and author of classics - the expression can build a tuple...
classics = [(b["title"], b["author"]) for b in books if b["genre"] == "Classics"]
print(classics)

# ...or a small dict per book, whichever reads better downstream.
classics_dicts = [
    {"title": b["title"], "author": b["author"]}
    for b in books
    if b["genre"] == "Classics"
]
print(classics_dicts)

# Books with average rating > 4 - any expression can appear in the 'if'.
well_rated = [b for b in books if sum(b["ratings"]) / len(b["ratings"]) > 4]
print([b["title"] for b in well_rated])

# Title and author of childrens books with average rating > 4 -
# conditions chain with 'and', projection stays in the expression.
top_childrens = [
    (b["title"], b["author"])
    for b in books
    if b["genre"] == "Childrens" and sum(b["ratings"]) / len(b["ratings"]) > 4
]
print(top_childrens)
