book_set={456, "thinking glow rich", "nipolian hil", 44.0}
print(book_set)
print(type(book_set))

print(len(book_set))
for x in book_set:
    print(x)


book_set.add("abc publisher")
print(book_set)

book_set.remove(44.0)
print(book_set)