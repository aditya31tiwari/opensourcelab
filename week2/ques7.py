# Number of terms
n = 5

# First two terms
a, b = 0, 1

print("Fibonacci series till 5th term:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
