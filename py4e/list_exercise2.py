#The line print(words[2]) is not properly guarded in the current code.
# If the line from the file doesn't start with "From" or if it's a blank line,
# the code will execute without any issues.
# However, if the line starts with "From" but doesn't have at least three words,
# it will raise an IndexError when trying to access words[2].

#To construct a text file that causes the program to fail,
# we can create a file with a line that starts with "From" but has fewer than three words.

#To fix this issue, we can add a guard condition to check
#if the length of words is greater than or equal to 3 before accessing words[2]

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' or len(words) < 3:
        continue
    print(words[2])