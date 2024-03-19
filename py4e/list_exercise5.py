# Open the mailbox file
file_name = input("Enter a file name: ")
try:
    fhand = open(file_name)
except FileNotFoundError:
    print("File not found:", file_name)
    exit()

# Initialize the count
count = 0

# Loop through each line in the file
for line in fhand:
    # Check if the line starts with "From "
    if line.startswith("From "):
        # Split the line into words
        words = line.split()
        # Print the second word (email address)
        print(words[1])
        # Increment the count
        count += 1

# Print the count of "From" lines
print(f"There were {count} lines in the file with From as the first word")