"""
Additional Python Practice Exercises
More advanced concepts to practice once you're comfortable with fundamentals.
"""

def advanced_list_operations():
    """Practice with advanced list operations"""
    print("=== Advanced List Operations ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # List slicing
    print(f"Original: {numbers}")
    print(f"First half: {numbers[:5]}")
    print(f"Second half: {numbers[5:]}")
    print(f"Every second element: {numbers[::2]}")
    print(f"Reversed: {numbers[::-1]}")
    
    # List comprehensions
    squares = [x**2 for x in numbers]
    print(f"Squares: {squares}")
    
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # Nested list comprehensions
    matrix = [[i+j for j in range(3)] for i in range(3)]
    print(f"Matrix: {matrix}")
    
    print()

def file_operations_practice():
    """Practice with file I/O operations"""
    print("=== File Operations ===")
    
    # Create a sample file
    sample_data = [
        "Alice,25,Engineer",
        "Bob,30,Designer", 
        "Charlie,22,Student",
        "Diana,28,Teacher"
    ]
    
    filename = "sample_data.txt"
    
    # Write to file
    try:
        with open(filename, 'w') as file:
            for line in sample_data:
                file.write(line + '\n')
        print(f"Created file: {filename}")
        
        # Read from file
        with open(filename, 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
        
        # Read line by line and process
        people = []
        with open(filename, 'r') as file:
            for line in file:
                name, age, job = line.strip().split(',')
                people.append({
                    'name': name,
                    'age': int(age),
                    'job': job
                })
        
        print("Processed data:")
        for person in people:
            print(f"  {person['name']}: {person['age']} years old, {person['job']}")
            
    except Exception as e:
        print(f"Error working with file: {e}")
    
    # Clean up
    import os
    try:
        os.remove(filename)
        print(f"Cleaned up: {filename}")
    except:
        pass
    
    print()

def error_handling_practice():
    """Practice with try/except error handling"""
    print("=== Error Handling ===")
    
    def safe_division(a, b):
        """Safely divide two numbers with error handling"""
        try:
            result = a / b
            return f"{a} / {b} = {result}"
        except ZeroDivisionError:
            return f"Error: Cannot divide {a} by zero!"
        except TypeError:
            return f"Error: Invalid types - need numbers, got {type(a)} and {type(b)}"
    
    def safe_list_access(lst, index):
        """Safely access list element with error handling"""
        try:
            return lst[index]
        except IndexError:
            return f"Error: Index {index} out of range for list of length {len(lst)}"
        except TypeError:
            return f"Error: Invalid index type {type(index)}"
    
    # Test error handling
    print(safe_division(10, 2))
    print(safe_division(10, 0))
    print(safe_division("10", 2))
    
    numbers = [1, 2, 3, 4, 5]
    print(safe_list_access(numbers, 2))
    print(safe_list_access(numbers, 10))
    print(safe_list_access(numbers, "invalid"))
    
    print()

def class_practice():
    """Practice with basic object-oriented programming"""
    print("=== Classes and Objects ===")
    
    class Book:
        """A simple Book class"""
        
        def __init__(self, title, author, pages):
            self.title = title
            self.author = author
            self.pages = pages
            self.is_read = False
        
        def mark_as_read(self):
            self.is_read = True
            return f"Marked '{self.title}' as read!"
        
        def get_info(self):
            status = "Read" if self.is_read else "Unread"
            return f"'{self.title}' by {self.author} ({self.pages} pages) - {status}"
        
        def __str__(self):
            return f"Book: {self.title} by {self.author}"
    
    class Library:
        """A simple Library class to manage books"""
        
        def __init__(self):
            self.books = []
        
        def add_book(self, book):
            self.books.append(book)
            return f"Added {book.title} to library"
        
        def get_unread_books(self):
            return [book for book in self.books if not book.is_read]
        
        def get_stats(self):
            total = len(self.books)
            read = sum(1 for book in self.books if book.is_read)
            unread = total - read
            return f"Library: {total} books ({read} read, {unread} unread)"
    
    # Create and use objects
    book1 = Book("1984", "George Orwell", 328)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 376)
    book3 = Book("The Python Crash Course", "Eric Matthes", 544)
    
    library = Library()
    
    print(library.add_book(book1))
    print(library.add_book(book2))
    print(library.add_book(book3))
    
    print(f"\n{library.get_stats()}")
    
    print(f"\nBook info:")
    for book in library.books:
        print(f"  {book.get_info()}")
    
    print(f"\n{book1.mark_as_read()}")
    print(f"{book3.mark_as_read()}")
    
    print(f"\n{library.get_stats()}")
    
    unread = library.get_unread_books()
    print(f"\nUnread books:")
    for book in unread:
        print(f"  {book}")
    
    print()

def lambda_and_functional():
    """Practice with lambda functions and functional programming concepts"""
    print("=== Lambda and Functional Programming ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Lambda functions
    square = lambda x: x ** 2
    print(f"Square of 5: {square(5)}")
    
    # Using map()
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(f"Squared numbers: {squared_numbers}")
    
    # Using filter()
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {even_numbers}")
    
    # Using reduce()
    from functools import reduce
    sum_all = reduce(lambda x, y: x + y, numbers)
    print(f"Sum of all numbers: {sum_all}")
    
    # Combining functional operations
    result = reduce(
        lambda x, y: x + y,
        map(lambda x: x ** 2,
            filter(lambda x: x % 2 == 0, numbers))
    )
    print(f"Sum of squares of even numbers: {result}")
    
    # Practical example: processing data
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92},
        {"name": "Charlie", "grade": 78},
        {"name": "Diana", "grade": 96},
        {"name": "Eve", "grade": 81}
    ]
    
    # Find students with grades above 80
    good_students = list(filter(lambda s: s["grade"] >= 80, students))
    print(f"\nStudents with grade >= 80:")
    for student in good_students:
        print(f"  {student['name']}: {student['grade']}")
    
    # Get just the names of top students (grade >= 90)
    top_student_names = list(map(
        lambda s: s["name"],
        filter(lambda s: s["grade"] >= 90, students)
    ))
    print(f"Top students (grade >= 90): {top_student_names}")
    
    print()

def main():
    """Run all practice exercises"""
    print("🚀 Advanced Python Practice Session")
    print("=" * 50)
    
    advanced_list_operations()
    file_operations_practice()
    error_handling_practice()
    class_practice()
    lambda_and_functional()
    
    print("🎯 Advanced practice session complete!")
    print("Next steps: Try web scraping, APIs, or data analysis!")

if __name__ == "__main__":
    main()