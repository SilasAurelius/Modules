"""
Task 1: Custom Module with Aliases 
Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.
"""
import text_utils as tu

s = "i am excited that the ORIGINAL MCGYVER show is on Prime."

reversed_text = tu.reverse_string(s)
capitalized_text = tu.capitalize_string(s)

print(f"Original text: {s}\n")
print(f"Reversed text: {reversed_text}\n")
print(f"Capitalized text: {capitalized_text}\n")
