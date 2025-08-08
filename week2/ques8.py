'''8. Write a python program to read a txt file and replace the contents of the file with “Hi, I am currently pursuing my BTech from Jaypee.”
 '''# Number of terms
# File name
filename = "sample.txt"

# New content
new_content = "Hi, I am currently pursuing my BTech from Jaypee."

# Write new content to the file
with open(filename, "w") as file:
    file.write(new_content)

print("File content replaced successfully.")

