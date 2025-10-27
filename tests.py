import operations

# Reset data for testing
operations.books = {}
operations.members = []
operations.genres = ('Fiction', 'Non-Fiction', 'Sci-Fi')

# Test 1: Add a book successfully
operations.add_book("SL001", "Tales of Freetown", "Aminata Kamara", "Fiction", 3)
assert "SL001" in operations.books, "Test 1 Failed: Book not added to Freetown Library!"

# Test 2: Borrow when no copies left fails
operations.add_book("SL002", "Sierra Leone History", "Saidu Conteh", "Non-Fiction", 0)
assert operations.borrow_book("SL002", 1) == "No copies left at the market!", "Test 2 Failed: Should not allow borrowing!"

# Test 3: Add a member successfully
operations.add_member(1, "Fatima Bangura", "fatima@freetown.sl")
assert any(m['member_id'] == 1 for m in operations.members), "Test 3 Failed: Member not added to community!"

# Test 4: Borrow with 3-book limit fails
operations.add_book("SL003", "Krio Sci-Fi", "Jalloh Bah", "Sci-Fi", 4)
operations.add_member(2, "Ibrahim Sesay", "ibrahim@slmarket.sl")
operations.borrow_book("SL003", 2)
operations.borrow_book("SL003", 2)
operations.borrow_book("SL003", 2)
assert operations.borrow_book("SL003", 2) == "Member has reached the borrowing limit (3 books) from Freetown!", "Test 4 Failed: Should respect 3-book limit!"

# Test 5: Return a book updates copies
operations.borrow_book("SL001", 1)
operations.return_book("SL001", 1)
assert operations.books["SL001"]["total_copies"] == 3, "Test 5 Failed: Copy count not updated after return!"