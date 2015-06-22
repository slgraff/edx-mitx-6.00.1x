# pset1countingVowels.py
# Problem Set 1 - Counting Vowels
#
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:
#
# Number of vowels: 5

# For problems like this, do not include raw_input statements 
# or define the variable s in any way. Assume 's' is already defined

# NOTE: for my development and testing am including the following raw_input
# and definition of 's'. Comment out before submitting for grading
# s = "azcbobobegghakl"
# s = "now is the time for all good men to come to the aid of their country"

# Initialize numVowels and index
numVowels = 0
index = 0

# Loop through the string to find all vowels a,e,i,o,u
while index < len(s):
    if s[index] == "a" or s[index] == "e" or s[index] == "i" or s[index] == "o" \
    or s[index] == "u":
        # Increment numVowels
        numVowels += 1
    
    # Iterate index
    index += 1

#When done iterating through string print total number of vowels
print "Number of vowels: " + str(numVowels)

