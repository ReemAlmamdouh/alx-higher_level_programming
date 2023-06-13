#!/usr/bin/python3
"""Function that reads a file"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""


    with open(filename, encoding="utf-8") as f:
        contents = f.read()
        print(contents)
