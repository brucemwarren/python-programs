# Exercises for chapter 10 - Tuples, PY4E

# Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the
# line. Count the number of messages from each person using a dictionary.
#
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples
# from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

# d = dict() # Create dictionary
# fhand = open('mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     if len(words) < 3 or words[0] != 'From': continue
#     if words[1] in words:
#         d[words[1]] = d.get(words[1], 0) + 1
#
# tmp = list() # Create list to sort tuples.
# for email, count in d.items():
#     tmp.append((count, email)) # Add each reversed tuple to list
#     tmp.sort(reverse= True) # Sort list
# for count, email in tmp[:1]: # Print out the top item
#     print(email, count)

# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the
# hour from the "From" line by finding the time string and then splitting that string into parts using the colon c
# haracter. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour
# as shown below.

# Set up our dictionary and lists

# d = dict()
# hours = list()
# tmp = list()
#
# fhand = open('mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     if len(words) < 3 or words[0] != 'From': continue
#     # Take the time position, split the string at the ':' and append the hour to the hours list.
#     if words[5] in words:
#         times = (words[5].split(":"))
#         hours.append(times[0])
#
# # Add items to the dictionary
# for hour in hours:
#     d[hour] = d.get(hour, 0) + 1
# # Create list of tuples with hour and count
# tmp = list(d.items())
# tmp.sort()
# # Print out the tuples
# for k, v in tmp:
#     print(k, v)

# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program
# should convert all the input to lower case and only count the letters a-z. Your program should not count spaces,
# digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and
# see how letter frequency varies between languages. Compare your results with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.

import string
d = dict()
tmp = list()
# Input and read the file
fname = input('Please enter your file name, for the magical magics of the magic: ')
if len(fname) < 1: fname = 'words.txt'
try:
    fhand = open(fname)
except:
    print("Can't open that one, sorry.")
    exit()

# Take out punctuation, whitespace, and lowercase
for line in fhand:
    line = line.rstrip()
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.translate(str.maketrans('','',string.whitespace))
    line = line.translate(str.maketrans('','','0123456789'))
    line = line.lower()
    # print(line)

# Iterate over each letter and add to dictionary or add to count
    for letter in line:
        d[letter] = d.get(letter, 0) + 1
# print(d)

# Create tuples for list of letters and their counts
for ltr, count in d.items():
    tmp.append((count, ltr))
    tmp.sort(reverse=True)
for k, v in tmp:
    print(k, v)