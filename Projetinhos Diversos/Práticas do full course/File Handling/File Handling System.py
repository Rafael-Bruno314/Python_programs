# Python supports two types of file:
# Binary and text

# Key function: open(filename.ext, mode)

# Mode can be:
# r - Read: Default value. Opens a file for reading, error if file doesn't exist
# a - Append: Opens a file for appending, creates the file if doesn't exist
# w - Write: Opens a file for writing, creates the file if doesn't exist
# x - Create: Creates the specified file, return an error if the file exists

# In addition to mode (place together in the function)
# t - Text: Default value. Text Mode
# b - Binary: Binary Mode (e.g. images)

"""
Additionally, here are the other options:

"r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing. The file is created if it does not exist.
"a+"  Open for reading and writing.  The file is created if it does not exist.
"""