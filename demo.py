import operations

# Add books
print(operations.add_book("SL001", "Tales of Freetown", "Aminata Kamara", "Fiction", 3))
print(operations.add_book("SL002", "Sierra Leone History", "Saidu Conteh", "Non-Fiction", 2))

# Add members
print(operations.add_member(1, "Fatima Bangura", "fatima@freetown.sl"))
print(operations.add_member(2, "Ibrahim Sesay", "ibrahim@slmarket.sl"))

# Borrow books
print(operations.borrow_book("SL001", 1))  # Should work
print(operations.borrow_book("SL002", 1))  # Should work
print(operations.borrow_book("SL002", 1))  # Error: No copies left

# Search for a book
print(operations.search_book("Freetown"))

# Update a book
print(operations.update_book("SL001", title="Tales of Freetown Market"))

# Return a book
print(operations.return_book("SL001", 1))  # Should work

# Delete a book
print(operations.delete_book("SL001"))  # Should work after return
print(operations.delete_book("SL003"))  # Error: Book not found

# Try to borrow with max limit
print(operations.borrow_book("SL001", 1))  # Should work
print(operations.borrow_book("SL002", 1))  # Should fail: 3 books limit