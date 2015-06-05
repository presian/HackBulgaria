def on_budget(books, budget):
    bookwithbudget = 0
    books = sorted(books)
    result = {}
    for i in range(0, len(books)):
        if budget >= books[i]:
            budget -= books[i]
            bookwithbudget += 1
        else:
            laon = sum(books[i:]) - budget
            result = {
                'books_on_budget': bookwithbudget,
                'loan': laon
            }
            break
    return result

print(on_budget([0, 10, 100, 5, 3, 8, 25], 35))
