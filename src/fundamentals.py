"""
Python Fundamentals Practice
Practice file covering basic Python concepts with exercises and examples.
"""

def variables_and_data_types():
    """Practice with variables and basic data types"""
    print("=== Variables and Data Types ===")
    
    # Integer
    age = 25
    print(f"Age: {age}, Type: {type(age)}")
    
    # Float
    height = 5.9
    print(f"Height: {height}, Type: {type(height)}")
    
    # String
    name = "Python Learner"
    print(f"Name: {name}, Type: {type(name)}")
    
    # Boolean
    is_learning = True
    print(f"Is learning: {is_learning}, Type: {type(is_learning)}")
    
    # List
    favorite_colors = ["blue", "green", "red"]
    print(f"Colors: {favorite_colors}, Type: {type(favorite_colors)}")
    
    # Dictionary
    person = {"name": "Alice", "age": 30, "city": "New York"}
    print(f"Person: {person}, Type: {type(person)}")
    
    print()

def string_operations():
    """Practice with string operations"""
    print("=== String Operations ===")
    
    text = "Python Programming"
    
    # String methods
    print(f"Original: {text}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Length: {len(text)}")
    print(f"Replace: {text.replace('Python', 'Amazing Python')}")
    print(f"Split: {text.split()}")
    
    # String slicing
    print(f"First 6 chars: {text[:6]}")
    print(f"Last 11 chars: {text[7:]}")
    print(f"Middle: {text[3:10]}")
    
    print()

def lists_and_loops():
    """Practice with lists and different types of loops"""
    print("=== Lists and Loops ===")
    
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    
    # For loop with list
    print("Fruits using for loop:")
    for fruit in fruits:
        print(f"  - {fruit.capitalize()}")
    
    # For loop with index
    print("\nFruits with index:")
    for i, fruit in enumerate(fruits):
        print(f"  {i}: {fruit}")
    
    # List comprehension
    long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
    print(f"\nLong fruits: {long_fruits}")
    
    # While loop
    print("\nCountdown:")
    count = 5
    while count > 0:
        print(f"  {count}")
        count -= 1
    print("  Done!")
    
    print()

def conditionals():
    """Practice with if/elif/else statements"""
    print("=== Conditionals ===")
    
    numbers = [15, 8, 23, 4, 42, 16]
    
    for num in numbers:
        if num > 20:
            category = "large"
        elif num > 10:
            category = "medium"
        else:
            category = "small"
        
        # Check if even or odd
        parity = "even" if num % 2 == 0 else "odd"
        
        print(f"  {num} is {category} and {parity}")
    
    print()

def functions_practice():
    """Practice with functions"""
    print("=== Functions ===")
    
    def greet(name, greeting="Hello"):
        """Function with default parameter"""
        return f"{greeting}, {name}!"
    
    def calculate_area(length, width):
        """Function that returns a value"""
        return length * width
    
    def process_numbers(*numbers):
        """Function with variable arguments"""
        total = sum(numbers)
        average = total / len(numbers) if numbers else 0
        return {"total": total, "average": average, "count": len(numbers)}
    
    # Test functions
    print(greet("Alice"))
    print(greet("Bob", "Hi"))
    
    area = calculate_area(5, 3)
    print(f"Area of 5x3 rectangle: {area}")
    
    result = process_numbers(10, 20, 30, 40, 50)
    print(f"Numbers analysis: {result}")
    
    print()

def dictionary_practice():
    """Practice with dictionaries"""
    print("=== Dictionaries ===")
    
    # Create and manipulate dictionaries
    student = {
        "name": "John Doe",
        "age": 20,
        "grades": [85, 92, 78, 96],
        "major": "Computer Science"
    }
    
    # Access and modify dictionary
    print(f"Student: {student['name']}")
    print(f"Age: {student.get('age', 'Unknown')}")
    
    # Calculate average grade
    average_grade = sum(student["grades"]) / len(student["grades"])
    student["average_grade"] = round(average_grade, 2)
    
    # Add new key
    student["year"] = "Sophomore"
    
    # Iterate through dictionary
    print("\nStudent Information:")
    for key, value in student.items():
        print(f"  {key.title()}: {value}")
    
    print()

def main():
    """Main function to run all practice exercises"""
    print("🐍 Python Fundamentals Practice Session")
    print("=" * 50)
    
    variables_and_data_types()
    string_operations()
    lists_and_loops()
    conditionals()
    functions_practice()
    dictionary_practice()
    
    print("🎉 Practice session complete!")
    print("Try modifying the code above to experiment with different values!")

if __name__ == "__main__":
    main()