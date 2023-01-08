# Docstrings

def countSetBits(number):
    '''Takes a number as input and returns the number of set-bits in its binary representation'''
    setBits = 0
    while (number):
        setBits += 1
        number &= number - 1
    return setBits


queryNumber = input("Enter the number to counts its set bits: ")
if (not queryNumber.isnumeric()):
    exit("Please enter the input a 'Number'")

queryNumber = int(queryNumber)
print(f"The number of set bits in {queryNumber} = {countSetBits(queryNumber)}")
print(countSetBits.__doc__)


# PEP 8 (Python Enhancement Proposal)
# It provides a guidline and best practice on how to write python code
# It's main aim is to improve the readability and consistency of python code

# import this
# This prints 'The Zen of Python'
"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""
