# Create an empty list to store the numbers
numbers = []

# Prompt the user to enter numbers
while True:
    user_input = input("Enter a number: ")

    # Check if the user entered "done"
    if user_input == "done":
        break

    # Try to convert the input to a float
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")
        continue

    # Add the number to the list
    numbers.append(number)

# Check if the list is not empty
if numbers:
    # Compute the maximum and minimum values
    maximum = max(numbers)
    minimum = min(numbers)

    # Print the maximum and minimum values
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
else:
    print("No numbers were entered.")