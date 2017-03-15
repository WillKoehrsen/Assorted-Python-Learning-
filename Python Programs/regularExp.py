'''
IDENTIFIERS (looking for this type)
\ :escape character (in regular expressions, start an expression)
\d any number
\D anything but a number
\s space
\S anything but a character
\w any character
\W anything but a character
.  any character except for a new line
\b whitespace around words
\. period

MODIFIERS (qualifier description of type)
{1, 3} expecting 1-3 of type
\d{1-3} looking for digits 1-3 in length
+ match 1 or more
? match 0 or 1 
* match 0 or more
$ match end of string
^ match beginning of string
| either or 
\d{1-3} | \w{5-6} looking for digit 1-3 in length or character 5-6 in length
[] range or "variance" [A-Za-z] [1-5a-tA-Z]
{x} expecting "x" amount

White Space Characters (might not necessarily see)
\n newline
\t tab
\s space
\f form feed
\e escape
\r return (carriage)

THESE ONES
. + * ? [ } $ ^ ( ) { } | \ 

'''
import re

exampleString = '''
I do not know what this sentence is about but it needs some digits.
Therefore, Todd has 50 keys, Alice has 96 buttons, and Tom is 76 cm from the wall.
'''

digits = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]{2,5}\s', exampleString) #any capital letter, followed by any lowercase letter, followed by any character

print(digits, names)

digitsDict = {}
x = 0
for eachName in names:
	digitsDict[eachName] = digits[x]
	x += 1

print(digitsDict)

