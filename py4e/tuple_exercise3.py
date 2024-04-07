import string

file_name = input("Enter a file name: ")
try:
    with open(file_name, encoding='utf-8') as fhand:
        text = fhand.read()
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
    exit()

letter_counts = dict()
for char in text.lower():
    if char.isalpha() and char in string.ascii_lowercase:
        letter_counts[char] = letter_counts.get(char, 0) + 1

sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

for letter, count in sorted_letters:
    print(f"{letter} {count}")