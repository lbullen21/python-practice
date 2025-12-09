# Python Practice Repository 🐍

A repository for practicing Python fundamentals with hands-on exercises and tests.

## Setup

### 1. Create a Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Practice Files

### Running the Main Practice File
```bash
# Run the fundamentals practice file
python src/fundamentals.py
```

This will run through all the fundamental concepts with examples and output.

### Running Tests
```bash
# Run all tests
pytest tests/

# Run tests with verbose output
pytest tests/ -v

# Run tests with coverage report
pytest tests/ --cov=src

# Run a specific test file
pytest tests/test_fundamentals.py
```

## What's Included

### `src/fundamentals.py`
- **Variables and Data Types**: integers, floats, strings, booleans, lists, dictionaries
- **String Operations**: string methods, slicing, formatting
- **Lists and Loops**: for loops, while loops, list comprehensions, enumerate
- **Conditionals**: if/elif/else statements, comparison operators
- **Functions**: function definition, parameters, return values, default parameters
- **Dictionaries**: creation, access, modification, iteration

### `tests/test_fundamentals.py`
- Unit tests for basic concepts
- Practice exercises with TODO implementations:
  - FizzBuzz algorithm
  - Vowel counting
  - Word reversal
  - Finding common elements between lists

## How to Practice

1. **Start with the basics**: Run `python src/fundamentals.py` to see examples
2. **Experiment**: Modify the code in `fundamentals.py` to try different values
3. **Test your understanding**: Run `pytest tests/` to see if tests pass
4. **Solve exercises**: Implement the TODO functions in `test_fundamentals.py`
5. **Create your own**: Add new functions and tests

## Practice Exercises

The `tests/test_fundamentals.py` file includes several practice exercises:

1. **FizzBuzz**: Classic programming problem
2. **Count Vowels**: String manipulation practice
3. **Reverse Words**: Working with strings and lists
4. **Find Common Elements**: List operations and set theory

To work on these:
1. Open `tests/test_fundamentals.py`
2. Find the `PracticeExercises` class
3. Implement the functions marked with `# TODO`
4. Uncomment the corresponding tests at the bottom
5. Run `pytest tests/test_fundamentals.py` to check your solutions

## Tips for Learning

- **Run code frequently**: Don't just read, execute the code to see results
- **Make changes**: Modify variables and see how output changes
- **Break things**: Try invalid inputs to understand error messages
- **Add print statements**: Use `print()` to debug and understand flow
- **Test incrementally**: Write small pieces of code and test them

## Next Steps

Once comfortable with fundamentals, consider exploring:
- Object-Oriented Programming (classes, inheritance)
- File I/O operations
- Working with APIs using `requests`
- Data analysis with `pandas` and `numpy`
- Web development with Flask or Django

## Project Structure
```
python-practice/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── src/                  # Source code
│   └── fundamentals.py   # Main practice file
└── tests/               # Test files
    └── test_fundamentals.py  # Tests and exercises
```

Happy coding! 🚀