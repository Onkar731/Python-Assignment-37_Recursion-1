"""
Write a recursive function to print first N natural numbers
"""

# defining a recursive function to print first N natural numbers
# which takes a number as an argument and print the natural numbers
def print_naturals(num):
    if num == 1:
        print(num, end=' ')
    else:
        print_naturals(num-1)
        print(num, end=' ')
        

# taking input from the user
N = int(input("Enter a number : "))

# calling print_naturals() to print N natural numbers
print_naturals(N)