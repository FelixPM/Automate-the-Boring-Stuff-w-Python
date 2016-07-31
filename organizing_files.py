"""Using python to move, copy, rename and delte files
"""

import shutil
import os

print('Current working directory: ')
print(os.getcwd())

# create copy folder
if not os.path.exists('.\\testcopy'):
    os.makedirs('.\\testcopy')

# copy file
if os.path.exists('test\\test_file.txt'):
    shutil.copy('test\\test_file.txt', 'testcopy\\test_file_copy.txt')

# copy directory
if not os.path.exists('.\\testbackup'):
    shutil.copytree('test', 'testbackup')

# move folder
if os.path.exists('test\\zen.txt'):
    shutil.move('test\\zen.txt', 'testcopy')

# rename by move to same folder with different name
if os.path.exists('test\\test_file.txt'):
    shutil.move('test\\test_file.txt', 'test\\test_file1.txt')
else:
    shutil.move('test\\test_file1.txt', 'test\\test_file.txt')

# delete single file
# os.unlink('testcopy\\test_file_copy.txt')

# delete empty folder
if not os.path.exists('test\\makefolder'):
    os.makedirs('test\\makefolder')
else:
    os.rmdir('test\\makefolder')

# delete folder and contents
# if os.path.exists('.\\testbackup'):
#     shutil.rmtree('.\\testbackup')
