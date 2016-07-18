"""Learning regular expressions with Python
Comparing code with and without the use of RE
"""

import re


def is_phone_number(text):
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


print('Matching strings without regular expressions')
print('415-555-4242 is a phone number:')
print(is_phone_number('415-555-4242'))
print('Moshi moshi is a phone number:')
print(is_phone_number('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
print('Looking for phone number(s) in the following message: \n' + message)
foundNumber = False
for j in range(len(message)):
    chunk = message[j:j + 12]
    if is_phone_number(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True

if not foundNumber:
    print('Could not find any phone numbers.')

""" Matching phone number using regular expression
\d stands for digit character
r before the string to mark it as raw string and avoid using double backslashes
this{x} match this x number of times
1. import regex module re
2. create regex object re.compile()
3. pass string to search with search() method returns a match object
4. call match object group() method returns a string of the matched text
"""

print('\nMatching strings using Regex')
# regular expression object
# phoneNumRegex = re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

# match object
# .search() finds the first occurrence
mo = phoneNumRegex.search(message)
print('\nSearch method shows first occurrence')
print(mo.group())

# .findall() returns a list of strings of all matches
print('\nFindall method returns a list of all matches')
print(phoneNumRegex.findall(message))

# use () to separate groups
print('\nUsing () to separate groups')
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search(message)

# group(i) i matching string
print(mo.group(1))
print(mo.group(2))

# group(0) full matching string
print(mo.group(0))

# | pipe matching one of several patterns
print('\nUsing | to match one of many')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

# ? optional group
print('\nUsing ? for optional patterns')
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

print('\nUsing | and ? ')
phoneRegex = re.compile(r'(((\d{3}-)|(\(\d{3}\)\s))?(\d{3}-\d{4}))')
mo = phoneRegex.findall('Call me at 415-555-1011 or (415) 555-9999')
print(mo)

# * zero or more
print('\nUsing * to match zero or more')
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The adventures of Batwowowoman')
print(mo.group())

# + one or more
print('\nUsing + to match one or more')
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The adventures of Batwoman')
print(mo.group())

# {} for repetitions
print('\nCurly braces for repetitions matches the longest by default')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

print('\nNon greedy {}? matches shortest')
nonGreedyRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyRegex.search('HaHaHaHaHa')
print(mo2.group())

# character classes
# \d numeric 0-9
# \D any not numeric
# \w letter, digit, underscore "words"
# \W not \w
# \s space, tab, newline
# \S not space

print('\nCharacter classes on 12 days of christmas')
lyrics = ('12 Drummers Drumming, '
          '11 Pipers Piping, '
          '10 Lords a Leaping, '
          '9 Ladies Dancing, '
          '8 Maids a Milking, '
          '7 Swans a Swimming, '
          '6 Geese a Laying, '
          '5 Golden Rings, '
          '4 Calling Birds, '
          '3 French Hens, '
          '2 Turtle Doves, '
          'and 1 Partridge in a Pear Tree')
print(lyrics)
xmasRegex = re.compile(r'\d+\s\w+')
xmas = xmasRegex.findall(lyrics)
print(xmas)

# Personalized classes
print('\nCustom class')
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))

# ^ and $ for starts and ends with
print('\nStarts and ends with using ^and$')
beginsWithHello = re.compile(r'^Hello')
print('Starts with Hello')
print('Hello World!:')
mo = beginsWithHello.search('Hello World!')
print(mo.group())
print('\nHe said hello:')
mo = beginsWithHello.search('He said hello')
print(mo)

endsWithWorld = re.compile(r'World!$')
print('\nEnds with World!')
print('Hello World!:')
mo = endsWithWorld.search('Hello World!')
print(mo.group())
print('\nHe said hello:')
mo = endsWithWorld.search('He said hello')
print(mo)

print('\nWhole string is number')
print('1234567890:')
wholeStringNum = re.compile(r'^\d+$')
mo = wholeStringNum.search('1234567890')
print(mo.group())
print('123x5678:')
mo = wholeStringNum.search('123x5678')
print(mo)

# Wildcard .
print('\nMatching anything with "."')
atRegex = re.compile(r'.at')
print('.at on "The cat in the hat sat on the flat mat."')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# .*
print('\nMatching everything with ".*"')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Felix Last Name: Perez')
print('.* First Name: Felix Last Name: Perez')
print(mo.group(1))
print(mo.group(2))

# greedy and non greedy matching
serve = '<To serve humans> for dinner.>'
print('Greedy and non-greedy matching: ' + serve)
nonGreedy = re.compile(r'<(.*?)>')
print(nonGreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

# Match all including newline
print('\nno newline: ')
prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search(prime)
print(mo.group())

print('\ninclude newline: ')
newLineRegex = re.compile('.*', re.DOTALL)
mo = newLineRegex.search(prime)
print(mo.group())

# case-insensitive re.I
robocop = re.compile(r'robocop', re.I)
mo = robocop.findall('Robocop ROBOCOP')
print(mo)

# find and replace
print('\nFind and Replace')
message = 'Agent Alice gave the secret documents to Agent Bob'
print(message)
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall(message)
print(mo)
message2 = namesRegex.sub('REDACTED', message)
print(message2)

replaceRegex = re.compile(r'Agent (\w)\w*')
mo = replaceRegex.findall(message)
print(mo)
message3 = replaceRegex.sub(r'Agent \1****', message)
print(message3)

# Verbose
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)
mo = phoneRegex.findall('Call me at 415-555-1011 or (415) 555-9999')
print(mo)

# Combining arguments
someRegexValue = re.compile('foo', re.I | re.DOTALL)
