"""Learning regular expressions with Python
Comparing code with and without the use of RE
"""

import re


def isphonenumber(text):
    """Verify if string is the correct phone number format
    e.g 415-555-0000
    Without using regular expression
    """
    if len(text) != 12:
        return False  # incorrect size
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # no area code
    if text[3] != '-':
        return False  # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # no first 3 digits
    if text[7] != '-':
        return False  # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # missing last 4 digits
    return True


print('415-555-4242 is a phone number:')
print(isphonenumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isphonenumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
print('Looking for phone number(s) in the following message: \n' + message)
foundNumber = False
for j in range(len(message)):
    chunk = message[j:j + 12]
    if isphonenumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True

if not foundNumber:
    print('Could not find any phone numbers.')
print('Done')

""" Matching phone number using regular expression
\d stands for digit character
r before the string to mark it as raw string and avoid using double backslashes
this{x} match this x number of times
1. import regex module re
2. create regex object re.compile()
3. pass string to search with search() method returns a match object
4. call match object group() method returns a string of the matched text
"""

# regular expression object
# phoneNumRegex = re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

# match object
# .search() finds the first occurence
mo = phoneNumRegex.search(message)
print(mo.group())

# .findall() returns a list of strings of all matches
print(phoneNumRegex.findall(message))

# use () to separate groups
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search(message)
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
