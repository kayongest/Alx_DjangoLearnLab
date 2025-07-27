from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books by a specific author - using the exact required pattern"""
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)  # Using the exact required pattern
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
    """Retrieve the librarian for a library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

def create_sample_data():
    """Create sample data for testing"""
    # Clear existing data
    Author.objects.all().delete()
    
    # Create sample data
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    
    book1 = Book.objects.create(title="Harry Potter 1", author=author1)
    book2 = Book.objects.create(title="Harry Potter 2", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    
    lib1 = Library.objects.create(name="Central Library")
    lib1.books.add(book1, book2, book3)
    
    Librarian.objects.create(name="Ms. Smith", library=lib1)
    
    print("Sample data created!")

def demonstrate_queries():
    """Demonstrate all query functions"""
    create_sample_data()
    
    print("\nBooks by J.K. Rowling:")
    books = get_books_by_author("J.K. Rowling")
    for book in books:
        print(f"- {book.title}")
    
    print("\nBooks in Central Library:")
    books = get_books_in_library("Central Library")
    for book in books:
        print(f"- {book.title}")
    
    print("\nLibrarian for Central Library:")
    librarian = get_librarian_for_library("Central Library")
    print(librarian.name if librarian else "No librarian found")

if __name__ == "__main__":
    import django
    django.setup()
    demonstrate_queries()