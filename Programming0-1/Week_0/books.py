book1_name = "Pragmatic Thinking and Learning"
book1_price = 30
book2_name = "Learn You a Haskell"
book2_price = 0
book3_name = "The Healthy Programmer"
book3_price = 50
book4_name = "Code Complete"
book4_price = 60
book5_name = "The Pragmatic Programmer"
book5_price = 20
book6_name = "Pro Git"
book6_price = 0
book7_name = "Introduction to Algorithms"
book7_price = 80
book8_name = "Concrete Mathematics"
book8_price = 100

books = [[book1_name, book1_price], [book2_name, book2_price], [book3_name, book3_price], [book4_name, book4_price],  [book5_name, book5_price], [book6_name, book6_price], [book7_name, book7_price], [book8_name, book8_price]]

for book in books:
	print (str.format("Book: {0}, Price: {1}", book[0], book[1]))

sum_price = 0
for book in books:
	sum_price += book[1]

print("Sum of all books: " + str(sum_price))

print("All books are: " + str(len(books)))

print("Price is: " + str((books[6][1] + books[7][1])*0.75))

sortedBooksByPrice = sorted(books, key = lambda book: book[1])
print(sortedBooksByPrice)


current_price = 0
max_count_books_for_150 = []
for book in sortedBooksByPrice:
	if current_price + book[1] <= 150 :
		max_count_books_for_150.append(book)
		current_price += book[1]
	else:
		break

print("Maximal count of books for 150 are: " + str(len(max_count_books_for_150)))