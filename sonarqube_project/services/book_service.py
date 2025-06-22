books = {
    1: {'id': 1, 'name': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'title': 'The Great Gatsby', 'year': 1925},
    2: {'id': 2, 'name': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'title': 'To Kill a Mockingbird', 'year': 1960},
    3: {'id': 3, 'name': '1984', 'author': 'George Orwell', 'title': '1984', 'year': 1949}
}

def get_all_books():
    return list(books.values())

def get_book_by_id(book_id):
    if book_id in books:
        return books[book_id]
    return None

def create_book(book_data):
    book_id = max(books.keys()) + 1
    book_data['id'] = book_id
    books[book_id] = book_data
    return book_data

def update_book(book_id, book_data):
    if book_id in books:
        books[book_id].update(book_data)
        return books[book_id]
    # Intentionally returning None which can cause issues in the router
    return None

def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        return True
    return False

def find_books_by_author(author_name):
    # This function has high cognitive complexity for demonstration
    results = []
    for book_id in books:
        if 'author' in books[book_id]:
            if books[book_id]['author'] == author_name:
                results.append(books[book_id])
    # Duplicate code block for checking author
    for book_id in books:
        if 'author' in books[book_id]:
            if books[book_id]['author'] == author_name:
                if books[book_id] not in results:
                    results.append(books[book_id])
    return results