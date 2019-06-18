# Exercise 1: Write a function called 'chop' that takes a list and modifies it, removing the first and last elements,
# and returns None. Then write a function called 'middle' that takes a list and returns a new list that contains all
# but the first and last elements.

# def chop(t):
#     del t[0]
#     del t[-1]
#
# def middle(t):
#     mids = t[1:] # Need to save the slice of the original list first, then delete last element
#     del mids[-1]
#     return mids
#
# # Test lists and prints
# list1 = [1, 2, 3, 4]
# list2 = ['Chalkdust', 'Moma', 'Funky Bitch', '46 Days']
#
# print(chop(list1)) # Applies the 'chop' function to list1, modifying it, returning nothing
# print(list1) # Prints original list for verification
# print(middle(list2))
# print(list2)

#
#
# Exercise 2: Figure out which line of the above program is still not properly guarded. See if you can construct a
# text file which causes the program to fail and then modify the program so that the line is properly guarded and test
# it to make sure it handles your new text file.
#
# Program in question:
#
# fhand = open('mbox-short-edit.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     # print 'Debug:', words
#     if len(words) == 0 : continue
#     if words[0] != 'From' : continue
#     print(words[2])

# File would fail for word lists of length 1 or 2, as well as the 0 above. Try with 'mbox-short-edit.txt' - file I made
# with a single line of 'From' on it to test if this is correct. Yes, was the case.
#
# New code to take care of this:

# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     # print 'Debug:', words
#     if len(words) < 3 : continue # Change this line for anything less than len == 3, words[2].
#     if words[0] != 'From' : continue
#     print(words[2])

# Exercise 3: Rewrite the guardian code in the above example without two if statements. Instead, use a compound logical
# expression using the and (should be 'or') logical operator with a single if statement.

# print('Exercise 3')

# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     # print 'Debug:', words
#     if len(words) < 3 or words[0] != 'From': continue # New compound statement. Order matters!
#     # if words[0] != 'From' : continue
#     print(words[2])

# Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt. Write a program to open the file romeo.txt and
# read it line by line. For each line, split the line into a list of words using the split function. For each word,
# check to see if the word is already in a list. If the word is not in the list, add it to the list. When the program
# completes, sort and print the resulting words in alphabetical order.

# word_list = []
#
# fhand = open('romeo.txt')
# for line in fhand:
#     words = line.split() # Splits lines into a list of words
#     for word in words:
#         if word in word_list: continue # checks if word is in the word list
#         word_list.append(word)
# print(sorted(word_list))

# Exercise 5: Write a program to read through the mail box data and when you find line that starts with "From", you
# will split the line into words using the split function. We are interested in who sent the message, which is the
# second word on the From line.
#
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each From line, then you will also count the number of
# From (not From:) lines and print out a count at the end.

# Ask for the file and make sure it is readable
# fname = input('Enter a file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('Invalid file.')
#     exit()
# count = 0
# for line in fhand:
#     line = line.rstrip()
#     words = line.split()
#     if len(words) < 3 or words[0] != 'From': continue # Takes out lines with only From or not a From line
#     print(words[1]) # Prints email
#     count += 1 # Increases count by one.
# print('There were', count, "lines in the file with From as the first word.")

# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of
# the numbers at the end when the user enters "done". Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

print('Max: ', max(numlist))
print('Min: ', min(numlist))