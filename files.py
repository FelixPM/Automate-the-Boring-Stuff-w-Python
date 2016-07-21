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
test_path = os.path.join(absolute_path, 'test', 'test_file.txt')
print('\nPath dir and base: ')
print(test_path)
print(os.path.dirname(test_path))
print(os.path.basename(test_path))
print(os.path.split(test_path))

# Check existence
calc_path = 'C:\\Windows\\System32\\calc.exe'
print('\nCheck path and file existence: ')
print(os.path.exists(calc_path))
print(os.path.isdir(calc_path))
print(os.path.isfile(calc_path))
print(os.path.isdir(absolute_path))
print(os.path.isfile(absolute_path))

# size
print('\nGetting size: ')
print(os.path.getsize(calc_path))

# listing
print('\nList contents of path')
print(os.listdir(absolute_path))

total_size = 0
for filename in os.listdir(os.getcwd()):
    filename = os.path.join(absolute_path, filename)
    if not os.path.isfile(filename):
        continue
    total_size += os.path.getsize(filename)
print('\nTotal size of contents: ', total_size)

# make directory
if not os.path.exists('.\\test\\makefolder'):
    os.makedirs('.\\test\\makefolder')

# Opening files
print('\nOpening file in {}'.format(test_path))
test_file = open(test_path)

# Reading files
test_content = test_file.read()
print('File content: {}'.format(test_content))

zen_file = open('.\\test\\zen.txt')
print(zen_file.readlines())

# Writing to files r=read w=write a=append
ender_file = open('ender.txt', 'w')
ender_file.write('The enemy gate is down\n')
ender_file.close()
ender_file = open('ender.txt', 'a')
ender_file.write('The giant\'s drink')
ender_file.close()
ender_file = open('ender.txt')
content = ender_file.read()
ender_file.close()
print(content)
