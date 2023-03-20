"""
# Display all odd numbers between 1 and 20
for i from 1 to 20 with step 2
    display i
display newline

# Count in 10s from 0 to 100
for i from 0 to 100 with step 10
    display i
display newline

# Count down from 20 to 1
for i from 20 to 1 with step -1
    display i
display newline

# Print n stars
get n
for i from 1 to n
    display '*'
display newline

# Print n lines of increasing stars
for i from 1 to n + 1
    for j from 1 to i
        display '*'
    display newline
"""

# Display all odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Print n stars
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()

# Print n lines of increasing stars
for i in range(1, n + 1):
    print('*' * i)