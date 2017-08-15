# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

# ENTER CODE BELOW HERE
search_string = "zip"

#find FIRST occurrence
first_occurrence = text.find(search_string)

#find SECOND occurrence (if FIRST is -1, SECOND will be -1 too!)
second_occurrence = text.find(search_string, first_occurrence + 1)

print second_occurrence 

# IMPORTANT BEFORE SUBMITTING: 
# You should only have one print command in your function
