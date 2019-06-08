# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

vowels = {"a", "e", "i", "o", "u", "y", " "}
inpString = input("Please enter your string: ").lower()

# Set up two complete sets to use in formatting
setString = set(inpString)
setString_2 = set(inpString)

# Print the set
print("The set from your string is: ")
print(sorted(setString))

# Version 1: Loop
for vowel in vowels:
    if vowel in setString:
        setString.discard(vowel)

print("The set without vowels iterating is: ")
print(sorted(setString))

# Version 2: Use created set, then apply difference
print("The set without vowels using difference is: ")
print(sorted(setString_2.difference(vowels)))

# Version 3: Create set and apply difference in one line
finalSet = set(inpString).difference(vowels)
print("Final set: ")
print(sorted(finalSet))