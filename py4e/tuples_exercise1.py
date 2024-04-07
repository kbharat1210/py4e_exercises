# Open the file for reading
file_name = input("Enter a file name:")
try:
    fhand = open(file_name)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
    exit()

# Initialize a dictionary to count the emails
email_counts = {}

# Read and parse the file line by line
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        email_counts[email] = email_counts.get(email, 0) + 1

# Close the file
fhand.close()

# Create a list of (count, email) tuples from the dictionary
email_list = list(email_counts.items())

# Sort the list in reverse order based on the count
email_list.sort(reverse=True)
count, email = email_list[0]

print(count,email)
