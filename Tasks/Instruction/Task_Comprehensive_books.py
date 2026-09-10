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

# Worked example - titles only:
titles = [b["title"] for b in books]
print(titles)

# TODO: childrens books only (hint: a trailing 'if' filters)

# TODO: titles of childrens books only

# TODO: educational and military/war books only

# TODO: title and author of classics only (hint: the leading expression
#       can build a tuple or a small dict per book)

# TODO: books with average rating greater than 4 only
#       (hint: sum(ratings) / len(ratings))

# TODO: title and author of childrens books with average rating > 4
