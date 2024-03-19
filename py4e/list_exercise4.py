# Open the file and read its contents
with open('romeo.txt', 'r') as file:
    contents = file.read().replace('\n', ' ')

# Split the contents into a list of words
words = contents.split()

# Create an empty list to store unique words
unique_words = []

# Iterate through the list of words
for word in words:
    # Check if the word is already in the list of unique words
    if word not in unique_words:
        # If not, add it to the list of unique words
        unique_words.append(word)

# Sort the list of unique words in alphabetical order
unique_words.sort()

# Print the sorted list of unique words
print("Unique words in the file:")
for word in unique_words:
    print(word)