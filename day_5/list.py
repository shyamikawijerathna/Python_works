
book_names = ["science","maths","English","IT",18]

print(book_names[2])

book_names[0]= "ET"

print(book_names)

print(len(book_names))

print(book_names[-1]) #access the last element

print(book_names[-2]) # Access the element before the last

for book_name in book_names:
    print(book_name)

book_names.append("SILO") # append to the list in last

book_names.insert(2,"Atomic habits") # insert atomic habit book in required position
print(book_names)

del book_names[2] #delete the item
print(book_names)

# print(help(book_names))

#remove the item
if "English" in book_names:
    book_names.remove("English")
print(book_names)

book_names.pop(2)
print(book_names)

