#!/usr/bin/env python3
"""
Utility functions for the project
"""

def helper():
    """Helper function that returns a string"""
    return "This is helper function"

def format_output(text):
    """Format text with borders"""
    border = "=" * (len(text) + 4)
    return f"{border}\n| {text} |\n{border}"

def validate_number(value):
    """Check if value is a number"""
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_timestamp():
    """Get current timestamp as string"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    print(helper())
    print(format_output("Testing utils"))
