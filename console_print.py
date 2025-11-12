#!/usr/bin/env python3
"""
Simple Python file for console printing examples.
"""

# Part 1: Direct code execution (no function)
print("=== Part 1: Direct Execution ===")
print("Hello from Python!")
message = "This is a simple print statement"
print(message)
print(f"2 + 2 = {2 + 2}")
print()

# Part 2: Function definition and call
print("=== Part 2: Function Call ===")


def greet(name):
    """Function that prints a greeting message."""
    print(f"Hello, {name}!")
    print(f"Welcome to Python programming.")


def calculate_sum(a, b):
    """Function that calculates and prints the sum of two numbers."""
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    return result


# Calling the functions
greet("World")
calculate_sum(10, 20)
