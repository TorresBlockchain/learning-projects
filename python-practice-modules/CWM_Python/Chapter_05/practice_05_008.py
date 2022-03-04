# Lessons on sorting complex lists (tuples)

# python doesn't know how to sort these, so will need to define a function
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
