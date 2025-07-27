from relationship_app.models import Author, Book, Library, Librarian

def get_books_in_library(library_name):
    """List all books in a library - this is the function you're missing"""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return Book.objects.none()

def create_sample_data():
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
    # Create sample data first
    create_sample_data()
    
    # Test the books in library query
    print("\nBooks in Central Library:")
    books = get_books_in_library("Central Library")
    for book in books:
        print(f"- {book.title}")

if __name__ == "__main__":
    import django
    django.setup()
    demonstrate_queries()  # Changed from create_sample_data() to demonstrate_queries()