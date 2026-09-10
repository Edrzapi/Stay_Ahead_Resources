names = [
    "alice",
    "bob",
    "alice",
    "charlie",
    "bob",
    "dave"
]


# A SET comprehension uses { } with a single expression.
# Sets cannot hold duplicates, so repeats disappear automatically -
# no manual "have I seen this?" bookkeeping needed.
unique_names = {name for name in names}
print(unique_names)          # order not guaranteed - sets are unordered

# (set(names) does the same job here; the comprehension form earns its
# keep once you also want to transform, e.g. {n.title() for n in names})


# A DICT comprehension uses { } with a key: value expression.
# Duplicate keys simply overwrite each other, so each name appears once.
name_lookup = {name: name.upper() for name in names}
print(name_lookup)           # {'alice': 'ALICE', 'bob': 'BOB', ...}
