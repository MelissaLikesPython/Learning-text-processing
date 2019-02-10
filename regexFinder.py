#! /usr/bin/env python3

# This program searches all plain text files in a folder for a user-inputted regex.
# Note: Choose UTF-8 as your encoding when converting word processing files to plain text. 

import os, re

# Prompts user to input regex. 
userRegex = re.compile(input('Enter your chosen regex:\n'), re.I)

# Prompts user to input file path.        
path = input('Please enter your chosen folder with file path:\n') 

# Checks that file path is valid.
while True:
    if os.path.exists(path) == True:
        break
    else:    
        print('Sorry, I can\'t find this file path.')

# Opens and reads all files in folder with .txt extension.
# Finds and prints all instances of user's regex. 
fileList = os.listdir(path)
for file in fileList:
    if file.endswith('.txt'):
        print(os.path.join(path, file))
        content = open(os.path.join(path, file), 'r+')
        text = content.read()       
        result = userRegex.findall(text)
        print(result)
        
        
    