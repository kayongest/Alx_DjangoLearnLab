from relationship_app.models import Author, Book, Library, Librarian

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

if __name__ == "__main__":
    import django
    django.setup()
    create_sample_data()