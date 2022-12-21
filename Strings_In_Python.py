# Strings
"""Learning about strings in python
This is a multiline comment"""

print(type(""" This is 'basically' a "string" """))

multiline_string = """This is a multiline string.
My name is neeraj and I am 22 years old (2022)
This is the end of the string"""
print(multiline_string)

print("Iterating through the string")
print(len(multiline_string))
for character in multiline_string:
    print(character, end=" ")
