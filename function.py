Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='computer'b='this is a python class'
SyntaxError: invalid syntax
>>> a='computer'
>>> b='This is a python class'
>>> a.upper()
'COMPUTER'
>>> b.upper()
'THIS IS A PYTHON CLASS'
>>> a.lower()
'computer'
>>> b.lower()
'this is a python class'
>>> b='this is a python class. This is our 4th class.'
>>> b.capitalize()
'This is a python class. this is our 4th class.'
>>> b.title()
'This Is A Python Class. This Is Our 4Th Class.'
>>> b.count('a')
3
>>> b
'this is a python class. This is our 4th class.'
>>> b.split()
['this', 'is', 'a', 'python', 'class.', 'This', 'is', 'our', '4th', 'class.']
