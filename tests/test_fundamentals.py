"""
Test file for Python fundamentals practice
This file demonstrates how to write and run tests for your practice code.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from fundamentals import *

def test_string_operations():
    """Test some basic string operations"""
    text = "Python Programming"
    assert text.upper() == "PYTHON PROGRAMMING"
    assert text.lower() == "python programming"
    assert len(text) == 18
    assert "Python" in text

def test_list_operations():
    """Test basic list operations"""
    fruits = ["apple", "banana", "cherry"]
    assert len(fruits) == 3
    assert fruits[0] == "apple"
    assert fruits[-1] == "cherry"
    
    # Test list comprehension concept
    long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
    assert "banana" in long_fruits
    assert len(long_fruits) == 2

def test_conditionals():
    """Test conditional logic"""
    def categorize_number(num):
        if num > 20:
            return "large"
        elif num > 10:
            return "medium"
        else:
            return "small"
    
    assert categorize_number(25) == "large"
    assert categorize_number(15) == "medium"
    assert categorize_number(5) == "small"

def test_dictionary_operations():
    """Test dictionary operations"""
    student = {"name": "John", "age": 20, "grades": [85, 90, 78]}
    
    assert student["name"] == "John"
    assert len(student["grades"]) == 3
    
    # Test adding new key
    student["major"] = "CS"
    assert "major" in student
    assert student["major"] == "CS"

def test_function_concepts():
    """Test basic function concepts"""
    def add_numbers(a, b):
        return a + b
    
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    # Test basic function
    assert add_numbers(3, 5) == 8
    
    # Test default parameters
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob", "Hi") == "Hi, Bob!"

# Practice exercises you can solve
class PracticeExercises:
    """
    Practice exercises to test your understanding.
    Uncomment and implement these to practice!
    """
    
    def exercise_1_fizzbuzz(self, n):
        """
        Classic FizzBuzz: Return a list of numbers 1 to n, but:
        - Replace multiples of 3 with "Fizz"
        - Replace multiples of 5 with "Buzz" 
        - Replace multiples of both with "FizzBuzz"
        
        Example: fizzbuzz(15) should return:
        [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
        """
        # TODO: Implement this function
        pass
    
    def exercise_2_count_vowels(self, text):
        """
        Count the number of vowels (a, e, i, o, u) in the given text.
        Should be case-insensitive.
        
        Example: count_vowels("Hello World") should return 3
        """
        # TODO: Implement this function
        pass
    
    def exercise_3_reverse_words(self, sentence):
        """
        Reverse the order of words in a sentence.
        
        Example: reverse_words("Hello World Python") should return "Python World Hello"
        """
        # TODO: Implement this function
        pass
    
    def exercise_4_find_common_elements(self, list1, list2):
        """
        Find common elements between two lists.
        
        Example: find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) should return [3, 4]
        """
        # TODO: Implement this function
        pass

# Uncomment the tests below when you implement the exercises above!

# def test_fizzbuzz():
#     exercises = PracticeExercises()
#     result = exercises.exercise_1_fizzbuzz(15)
#     assert result[0] == 1
#     assert result[2] == "Fizz"  # 3
#     assert result[4] == "Buzz"  # 5
#     assert result[14] == "FizzBuzz"  # 15

# def test_count_vowels():
#     exercises = PracticeExercises()
#     assert exercises.exercise_2_count_vowels("Hello World") == 3
#     assert exercises.exercise_2_count_vowels("Python") == 1
#     assert exercises.exercise_2_count_vowels("AEIOU") == 5

# def test_reverse_words():
#     exercises = PracticeExercises()
#     assert exercises.exercise_3_reverse_words("Hello World") == "World Hello"
#     assert exercises.exercise_3_reverse_words("Python is awesome") == "awesome is Python"

# def test_find_common_elements():
#     exercises = PracticeExercises()
#     result = exercises.exercise_4_find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
#     assert set(result) == {3, 4}