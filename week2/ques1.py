'''1. Write a python program to initialize a list with 10 names of your
friends. Do the following :-
a. Print the first name.
b. Print the last name.
c. Use slicing to print the names from the third to the fifth index.
d. Use slicing to print the names in reverse order.
e. Use slicing to print the names from eight to third.'''


friends =["aditya","abc", "abc2","abc3","abc4","abc5","abc6","abc7","abc8","abc9","abc10"];

print("First Name in the list:", friends[0]);
print("Second Name in the list:", friends[1]);
print("Last Name in the list:", friends[10]);
print("Last Name, other method:", friends[-1]);
print("Reverse order", friends[::-1]);
print("From 3rd to 5th:", friends[3:6]);
print("From 8th to 3rd", friends[8:2:-1]);
