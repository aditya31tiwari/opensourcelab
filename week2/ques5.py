'''5. Write a python program to print all the duplicate elements in the list '''# Sample list with duplicates
numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1, 9, 5]

# Set to store seen elements
seen = set()
# Set to store duplicates
duplicates = set()

# Loop through the list
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

# Print the duplicates
print("Duplicate elements in the list:")
for dup in duplicates:
    print(dup)
