# pattern_drawing.py

# Prompt the user to enter a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks side by side for each row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after printing one row
    print()
    # Increment the row counter
    row += 1
