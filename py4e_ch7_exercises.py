# The exercises for Chapter 7 (8 in the ebook) for PY4E course on files.
#
#
# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case.

# fhand = open(input('Please enter a file name: '))
#
# for line in fhand:
#     line = line.rstrip()
#     print(line.upper())

# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
#
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point
# number on the line. Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.
#
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
#
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# Test your file on the mbox.txt and mbox-short.txt files.

# fname = input('Please enter a file name: ') #Prompt for file
# count = 0
# spam_con = 0
# try: # Check if file is valid
#     fhand = open(fname)
# except:
#     print('Sorry, could not open file: ', fname)
#     exit()
#
# for line in fhand:
#     line = line.rstrip()
#     if 'X-DSPAM-Confidence: ' in line: # Search for text, count lines with text
#         spam_con += float(line[20:])
#         count += 1
# print('Average spam confidence: ', (spam_con/count))

# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to
# their program Modify the program that prompts the user for the file name so that it prints a funny message when the
# user types in the exact file name "na na boo boo". The program should behave normally for all other files which exist
# and don't exist.

count = 0
fname = input('Please enter the file name: ')
if fname == 'na na boo boo':
    print('BOOGITY BOOGITY BOOGITY BOO BOO!!')
    exit()
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    if 'Subject: ' in line:
        count += 1

print('There were ', count, ' subject lines in ', fname)