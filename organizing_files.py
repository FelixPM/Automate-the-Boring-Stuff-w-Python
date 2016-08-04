"""Using python to move, copy, rename and delte files
"""

import shutil
import os
import send2trash
import zipfile

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

# Delete folder and contents
# if os.path.exists('.\\testbackup'):
#     shutil.rmtree('.\\testbackup')

# send to trash instead of permanent delete
# send2trash.send2trash('testcopy\\test_file_copy.txt')

# Iterate over all folders and subfolders
for foldername, subfolders, filenames in os.walk('.\\'):
    print('Current folder: '+foldername)
    print('Current subfolders: '+str(subfolders))
    print('Current filenames: '+str(filenames))

# Read zipped file
examplezip = zipfile.ZipFile('testcopy\\ender.zip')
print(examplezip.namelist())

# zipped file info
zenInfo = examplezip.getinfo('zen.txt')
print(zenInfo.file_size)
print(zenInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(zenInfo.file_size / zenInfo.compress_size, 2)))

# Extract zip file to cwd or especified path
# exampleZip.extractall()
# exampleZip.extract('name', 'path')
examplezip.close()

# Create zip files
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('ender.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

