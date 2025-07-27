from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return Book.objects.none()

def get_books_in_library(library_name):
    """List all books in a library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return Book.objects.none()

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library using the exact required pattern"""
    try:
        return Librarian.objects.get(library__name=library_name)  # Exact pattern required
    except Librarian.DoesNotExist:
        return None

def create_sample_data():
    """Create sample data for testing"""
    # Clear existing data
    Author.objects.all().delete()
    
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    
    # Create books
    book1 = Book.objects.create(title="Harry Potter 1", author=author1)
    book2 = Book.objects.create(title="Harry Potter 2", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    
    # Create libraries
    lib1 = Library.objects.create(name="Central Library")
    lib2 = Library.objects.create(name="Community Library")
    
    # Add books to libraries
    lib1.books.add(book1, book2, book3)
    lib2.books.add(book1, book3)
    
    # Create librarians
    Librarian.objects.create(name="Ms. Smith", library=lib1)
    Librarian.objects.create(name="Mr. Johnson", library=lib2)
    
    print("Sample data created!")

def demonstrate_queries():
    """Demonstrate all query functions"""
    create_sample_data()
    
    # Test book by author query
    print("\nBooks by J.K. Rowling:")
    for book in get_books_by_author("J.K. Rowling"):
        print(f"- {book.title}")
    
    # Test books in library query
    print("\nBooks in Central Library:")
    for book in get_books_in_library("Central Library"):
        print(f"- {book.title}")
    
    # Test librarian query (using the exact required pattern)
    print("\nLibrarian for Central Library (using exact pattern):")
    try:
        librarian = Librarian.objects.get(library__name="Central Library")
        print(librarian.name)
    except Librarian.DoesNotExist:
        print("No librarian found")

if __name__ == "__main__":
    import django
    django.setup()
    demonstrate_queries()