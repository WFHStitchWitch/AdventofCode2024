import re

# Refined pattern to capture "mul(x,y)" with possible unwanted characters
pattern = r'mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)'

# Read the puzzle input from the file
with open('Day3_puzzleinput1', 'r') as textfile:
    chunk = textfile.read()

# Find all matches with the refined pattern
matches = re.findall(pattern, chunk)

if matches:
    uncorrupted_pairs = []
    for match in matches:
        x, y = match
        x = int(x)
        y = int(y)
        multiplier = x * y
        uncorrupted_pairs.append(multiplier)  # Ensure this line is inside the loop

    # Print the sum of all multipliers
    print("Sum of all multipliers:", sum(uncorrupted_pairs))
else:
    print("No matches found.")
