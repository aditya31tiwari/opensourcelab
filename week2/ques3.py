'''3. Create a dictionary with key value as name and age. Do the
following:-
a. Display those students whose age is greater than 20.
b. Add one more student with age 30.
c. Display all the students using .items().
d. Delete a student.
e. Display the average age of all the students.
'''
# Step 1: Create the initial dictionary
students = {
    "Alice": 19,
    "Bob": 22,
    "Charlie": 20,
    "David": 21
}

# a. Display students whose age is greater than 20
print("Students older than 20:")
for name, age in students.items():
    if age > 20:
        print(f"{name}: {age}")

# b. Add one more student with age 30
students["Eve"] = 30
print("\nAdded Eve with age 30.")

# c. Display all students using .items()
print("\nAll students:")
for name, age in students.items():
    print(f"{name}: {age}")

# d. Delete a student (let's delete 'Charlie')
del students["Charlie"]
print("\nDeleted Charlie.")

# e. Display the average age of all the students
total_age = sum(students.values())
average_age = total_age / len(students)
print(f"\nAverage age of students: {average_age:.2f}")

