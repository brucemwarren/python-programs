# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
#
# Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what the
# values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

# fhand = open('words.txt') #Open file
# wordsDict = {} # Initialize dictionary
#
# # Go through each line of the file, split the words, add each word to the dictionary.
# for line in fhand:
#     words = line.split()
#     for word in words:
#         wordsDict[word] = ''
#
# print(wordsDict)
#
# print('cow' in wordsDict)
# print('write' in wordsDict)

# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do
# this look for lines that start with "From", then look for the third word and keep a running count of each of the days
# of the week. At the end of the program print out the contents of your dictionary (order does not matter).

# First step: take the previous code and use this to find the day of the week, with adding new dictionary

# d = dict() # Create dictionary
# fhand = open('mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     if len(words) < 3 or words[0] != 'From': continue
#     if words[2] in d:
#         d[words[2]] += 1
#     else:
#         d[words[2]] = 1
# print(d)
# Successful output - {'Sat': 1, 'Fri': 20, 'Thu': 6}

# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many
# messages have come from each email address, and print the dictionary.

# Similar to above, but we need to pull the email address out of the words list instead of the day.
# The position for this is words[1], following the same code as above.

# d = dict() # Create dictionary
# fhand = open('mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     if len(words) < 3 or words[0] != 'From': continue
#     if words[1] in d:
#         d[words[1]] += 1
#     else:
#         d[words[1]] = 1
# print(d)

# Successful output confirmed. Basically, the same code as before, looking at a different list position.

# Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data
# has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5:
# Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

# Part 3 of the videos gives us help with this. We need a second loop using the items() function to find the max
# and the min. I'm just doing a min for fun. It's not accurate as it will only capture the first person to have 1.


# d = dict() # Create dictionary
# fhand = open('mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     if len(words) < 3 or words[0] != 'From': continue
#     if words[1] in d:
#         d[words[1]] += 1
#     else:
#         d[words[1]] = 1
# # print(d)
#
# #Initialize some variables
# bigEmail = None
# bigCount = None
# smallEmail = None
# smallCount = None
#
# # Iterate through the dictionary comparing the totals.
#
# for email, counts in d.items():
#     if bigCount is None or counts > bigCount:
#         bigCount = counts
#         bigEmail = email
#     if smallCount is None or counts < smallCount:
#         smallCount = counts
#         smallEmail = email
#
# print('Most sent by', bigEmail, 'who sent', bigCount, '.')
# print('Least sent by', smallEmail, 'who sent', smallCount,'.')

# Successful output.

# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of
# who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your
# dictionary.

d = dict() # Create dictionary
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From': continue
    domain = words[1].split('@') # Adding a new list of the split email addresses
    if domain[1] in d:
        d[domain[1]] += 1
    else:
        d[domain[1]] = 1
print(d)