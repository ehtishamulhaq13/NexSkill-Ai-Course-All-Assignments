book_list = [456, "thinking glow rich", "nipolian hil", 44.0]
print(book_list)
print(type(book_list))
print(len(book_list))

for x in book_list:
    print(x)


print(book_list[2])
print(type(book_list[2]))
print(type(book_list[3]))

book_list.append("abc publisher")
print("After append(abc publisher):", book_list)

book_list.insert(1, 1977)
print(book_list)

book_list.remove(44.0)
print(book_list)

book_list.pop(4)
print(book_list)
