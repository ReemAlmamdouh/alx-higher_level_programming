#!/usr/bin/python3
"""Function that writes a string to a text file"""

def write_file(filename="", text=""):
    """Writes a string to a text file
    and returns number of charecters 
    written"""

    with open(filename, mode="w", encoding="utf-8") as f:
        n_characters = f.write(text)
        return n_characters
