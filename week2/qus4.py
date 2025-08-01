unp = input("Enter numbers separated by space: ")
num_list = list(map(int, unp.split()))
print("Even numbers in the list:")
for n in num_list:
    if n % 2 == 0:
        print(n)
