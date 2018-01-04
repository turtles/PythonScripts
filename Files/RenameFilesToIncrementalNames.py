# Rename all files in a folder with a matching extension to an incremental name
# Ex. a folder with these files: turtle.png, lizard.png, crocodile.png, cat.jpg
#     will change to: reptile1.png, reptile2.png, reptile3.png, cat.jpg
#     provided you set prefix to "reptile" and extension to "png"

import glob
import os
from os.path import basename

dir = input("Directory: ")
extension = input("Extension to match: ")
prefix = input("New filename prefix: ")

# Scrub input
extension = extension.replace('.', '')
if not extension.isalnum():
    print("file extension must be alphanumeric")
    exit(1)

if dir[len(dir)-1] != "\\":
    dir += "\\"

# Get files using the glob module
# Create a separate directory variable for glob
# so we can reuse the original later
globdir = dir + "*." + extension
files = glob.glob(globdir)

# Preview file changes
print("These changes will be made: ")

increment = 1
for file in files:
    print("{} -> {}{}.{}".format(basename(file.title()),
                                 prefix, increment, extension))
    increment += 1

confirm = input("Type rename to confirm: ")
if confirm != "rename":
    print("Cancelled")
    exit(0)

# Rename files
increment = 1
for file in files:
    new_filename = "{}{}.{}".format(prefix, increment, extension)
    os.rename(file, "{}{}".format(dir, new_filename))
    increment += 1

print("Done!")

'''
Example output

Directory: C:\Python\imgs
Extension to match: .jpg
New filename prefix: kitty
These changes will be made:
Cat.Jpg -> kitty1.jpg
Cat2.Jpg -> kitty2.jpg
Type rename to confirm: rename
Done!

Process finished with exit code 0
'''
