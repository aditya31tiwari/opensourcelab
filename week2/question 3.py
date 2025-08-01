'''1. Create a tuple of 5 students. Do the following :-
a. Display all the students.
b. Add new student.
c. Delete a student.
d. Use slicing to print students from the first index to third index.
e. Modify the second index value. Can you modify it?'''

students= ("aditya","alok","devansh","ravi","helium");
print(students);

students = students + ("Himesh",);
print(students);

st_list = list(students);
st_list.remove("ravi");
students = tuple(st_list);
print (students);

print(students[1:4]);

#Just like while deleting the element, we need to covert it into a temporary LIST, and then do the deed.
st_list = list(students);
st_list[2] = "Heer";
students = tuple(st_list);
print(students);
