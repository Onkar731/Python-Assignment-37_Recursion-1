"""
Write a recursive function to print first N natural numbers in reverse order
"""

# defining a recursive function "print_naturals_rev()" to print first N natural 
# numbers which takes a number as an argument and print the natural numbers
# in reverse order
def print_naturals_rev(num):
    if num == 1:
        print(num, end=' ')
    else:
        print(num, end=' ')
        print_naturals_rev(num-1)
        

# taking input from the user
N = int(input("Enter a number : "))

# calling print_naturals() to print N natural numbers
print_naturals_rev(N)