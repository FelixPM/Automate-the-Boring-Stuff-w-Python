"""Using python to create, read, and save files
"""

import os

# current working directory
print('Current working directory: ')
print(os.getcwd())

# change directory
print('\nChange directory to \\test')
os.chdir('.\\test')
print('Current working directory: ')
print(os.getcwd())
os.chdir('..\\')

# Absolute and Relative paths
# Absolute paths always start with root folder, complete path
# Relative paths to program current working directory
absolute_path = r'D:\Documents\PycharmProjects\Automate-the-Boring-Stuff-w-Python'
relative_path = r'.\Automate-the-Boring-Stuff-w-Python'

# Relative to absolute path
print('\nAbsolute path to "test"')
print(os.path.abspath('test'))
print('Absolute path to "..\\test"')
print(os.path.abspath('..\\test'))

# Absolute path check
print('\nAbsolute path check: ')
print(os.path.isabs(absolute_path))
print(os.path.isabs(relative_path))

# Relative path from certain path (path, start) default start cwd
print('\nRelative path from {} to D:\\'.format(absolute_path))
print(os.path.relpath(absolute_path, 'D:\\'))

# Using path join and getting dir and base name
testpath = os.path.join(absolute_path, 'test', 'test_file.txt')
print('\nPath dir and base: ')
print(testpath)
print(os.path.dirname(testpath))
print(os.path.basename(testpath))
print(os.path.split(testpath))

# Check existence
calcpath = 'C:\\Windows\\System32\\calc.exe'
print('\nCheck path and file existence: ')
print(os.path.exists(calcpath))
print(os.path.isfile(calcpath))
print(os.path.isfile(relative_path))

# size
print('\nGetting size: ')
print(os.path.getsize(calcpath))

# listing
print('\nList contents of path')
print(os.listdir(absolute_path))

totalSize = 0
for filename in os.listdir(os.getcwd()):
    filename = os.path.join(absolute_path, filename)
    if not os.path.isfile(filename):
        continue
    totalSize += os.path.getsize(filename)
print('\nTotal size of contents: ', totalSize)

# make directory
os.makedirs('.\\test\\makefolder')
