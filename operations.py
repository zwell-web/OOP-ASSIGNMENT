books = {}
members = []
genres = ('Fiction', 'Non-Fiction', 'Sci-Fi')

def add_book(ISBN, title, author, genre, total_copies):
    if ISBN in books:
        return "Book already exists in Freetown Library!"
    if genre not in genres:
        return "Invalid genre, stick to Sierra Leone's favorites!"
    if total_copies < 0:
        return "Total copies cannot be negative!"
    books[ISBN] = {"title": title, "author": author, "genre": genre, "total_copies": total_copies}
    return "Book added to Freetown Library successfully!"

def add_member(member_id, name, email):
    for member in members:
        if member['member_id'] == member_id:
            return "Member ID already exists in our community!"
    members.append({'member_id': member_id, 'name': name, 'email': email, 'borrowed_books': []})
    return "Member added to Sierra Leone Library community!"

def search_book(keyword):
    results = []
    for ISBN, details in books.items():
        if keyword.lower() in details['title'].lower() or keyword.lower() in details['author'].lower():
            results.append({"ISBN": ISBN, "title": details['title'], "author": details['author'], "genre": details['genre'], "total_copies": details['total_copies']})
    return results if results else "No books found in Freetown markets!"

def update_book(ISBN, **details):
    if ISBN not in books:
        return "Book not found in Freetown Library!"
    if 'genre' in details and details['genre'] not in genres:
        return "Invalid genre, check Sierra Leone's list!"
    if 'total_copies' in details and details['total_copies'] < 0:
        return "Total copies cannot be negative!"
    books[ISBN].update(details)
    return "Book updated at Freetown Library!"

def delete_book(ISBN):
    if ISBN not in books:
        return "Book not found in Freetown Library!"
    for member in members:
        if ISBN in member['borrowed_books']:
            return "Cannot delete: Book is borrowed by a Sierra Leonean!"
    del books[ISBN]
    return "Book deleted from Freetown Library!"

def borrow_book(ISBN, member_id):
    if ISBN not in books:
        return "Book not found in Freetown Library!"
    if books[ISBN]['total_copies'] <= 0:
        return "No copies left at the market!"
    member = next((m for m in members if m['member_id'] == member_id), None)
    if not member:
        return "Member not found in our community!"
    if len(member['borrowed_books']) >= 3:
        return "Member has reached the borrowing limit (3 books) from Freetown!"
    member['borrowed_books'].append(ISBN)
    books[ISBN]['total_copies'] -= 1
    return "Book borrowed from Freetown Library successfully!"

def return_book(ISBN, member_id):
    if ISBN not in books:
        return "Book not found in Freetown Library!"
    member = next((m for m in members if m['member_id'] == member_id), None)
    if not member:
        return "Member not found in our community!"
    if ISBN not in member['borrowed_books']:
        return "Member did not borrow this book from Freetown!"
    member['borrowed_books'].remove(ISBN)
    books[ISBN]['total_copies'] += 1
    return "Book returned to Freetown Library successfully!"